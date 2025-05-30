from __future__ import annotations

import json
import os
import sqlite3
from importlib import resources
from typing import List, Dict

# Path to database file
DB_PATH = os.getenv(
    "SSTAI_DB_PATH",
    str((resources.files("sstai") / "data" / "lemmas.db").resolve()),
)


def init_db() -> None:
    """Create the lemmas table and populate it from lemmas.json if needed."""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS lemmas (code TEXT PRIMARY KEY, title TEXT)"
        )
        cur.execute("SELECT COUNT(*) FROM lemmas")
        count = cur.fetchone()[0]
        if count == 0:
            with resources.files("sstai.data").joinpath("lemmas.json").open("r", encoding="utf-8") as f:
                data = json.load(f)
            cur.executemany(
                "INSERT INTO lemmas (code, title) VALUES (?, ?)",
                [(d["code"], d["title"]) for d in data],
            )
            conn.commit()
    finally:
        conn.close()


def load_lemmas_from_db() -> List[Dict[str, str]]:
    """Load lemmas from the database, initializing it on first use."""
    init_db()
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("SELECT code, title FROM lemmas ORDER BY rowid")
        rows = cur.fetchall()
        return [{"code": c, "title": t} for c, t in rows]
    finally:
        conn.close()
