import enum
from collections import defaultdict
from types import DynamicClassAttribute


class SelectionMeta(enum.EnumMeta):
    """Meta class for creating enumerated selection"""

    def __new__(metacls, cls, bases, classdict):
        labels = defaultdict(str)
        for key in classdict._member_names:
            value = classdict[key]
            if isinstance(value, (list, tuple)) and len(value) > 1:
                value, label = value
            else:
                label = key.replace("_", " ").title()
            labels[key] = label
            dict.__setitem__(classdict, key, value)
        cls = super().__new__(metacls, cls, bases, classdict)
        for member in cls:
            setattr(member, "_label_", labels[member.name])
        return enum.unique(cls)

    @property
    def as_selections(cls):
        """Return the list of enum members where each member presents as (name, label) tuple"""
        return [(member.value, member.label) for member in cls]


class Selection(enum.Enum, metaclass=SelectionMeta):
    """Base class for creating enumerated selection"""

    @DynamicClassAttribute
    def label(self):
        """The label of the Enum member."""
        return self._label_


class IntSelection(int, Selection):
    pass


class TextSelection(str, Selection):
    pass
