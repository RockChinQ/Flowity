# the runtime
from __future__ import annotations

import typing

from langchain_core.language_models.chat_models import BaseChatModel

from . import symbol, builtin
from ..parser import parser
from .error import *
from .context import Context, ContextStatus


class FlowityRuntime:

    def fill_builtins(self, context: Context):
        context.set_symbol(
            symbol.Symbol(
                name="$query",
                type=symbol.SymbolType.FUNCTION,
                value=builtin.BuiltinSymbols.query
            )
        )
        context.set_symbol(
            symbol.Symbol(
                name="$end",
                type=symbol.SymbolType.FUNCTION,
                value=builtin.BuiltinSymbols.end
            )
        )

    def run(
        self,
        code: str,
        model: BaseChatModel
    ) -> symbol.Symbol:
        
        ast = parser.parser.parse(code)

        context = Context(model=model)

        self.fill_builtins(context)

        context.status = ContextStatus.PROCESSING

        self.run_subtree(ast, context)

        return context.return_value

    def run_subtree(
        self,
        ast: typing.Union[tuple, str],
        context: Context
    ) -> symbol.Symbol:
        
        # if ast is not a tuple
        if isinstance(ast, str):
            return eval(ast)
        # if ast is a tuple
        else:
            if ast[0] == 'prompt':
                context.pending_prompt(ast[1])
                return
            elif ast[0] == 'assignment':
                symb_right = self.run_subtree(ast[2], context)

                symb = symbol.Symbol(
                    name=ast[1],
                    type=symb_right.type,
                    value=symb_right.value
                )

                context.set_symbol(symb)
                return symb
            elif ast[0] == 'function_call':
                return self.run_function(ast, context)
            elif ast[0] == 'program':
                for s in ast[1]:
                    self.run_subtree(s, context)
                    if context.status == ContextStatus.FINISHED:
                        break
                return
        
    def run_function(
        self,
        ast: tuple,
        context: Context
    ) -> symbol.Symbol:
        symb = context.get_symbol(ast[1])

        if symb.type == symbol.SymbolType.FUNCTION:
            return symb.value(ast[2], context)
        else:
            raise SymbolNotFunctionException(ast[1])
        
    

