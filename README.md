# Flowity

Workflow language designed for LLM.

## Installation

```bash
pip install flowity
```

## Write flowity code

```flowity
Hello, who are you?

$resp = $query()
$end($resp)
```

## Run a workflow

```python
import os

# === Setup Langchain ===

from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "sk-xxxx" # Your OpenAI api key
# Set OPENAI_API_BASE if you're using a reverse proxy
# os.environ["OPENAI_API_BASE"] = "https://api.openai.com/v1"

model = ChatOpenAI()

# === Write Flowity Code ===

code = """
Hello, who are you?

$str = $query()
$end($str)
"""

# === Run Flowity Code ===

from flowity.rt import rtime

rt = rtime.FlowityRuntime()

ret = rt.run(
    code=code,
    model=model
)

print(ret)
```