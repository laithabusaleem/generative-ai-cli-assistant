from dataclasses import dataclass
from typing import List, Dict

import yaml

from llm.base import LLMClient
from llm.openai_client import OpenAILLMClient
from llm.dummy_client import DummyLLMClient
from prompt_engineering.system_prompts import BASE_SYSTEM_PROMPT


@dataclass
class LLMConfig:
    provider: str
    name: str
    temperature: float
    max_tokens: int


def load_config(path: str) -> LLMConfig:
    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    model = raw.get("model", {})
    return LLMConfig(
        provider=model.get("provider", "openai"),
        name=model.get("name", "gpt-4.1-mini"),
        temperature=float(model.get("temperature", 0.7)),
        max_tokens=int(model.get("max_tokens", 512)),
    )


def build_llm_client(config: LLMConfig) -> LLMClient:
    if config.provider == "openai":
        return OpenAILLMClient(
            model_name=config.name,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
        )
    if config.provider == "dummy":
        return DummyLLMClient()

    raise ValueError(f"Unsupported provider: {config.provider}")


class SimpleChatSession:
    """Minimal conversational pipeline for Project 1."""

    def __init__(self, llm_client: LLMClient) -> None:
        self._llm_client = llm_client
        self._messages: List[Dict[str, str]] = [
            {"role": "system", "content": BASE_SYSTEM_PROMPT}
        ]

    def ask(self, user_input: str) -> str:
        self._messages.append({"role": "user", "content": user_input})
        reply = self._llm_client.chat(self._messages)
        self._messages.append({"role": "assistant", "content": reply})
        return reply

