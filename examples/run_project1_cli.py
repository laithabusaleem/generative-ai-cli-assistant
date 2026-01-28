import os
import sys
from pathlib import Path

from rich.console import Console
from rich.prompt import Prompt

# Ensure the local `src` directory is on sys.path so we can import pipelines.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from pipelines.project1_llm_assistant import (  # type: ignore  # noqa: E402
    load_config,
    build_llm_client,
    SimpleChatSession,
)


def main() -> None:
    console = Console()

    config_path = Path("config") / "project1_llm_assistant.yaml"
    if not config_path.exists():
        console.print(f"[red]Config file not found:[/red] {config_path}")
        raise SystemExit(1)

    cfg = load_config(str(config_path))

    # Only require an API key when using a real provider like OpenAI.
    if cfg.provider == "openai" and "OPENAI_API_KEY" not in os.environ:
        console.print(
            "[red]OPENAI_API_KEY is not set.[/red] "
            "Set it in your environment or switch the config provider to 'dummy'."
        )
        raise SystemExit(1)

    llm_client = build_llm_client(cfg)
    session = SimpleChatSession(llm_client)

    console.print("[bold green]Project 1 – LLM Assistant[/bold green]")
    console.print("Type 'exit' or 'quit' to end the session.\n")

    while True:
        user_input = Prompt.ask("[bold cyan]You[/bold cyan]")
        if user_input.strip().lower() in {"exit", "quit"}:
            console.print("[bold yellow]Goodbye![/bold yellow]")
            break

        reply = session.ask(user_input)
        console.print(f"[bold magenta]Assistant[/bold magenta]: {reply}\n")


if __name__ == "__main__":
    main()

