from src.pipelines.project1_llm_assistant import SimpleChatSession
from src.llm.base import LLMClient


class DummyLLM(LLMClient):
    def chat(self, messages, **kwargs) -> str:
        last_user = [m for m in messages if m["role"] == "user"][-1]["content"]
        return f"echo: {last_user}"


def test_simple_chat_session_round_trip():
    session = SimpleChatSession(DummyLLM())
    reply = session.ask("hello")
    assert "echo: hello" in reply

