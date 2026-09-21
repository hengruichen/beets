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
        
# ... [truncated] ...
                  if not obj.id < 0:
                            obj.load()
                    continue

        # Remove the temporary file before returning.
        finally:
            os.remove(new.name)

    def apply_data(self, objs, old_data, new_data):
        """Take potentially-updated data and apply it to a set of Model
        objects.

        The objects are not written back to the database, so the changes
        are temporary.
        """
        if len(old_data) != len(new_data):
            self._log.warning(
                "number of objects changed from {} to {}",
                len(old_data),
                len(new_data),
            )

        obj_by_id = {o.id: o for o in objs}
        ignore_fields = self.config["ignore_fields"].as_str_seq()
        for old_dict, new_dict in zip(old_data, new_data):
            # Prohibit any changes to forbidden fields to avoid
            # clobbering `id` and such by mistake.
            forbidden = False
            for key in ignore_fields:
                if old_dict.get(key) != new_dict.get(key):
                    self._log.warning("ignoring object whose {} changed", key)
                    forbidden = True
                    break
            if forbidden:
                continue

            id_ = int(old_dict["id"])
            apply_(obj_by_id[id_], new_dict)

    def save_changes(self, objs):
        """Save a list of updated Model objects to the database."""
        # Save to the database and possibly write tags.
        for ob in objs:
            if ob._dirty:
                self._log.debug("saving changes to {}", ob)
                ob.try_sync(ui.should_write(), ui.should_move())

    # Methods for interactive importer execution.

    def before_choose_candidate_listener(self, session, task):
        """Append an "Edit" choice and an "edit Candidates" choice (if
        there are candidates) to the interactive importer prompt.
        """
        choices = [PromptChoice("d", "eDit", self.importer_edit)]
        if task.candidates:
            choices.append(
                PromptChoice(
                    "c", "edit Candidates", self.importer_edit_candidate
                )
            )

        return choices

    def importer_edit(self, session, task):
        """Callback for invoking the functionality during an interactive
        import session on the *original* item tags.
        """
        # Assign negative temporary ids to Items that are not in the database
        # yet. By using negative values, no clash with items in the database
        # can occur.
        for i, obj in enumerate(task.items, start=1):
            # The importer may set the id to None when re-importing albums.
            if not obj._db or obj.id is None:
                obj.id = -i

        # Present the YAML to the user and let them change it.
        fields = self._get_fields(album=False, extra=[])
        success = self.edit_objects(task.items, fields)

        # Remove temporary ids.
        for obj in task.items:
            if obj.id < 0:
                obj.id = None

        # Save the new data.
        if success:
            # Return action.RETAG, which makes the importer write the tags
            # to the files if needed without re-applying metadata.
            return action.RETAG
        else:
            # Edit cancelled / no edits made. Revert changes.
            for obj in task.items:
                obj.read()

    def importer_edit_candidate(self, session, task):
        """Callback for invoking the functionality during an interactive
        import session on a *candidate*. The candidate's metadata is
        applied to the original items.
        """
        # Prompt the user for a candidate.
        sel = ui.input_options([], numrange=(1, len(task.candidates)))
        # Force applying the candidate on the items.
        task.match = task.candidates[sel - 1]
        task.apply_metadata()

        return self.importer_edit(session, task)

