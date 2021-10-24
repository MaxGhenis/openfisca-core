from __future__ import annotations

from typing import Optional, Sequence
from typing_extensions import TypedDict

import textwrap
from dataclasses import dataclass

from openfisca_core.types import HasRoles, SupportsRole


@dataclass
class Role:
    """Role of an :class:`.Entity` within a :class:`.GroupEntity`.

    Each :class:`.Entity` related to a :class:`.GroupEntity` has a
    :class:`.Role`. For example, if you have a family, its roles could include
    a parent, a child, and so on. Or if you have a tax household, its roles
    could include the taxpayer, a spouse, several dependents, and so on.

    Attributes:
        entity: Entity the :class:`.Role` belongs to.
        key: Key to identify the :class:`.Role`.
        plural: The ``key``, pluralised.
        label: A summary description.
        doc: A full description, dedented.
        max: Max number of members. Defaults to None.
        subroles: The ``subroles``. Defaults to None.

    Args:
        description: A dictionary containing most of the attributes.
        entity: :obj:`.Entity` the :class:`.Role` belongs to.

    Examples:
        >>> description = {
        ...     "key": "parent",
        ...     "label": "Parents",
        ...     "plural": "parents",
        ...     "doc": "The one or two adults in charge of the household.",
        ...     "max": 2,
        ...     }

        >>> role = Role(description, object())

        >>> repr(Role)
        "<class 'openfisca_core.entities.role.Role'>"

        >>> repr(role)
        'Role(parent)'

        >>> str(role)
        'parent'

    .. versionchanged:: 35.7.0
        Added documentation, doctests, and typing.

    """

    __slots__ = "entity", "key", "plural", "label", "doc", "max", "subroles"

    entity: HasRoles
    key: str
    plural: Optional[str]
    label: Optional[str]
    doc: Optional[str]
    max: Optional[int]
    subroles: Optional[Sequence[SupportsRole]]

    def __init__(self, description: RoleLike, entity: HasRoles) -> None:
        self.entity = entity
        self.key = description['key']
        self.plural = description.get('plural')
        self.label = description.get('label')
        self.doc = textwrap.dedent(str(description.get('doc', "")))
        self.max = description.get('max')
        self.subroles = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.key})"

    def __str__(self) -> str:
        return self.key


class RoleLike(TypedDict, total = False):
    """Base type for any data castable to a :class:`.Role`.

    .. versionadded:: 35.7.0

    """

    key: str
    plural: Optional[str]
    label: Optional[str]
    doc: Optional[str]
    max: Optional[int]
    subroles: Optional[Sequence[str]]
