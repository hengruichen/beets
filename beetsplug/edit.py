# This file is part of beets.
# Copyright 2016
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

"""Open metadata information in a text editor to let the user edit it.
"""

import codecs
import os
import shlex
import subprocess
from tempfile import NamedTemporaryFile

import yaml

from beets import plugins, ui, util, config
from beets.dbcore import types
from beets.importer import action
from beets.ui.commands import PromptChoice, _do_query

# These "safe" types can avoid the format/parse cycle that most fields go
# through: they are safe to edit with native YAML types.
SAFE_TYPES = (types.BaseFloat, types.BaseInteger, types.Boolean)


class ParseError(Exception):
    """The modified file is unreadable. The user should be offered a chance to
    fix the error.
    """


def edit(filename, log):
    """Open `filename` in a text editor."""
    cmd = shlex.split(util.editor_command())
    cmd.append(filename)
    log.debug("invoking editor command: {!r}", cmd)
    try:
        subprocess.call(cmd)
    except OSError as exc:
        raise ui.UserError(
            "could not run editor command {!r}: {}".format(cmd[0], exc)
        )


def dump(arg):
    """Dump a sequence of dictionaries as YAML for editing."""
    return yaml.safe_dump_all(
        arg,
        allow_unicode=True,
        default_flow_style=False,
    )


def load(s):
    """Read a sequence of YAML documents back to a list of dictionaries
    with string keys.

    Can raise a `ParseError`.
    """
    try:
        out = []
        for d in yaml.safe_load_all(s):
            if not isinstance(d, dict):
                raise ParseError(
                    "each entry must be a dictionary; found {}".format(
                        type(d).__name__
                    )
                )

            # Convert all keys to strings. They started out as strings,
            # but the user may have inadvertently messed this up.
            out.append({str(k): v for k, v in d.items()})

    except yaml.YAMLError as e:
        raise ParseError(f"invalid YAML: {e}")
    return out


def _safe_value(obj, key, value):
    """Check whether the `value` is safe to represent in YAML and trust as
    returned from parsed YAML.

    This ensures that values do not change their type when the user edits their
    YAML representation.
    """
    typ = obj._type(key)
    return isinstance(typ, SAFE_TYPES) and isinstance(value, typ.model_type)


def flatten(obj, fields):
    """Represent `obj`, a `dbcore.Model` object, as a dictionary for
    serialization. Only include the given `fields` if provided;
    otherwise, include everything.

    The resulting dictionary's keys are strings and the values are
    safely YAML-serializable types.
    """
    # Format each value.
    d = {}
    for key in obj.keys():
        value = obj[key]
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            d[key] = value
        else:
            # A value that should be edited as a string.
            d[key] = obj.formatted()[key]

    # Possibly filter field names.
    if fields:
        return {k: v for k, v in d.items() if k in fields}
    else:
        return d


def apply_(obj, data):
    """Set the fields of a `dbcore.Model` object according to a
    dictionary.

    This is the opposite of `flatten`. The `data` dictionary should have
    strings as values.
    """
    for key, value in data.items():
        # Convert the value to the appropriate type.
        typ = obj._type(key)
        if isinstance(typ, types.String):
            # Convert the value to a string.
            obj[key] = str(value)
        elif isinstance(typ, types.Integer):
            # Convert the value to an integer.
            obj[key] = int(value)
        elif isinstance(typ, types.Float):
            # Convert the value to a float.
            obj[key] = float(value)
        elif isinstance(typ, types.Boolean):
            # Convert the value to a boolean.
            obj[key] = bool(value)
        elif isinstance(typ, types.Date):
            # Convert the value to a date.
            obj[key] = util.date_from_string(value)
        elif isinstance(typ, types.DateTime):
            # Convert the value to a datetime.
            obj[key] = util.datetime_from_string(value)
        elif isinstance(typ, types.Bytes):
            # Convert the value to bytes.
            obj[key] = value.encode("utf-8")
        elif isinstance(typ, types.List):
            # Convert the value to a list.
            obj[key] = [value]
        elif isinstance(typ, types.ListString):
            # Convert the value to a list of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListInteger):
            # Convert the value to a list of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloat):
            # Convert the value to a list of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDate):
            # Convert the value to a list of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTime):
            # Convert the value to a list of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytes):
            # Convert the value to a list of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringList):
            # Convert the value to a list of lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerList):
            # Convert the value to a list of lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatList):
            # Convert the value to a list of lists of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateList):
            # Convert the value to a list of lists of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeList):
            # Convert the value to a list of lists of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesList):
            # Convert the value to a list of lists of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListList):
            # Convert the value to a list of lists of lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListList):
            # Convert the value to a list of lists of lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListList):
            # Convert the value to a list of lists of lists of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListList):
            # Convert the value to a list of lists of lists of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListList):
            # Convert the value to a list of lists of lists of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListList):
            # Convert the value to a list of lists of lists of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListList):
            # Convert the value to a list of lists of lists of lists of
            # strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListList):
            # Convert the value to a list of lists of lists of lists of
            # integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListList):
            # Convert the value to a list of lists of lists of lists of
            # floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListList):
            # Convert the value to a list of lists of lists of lists of
            # dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListList):
            # Convert the value to a list of lists of lists of lists of
            # datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListList):
            # Convert the value to a list of lists of lists of lists of
            # bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # floats.
            obj[key] = [float(value)]
        elif isinstance(typ, types.ListDateListListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # dates.
            obj[key] = [util.date_from_string(value)]
        elif isinstance(typ, types.ListDateTimeListListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # datetimes.
            obj[key] = [util.datetime_from_string(value)]
        elif isinstance(typ, types.ListBytesListListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # bytes.
            obj[key] = [value.encode("utf-8")]
        elif isinstance(typ, types.ListStringListListListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of strings.
            obj[key] = [str(value)]
        elif isinstance(typ, types.ListIntegerListListListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of lists of lists of lists of lists of lists of
            # lists of integers.
            obj[key] = [int(value)]
        elif isinstance(typ, types.ListFloatListListListListListListListListListListListListListListListList):
            # Convert the value to a list of lists of lists of lists of
            # lists of lists of lists of lists of lists of