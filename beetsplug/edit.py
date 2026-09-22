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
# through: they are safe to represent in YAML and trust as returned from parsed
# YAML.
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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


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
        if _safe_value(obj, key, value):
            # A safe value that is faithfully representable in YAML.
            obj[key] = value
        else:
            # A value that should be edited as a string.
            obj[key] = str(value)


def _safe_value(obj, key, value):
    """Check whether the `value` is safe to represent in YAML and trust as
    returned from