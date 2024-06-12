from __future__ import annotations

import enum

from langchain_core.language_models.chat_models import BaseChatModel

from . import symbol
from .error import *


class ContextStatus(enum.Enum):

    PENDING = "pending"
    PROCESSING = "processing"
    FINISHED = "finished"


class Context:

    symbols: list[symbol.Symbol]

    cached_prompt: str = ""

    model: BaseChatModel

    return_value: symbol.Symbol = None

    status: ContextStatus = ContextStatus.PENDING

    def __init__(self, model: BaseChatModel) -> None:
        self.symbols = []
        self.model = model

    def pending_prompt(self, prompt: str):
        self.cached_prompt += prompt

    def pop_prompt(self) -> str:
        prompt = self.cached_prompt
        self.cached_prompt = ""
        return prompt
    
    def set_symbol(self, symb: symbol.Symbol):
        for i, s in enumerate(self.symbols):
            if s.name == symb.name:
                self.symbols[i] = symb
                return
        self.symbols.append(symb)

    def get_symbol(self, name: str) -> symbol.Symbol:
        for s in self.symbols:
            if s.name == name:
                return s
        raise SymbolNotFoundException(name)
