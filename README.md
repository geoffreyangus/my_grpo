# README

## TODO

- [ ] Run VLLM with reasoning
- [ ] Run VLLM with python sandbox tool use
- [ ] Run VLLM with read_file(filename, start_line, end_line)
- [ ] Run TRL with GRPO
- [ ] Write reward functions representing the task (load model?)

## Lambda Labs

PLS SHUT DOWN THE GPU CLOUD INSTANCE WHEN YOU ARE DONE.

Start the instance, then update your ~/.ssh/config file to use the new IP address of the instance.
This should allow you to use `Remote - SSH: Connect to Host...` to connect to the instance.

In order to push the code, you have to use a GitHub PAT. You can set this in global git config
so that you don't have to type it every time.

```
git config --global credential.helper store
```

Then you can push the code.

```
git push
```

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

