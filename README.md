## Generative AI CLI Assistant

This repository contains a **single, production-style Generative AI CLI assistant**.

- **LLM-backed**: uses OpenAI by default with a clean abstraction layer.
- **Config-driven**: YAML config for model settings and runtime behavior.
- **Tested**: includes a small but realistic test of the chat pipeline.
- **Offline-friendly**: optional dummy mode for running without any API keys.

---

## LLM Assistant (CLI)

### Overview

This is a small but production-style CLI assistant:

- **Config-driven**: model, temperature, and tokens live in `config/`.
- **Separation of concerns**: LLM clients in `src/llm/`, prompts in `src/prompt_engineering/`, pipeline in `src/pipelines/`.
- **Tested**: a simple test in `tests/` shows how to unit test LLM pipelines via dummy clients.

### Installation

From the project root:

```bash
pip install -r requirements.txt
```

### Configuration

- **Default config (OpenAI)**: `config/project1_llm_assistant.yaml`
  - Uses `provider: openai` and a model like `gpt-4.1-mini`.
  - Requires `OPENAI_API_KEY` in your environment.

- **Offline config (Dummy)**: `config/project1_llm_assistant_dummy.yaml`
  - Uses `provider: dummy` and the `DummyLLMClient`.
  - No API calls, no key required (good for local demos and learning).

### Running the CLI

1. **With a real OpenAI key**:

   - Set your key (PowerShell example):

   ```powershell
   $env:OPENAI_API_KEY = "sk-..."
   ```

   - Ensure the default config points to OpenAI (already the case):

   ```yaml
   # config/project1_llm_assistant.yaml
   model:
     provider: openai
   ```

   - Run:

   ```bash
   python examples/run_project1_cli.py
   ```

2. **Offline / dummy mode**:

   - Switch the CLI to use the dummy config by editing `examples/run_project1_cli.py`
     to point to `project1_llm_assistant_dummy.yaml`, or temporarily copy that file
     over `project1_llm_assistant.yaml`.

   - Run the same command:

   ```bash
   python examples/run_project1_cli.py
   ```

### Running tests

```bash
pytest
```


