"""Simple CLI for talking to STAI via OpenAI API."""

from __future__ import annotations

import os
from pathlib import Path


ENV_PATH = Path(__file__).parent / ".env"


def _require_deps() -> tuple:
    """Import optional dependencies when available."""
    try:
        from dotenv import load_dotenv  # type: ignore
        from openai import OpenAI  # type: ignore
        from rich.console import Console  # type: ignore
        from rich.markdown import Markdown  # type: ignore
    except Exception as exc:  # pragma: no cover - missing deps
        raise ImportError(
            "chat_cli requires 'python-dotenv', 'openai' and 'rich' packages"
        ) from exc
    return load_dotenv, OpenAI, Console, Markdown


def chat_loop() -> None:
    """Run an interactive chat session."""

    load_dotenv, OpenAI, Console, Markdown = _require_deps()

    if ENV_PATH.exists():
        load_dotenv(ENV_PATH)

    api_key = os.getenv("OPENAI_API_KEY")
    org_id = os.getenv("OPENAI_ORG_ID") or None
    model = os.getenv("MODEL_NAME", "gpt-4o-mini")

    if not api_key:
        raise RuntimeError(
            "\u06a9\u0644\u06cc\u062f OPENAI_API_KEY \u0631\u0627 \u062f\u0631 .env \u0648\u0627\u0631\u062f \u0646\u06a9\u0631\u062f\u0647\u200c\u0627\u06cc\u062f!"
        )

    client = OpenAI(api_key=api_key, organization=org_id)
    console = Console()

    system_path = Path(__file__).parent / ".." / "persona_system.txt"
    system_prompt = system_path.read_text(encoding="utf-8")
    messages = [{"role": "system", "content": system_prompt}]

    console.print('[bold green]\U0001f7e2 SSTAI ready. Type "exit" to quit.[/]\n')
    while True:
        try:
            user_in = input("\U0001f464 > ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[red]\u23f9 \u067e\u0627\u06cc\u0627\u0646[/]")
            break

        if user_in.lower() in {"exit", "quit"}:
            break

        messages.append({"role": "user", "content": user_in})

        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.4,
        )
        assistant_out = resp.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_out})

        console.print(Markdown(assistant_out))
        console.print()


if __name__ == "__main__":  # pragma: no cover - manual run
    chat_loop()
