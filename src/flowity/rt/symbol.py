from __future__ import annotations

import pydantic
import enum
import typing


class SymbolType(enum.Enum):
    VARIABLE = "variable"
    FUNCTION = "function"


class Symbol(pydantic.BaseModel):
    name: str
    type: SymbolType
    value: typing.Any

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type and self.value == other.value


# class Variable(Symbol):
#     type = SymbolType.VARIABLE


# class Function(Symbol):
#     type = SymbolType.FUNCTION
