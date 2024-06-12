# Syntax

Currently supported syntax.

## Types

the same as in Python

## Operators

- `=`: assign a value to a variable

## Built-in functions

- `$query()`: make a llm query
- `$end($value)`: end the flow with a value

## Code

```flowity
Hello, who are you?

$resp = $query()
$end($resp)
```

Any statements not starting with `$` are considered as prompt, and will be sent to the model while calling `$query()`, the response will be stored in the variable `$resp`.
Prompt will be cached until the next `$query()` call.