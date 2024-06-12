from __future__ import annotations

from langchain_core.messages import AIMessage, HumanMessage

from . import symbol, context


class BuiltinSymbols:

    def query(
        args: list[str],
        ctx: context.Context
    ) -> symbol.Symbol:
        
        cnt = ctx.model.invoke(
            [
                HumanMessage(
                    content=ctx.cached_prompt
                )
            ]
        )

        return symbol.Symbol(
            name="query",
            type=symbol.SymbolType.VARIABLE,
            value=cnt.content
        )
    
    def end(
        args: list[str],
        ctx: context.Context
    ) -> symbol.Symbol:
        ctx.status = context.ContextStatus.FINISHED
        ctx.return_value = ctx.get_symbol(args[0])
        return None
