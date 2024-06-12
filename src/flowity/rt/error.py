from __future__ import annotations


class RuntimeException(Exception):
    pass

class SymbolNotFunctionException(RuntimeException):
    
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(f"Symbol {name} is not a callable function")

class SymbolNotFoundException(RuntimeException):
    
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(f"Symbol {name} not found")