# README

## TODO

- [ ] Run VLLM with reasoning
- [ ] Run VLLM with python sandbox tool use
- [ ] Run VLLM with read_file(filename, start_line, end_line)
- [ ] Run TRL with GRPO
- [ ] Write reward functions representing the task (load model?)

## Installation

Use UV to install an editable version of vLLM but do NOT use uv run because for some reason this
breaks the vllm package.

```
cd ~
git clone https://github.com/vllm-project/vllm.git
export VLLM_USE_PRECOMPILED=1
uv pip install -e ~/vllm
```

## Running

```
source .venv/bin/activate
python chat.py
```

PLS SHUT DOWN THE GPU CLOUD INSTANCE WHEN YOU ARE DONE.