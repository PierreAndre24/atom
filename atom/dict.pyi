# --------------------------------------------------------------------------------------
# Copyright (c) 2021, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# --------------------------------------------------------------------------------------
from typing import (
    Any,
    Dict as TDict,
    Optional,
    Tuple,
    Type,
    TypeVar,
    overload,
    Union,
)

from .catom import Member

T = TypeVar("T")

KT = TypeVar("KT")
VT = TypeVar("VT")
KT1 = TypeVar("KT1")
VT1 = TypeVar("VT1")
KT2 = TypeVar("KT2")
VT2 = TypeVar("VT2")

class Dict(Member[TDict[KT, VT], TDict[KT, VT]]):
    # Untyped
    @overload
    def __new__(
        cls,
        key: None = None,
        value: None = None,
        default: Optional[TDict] = None,
    ) -> Dict[Any, Any]: ...
    # Typed keys
    @overload
    def __new__(
        cls,
        key: Type[KT],
        value: None = None,
        default: Optional[TDict[KT, Any]] = None,
    ) -> Dict[KT, Any]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT]],
        value: None = None,
        default: Optional[TDict[KT, Any]] = None,
    ) -> Dict[KT, Any]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT], Type[KT1]],
        value: None = None,
        default: Optional[TDict[Union[KT, KT1], Any]] = None,
    ) -> Dict[Union[KT, KT1], Any]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT], Type[KT1], Type[KT2]],
        value: None = None,
        default: Optional[TDict[Union[KT, KT1, KT2], Any]] = None,
    ) -> Dict[Union[KT, KT1, KT2], Any]: ...
    @overload
    def __new__(
        cls,
        key: Member[KT, Any],
        value: None = None,
        default: Optional[TDict[KT, Any]] = None,
    ) -> Dict[KT, Any]: ...
    # Typed values
    @overload
    def __new__(
        cls,
        key: None,
        value: Type[VT],
        default: Optional[TDict[Any, VT]] = None,
    ) -> Dict[Any, VT]: ...
    @overload
    def __new__(
        cls,
        key: None,
        value: Tuple[Type[VT]],
        default: Optional[TDict[Any, VT]] = None,
    ) -> Dict[Any, VT]: ...
    @overload
    def __new__(
        cls,
        key: None,
        value: Tuple[Type[VT], Type[VT1]],
        default: Optional[TDict[Any, Union[VT, VT1]]] = None,
    ) -> Dict[Any, Union[VT, VT1]]: ...
    @overload
    def __new__(
        cls,
        key: None,
        value: Tuple[Type[VT], Type[VT1], Type[VT2]],
        default: Optional[TDict[Any, Union[VT, VT1, VT2]]] = None,
    ) -> Dict[Any, Union[VT, VT1, VT2]]: ...
    @overload
    def __new__(
        cls,
        key: None,
        value: Member[VT, Any] = None,
        default: Optional[TDict[Any, VT]] = None,
    ) -> Dict[Any, VT]: ...
    @overload
    def __new__(
        cls,
        key: None = None,
        *,
        value: Type[VT],
        default: Optional[TDict[Any, VT]] = None,
    ) -> Dict[Any, VT]: ...
    @overload
    def __new__(
        cls,
        key: None,
        *,
        value: Tuple[Type[VT]],
        default: Optional[TDict[Any, VT]] = None,
    ) -> Dict[Any, VT]: ...
    @overload
    def __new__(
        cls,
        key: None = None,
        *,
        value: Tuple[Type[VT], Type[VT1]],
        default: Optional[TDict[Any, Union[VT, VT1]]] = None,
    ) -> Dict[Any, Union[VT, VT1]]: ...
    @overload
    def __new__(
        cls,
        key: None = None,
        *,
        value: Tuple[Type[VT], Type[VT1], Type[VT2]],
        default: Optional[TDict[Any, Union[VT, VT1, VT2]]] = None,
    ) -> Dict[Any, Union[VT, VT1, VT2]]: ...
    @overload
    def __new__(
        cls,
        key: None = None,
        *,
        value: Member[VT, Any] = None,
        default: Optional[TDict[Any, VT]] = None,
    ) -> Dict[Any, VT]: ...
    # Typed key and value
    # value simple type
    @overload
    def __new__(
        cls,
        key: Type[KT],
        value: Type[VT],
        default: Optional[TDict[KT, VT]] = None,
    ) -> Dict[KT, VT]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT]],
        value: Type[VT],
        default: Optional[TDict[KT, VT]] = None,
    ) -> Dict[KT, Any]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT], Type[KT1]],
        value: Type[VT],
        default: Optional[TDict[Union[KT, KT1], VT]] = None,
    ) -> Dict[Union[KT, KT1], VT]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT], Type[KT1], Type[KT2]],
        value: Type[VT],
        default: Optional[TDict[Union[KT, KT1, KT2], VT]] = None,
    ) -> Dict[Union[KT, KT1, KT2], VT]: ...
    @overload
    def __new__(
        cls,
        key: Member[KT, Any],
        value: Type[VT],
        default: Optional[TDict[KT, VT]] = None,
    ) -> Dict[KT, VT]: ...
    # Value as single element tuple
    @overload
    def __new__(
        cls,
        key: Type[KT],
        value: Tuple[Type[VT]],
        default: Optional[TDict[KT, VT]] = None,
    ) -> Dict[KT, VT]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT]],
        value: Tuple[Type[VT]],
        default: Optional[TDict[KT, VT]] = None,
    ) -> Dict[KT, VT]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT], Type[KT1]],
        value: Tuple[Type[VT]],
        default: Optional[TDict[Union[KT, KT1], VT]] = None,
    ) -> Dict[Union[KT, KT1], VT]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT], Type[KT1], Type[KT2]],
        value: Tuple[Type[VT]],
        default: Optional[TDict[Union[KT, KT1, KT2], VT]] = None,
    ) -> Dict[Union[KT, KT1, KT2], VT]: ...
    @overload
    def __new__(
        cls,
        key: Member[KT, Any],
        value: Tuple[Type[VT]],
        default: Optional[TDict[KT, VT]] = None,
    ) -> Dict[KT, VT]: ...
    # Value as 2-tuple
    @overload
    def __new__(
        cls,
        key: Type[KT],
        value: Tuple[Type[VT], Type[VT1]],
        default: Optional[TDict[KT, Union[VT, VT1]]] = None,
    ) -> Dict[KT, Union[VT, VT1]]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT]],
        value: Tuple[Type[VT], Type[VT1]],
        default: Optional[TDict[KT, Union[VT, VT1]]] = None,
    ) -> Dict[KT, Union[VT, VT1]]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT], Type[KT1]],
        value: Tuple[Type[VT], Type[VT1]],
        default: Optional[TDict[Union[KT, KT1], Union[VT, VT1]]] = None,
    ) -> Dict[Union[KT, KT1], Union[VT, VT1]]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT], Type[KT1], Type[KT2]],
        value: Tuple[Type[VT], Type[VT1]],
        default: Optional[TDict[Union[KT, KT1, KT2], Union[VT, VT1]]] = None,
    ) -> Dict[Union[KT, KT1, KT2], Union[VT, VT1]]: ...
    @overload
    def __new__(
        cls,
        key: Member[KT, Any],
        value: Tuple[Type[VT], Type[VT1]],
        default: Optional[TDict[KT, Union[VT, VT1]]] = None,
    ) -> Dict[KT, Union[VT, VT1]]: ...
    # Value as 3-tuple
    @overload
    def __new__(
        cls,
        key: Type[KT],
        value: Tuple[Type[VT], Type[VT1], Type[VT2]],
        default: Optional[TDict[KT, Union[VT, VT1, VT2]]] = None,
    ) -> Dict[KT, Union[VT, VT1, VT2]]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT]],
        value: Tuple[Type[VT], Type[VT1], Type[VT2]],
        default: Optional[TDict[KT, Union[VT, VT1, VT2]]] = None,
    ) -> Dict[KT, Union[VT, VT1, VT2]]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT], Type[KT1]],
        value: Tuple[Type[VT], Type[VT1], Type[VT2]],
        default: Optional[TDict[Union[KT, KT1], Union[VT, VT1, VT2]]] = None,
    ) -> Dict[Union[KT, KT1], Union[VT, VT1, VT2]]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT], Type[KT1], Type[KT2]],
        value: Tuple[Type[VT], Type[VT1], Type[VT2]],
        default: Optional[TDict[Union[KT, KT1, KT2], Union[VT, VT1, VT2]]] = None,
    ) -> Dict[Union[KT, KT1, KT2], Union[VT, VT1, VT2]]: ...
    @overload
    def __new__(
        cls,
        key: Member[KT, Any],
        value: Tuple[Type[VT], Type[VT1], Type[VT2]],
        default: Optional[TDict[KT, Union[VT, VT1, VT2]]] = None,
    ) -> Dict[KT, Union[VT, VT1, VT2]]: ...
    # value as member
    @overload
    def __new__(
        cls,
        key: Type[KT],
        value: Member[VT, Any],
        default: Optional[TDict[KT, VT]] = None,
    ) -> Dict[KT, VT]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT]],
        value: Member[VT, Any],
        default: Optional[TDict[KT, VT]] = None,
    ) -> Dict[KT, Any]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT], Type[KT1]],
        value: Member[VT, Any],
        default: Optional[TDict[Union[KT, KT1], VT]] = None,
    ) -> Dict[Union[KT, KT1], VT]: ...
    @overload
    def __new__(
        cls,
        key: Tuple[Type[KT], Type[KT1], Type[KT2]],
        value: Member[VT, Any],
        default: Optional[TDict[Union[KT, KT1, KT2], VT]] = None,
    ) -> Dict[Union[KT, KT1, KT2], VT]: ...
    @overload
    def __new__(
        cls,
        key: Member[KT, Any],
        value: Member[VT, Any],
        default: Optional[TDict[KT, VT]] = None,
    ) -> Dict[KT, VT]: ...
