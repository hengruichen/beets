# This file is part of beets.
# Copyright 2016, Adrian Sampson.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

"""A Web interface to beets."""

import base64
import json
import os

import flask
from flask import g, jsonify
from unidecode import unidecode
from werkzeug.routing import BaseConverter, PathConverter

import beets.library
from beets import ui, util
from beets.plugins import BeetsPlugin

# Utilities.


def _rep(obj, expand=False):
    """Get a flat -- i.e., JSON-ish -- representation of a beets Item or
    Album object. For Albums, `expand` dictates whether tracks are
    included.
    """
    out = dict(obj)

    if isinstance(obj, beets.library.Item):
        if app.config.get("INCLUDE_PATHS", False):
            out["path"] = util.displayable_path(out["path"])
        else:
            del out["path"]

        # Filter all bytes attributes and convert them to strings.
        for key, value in out.items():
            if isinstance(out[key], bytes):
                out[key] = base64.b64encode(value).decode("ascii")

        # Get the size (in bytes) of the backing file. This is useful
        # for the Tomahawk resolver API.
        try:
            out["size"] = os.path.getsize(util.syspath(obj.path))
        except OSError:
            out["size"] = 0

        return out

    elif isinstance(obj, beets.library.Album):
        if app.config.get("INCLUDE_PATHS", False):
            out["artpath"] = util.displayable_path(out["artpath"])
        else:
            del out["artpath"]
        if expand:
            out["items"] = [_rep(item) for item in obj.items()]
        return out


def json_generator(items, root, expand=False):
    """Generator that dumps list of beets Items or Albums as JSON

    :param root:  root key for JSON
    :param items: list of :class:`Item` or :class:`Album` to dump
    :param expand: If true every :class:`Album` contains its items in the json
                   representation
    :returns:     generator that yields strings
    """
    yield '{"%s":[' % root
    first = True
    for item in items:
        if first:
            first = False
        else:
            yield ","
        yield json.dumps(_rep(item, expand=expand))
    yield "]}"


def is_expand():
    """Returns whether the current request is for an expanded response."""

    return flask.request.args.get("expand") is not None


def is_delete():
    """Returns whether the current delete request should remove the selected
    files.
    """

    return flask.request.args.get("delete") is not None


def get_method():
    """Returns the HTTP method of the current request."""
    return flask.request.method


def resource(name, patchable=False):
    """Decorates a function to handle RESTful HTTP requests for a resource."""

    def make_responder(retriever):
        def responder(ids):
            entities = [retriever(id) for id in ids]
            entities = [entity for entity in entities if entity]

            if get_method() == "DELETE":
                if app.config.get("READONLY", True):
                    return flask.abort(405)

                for entity in entities:
                    entity.remove(delete=is_delete())

                return flask.make_response(jsonify({"deleted": True}), 200)

            elif get_method() == "PATCH" and patchable:
                if app.config.get("READONLY", True):
                    return flask.abort(405)

                for entity in entities:
    
# ... [truncated] ...
tists = [row[0] for row in rows]
    return flask.jsonify(artist_names=all_artists)


# Library information.


@app.route("/stats")
def stats():
    with g.lib.transaction() as tx:
        item_rows = tx.query("SELECT COUNT(*) FROM items")
        album_rows = tx.query("SELECT COUNT(*) FROM albums")
    return flask.jsonify(
        {
            "items": item_rows[0][0],
            "albums": album_rows[0][0],
        }
    )


# UI.


@app.route("/")
def home():
    return