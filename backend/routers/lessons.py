from typing import List, Optional

from database import get_connection


def add_lesson(title: str, summary: str, content: str, source: str = "uploaded") -> int:
    conn = get_connection()
    cur = conn.execute(
        "INSERT INTO lessons (title, summary, content, source) VALUES (?, ?, ?, ?)",
        (title, summary, content, source),
    )
    conn.commit()
    lesson_id = cur.lastrowid
    conn.close()
    return lesson_id


def get_lessons() -> List[dict]:
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM lessons ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_lesson_by_id(lesson_id: int) -> Optional[dict]:
    conn = get_connection()
    row = conn.execute("SELECT * FROM lessons WHERE id = ?", (lesson_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def add_exercise(lesson_id: int, level: str, question: str, answer: str = "") -> int:
    conn = get_connection()
    cur = conn.execute(
        "INSERT INTO exercises (lesson_id, level, question, answer) VALUES (?, ?, ?, ?)",
        (lesson_id, level, question, answer),
    )
    conn.commit()
    ex_id = cur.lastrowid
    conn.close()
    return ex_id


def get_exercises_by_lesson(lesson_id: int, level: Optional[str] = None) -> List[dict]:
    conn = get_connection()
    if level:
        rows = conn.execute(
            "SELECT * FROM exercises WHERE lesson_id = ? AND level = ? ORDER BY created_at DESC",
            (lesson_id, level),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM exercises WHERE lesson_id = ? ORDER BY created_at DESC",
            (lesson_id,),
        ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def save_upload(file_name: str, original_name: str, file_path: str) -> int:
    conn = get_connection()
    cur = conn.execute(
        "INSERT INTO uploads (file_name, original_name, file_path) VALUES (?, ?, ?)",
        (file_name, original_name, file_path),
    )
    conn.commit()
    upload_id = cur.lastrowid
    conn.close()
    return upload_id


def get_uploads() -> List[dict]:
    conn = get_connection()
    rows = conn.execute("SELECT * FROM uploads ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(row) for row in rows]


def upsert_topic(name: str, score: int, source: str = "analysis") -> None:
    conn = get_connection()
    existing = conn.execute("SELECT id, score FROM topics WHERE name = ?", (name,)).fetchone()
    if existing:
        new_score = existing["score"] + score
        conn.execute("UPDATE topics SET score = ?, source = ? WHERE id = ?", (new_score, source, existing["id"]))
    else:
        conn.execute("INSERT INTO topics (name, score, source) VALUES (?, ?, ?)", (name, score, source))
    conn.commit()
    conn.close()


def get_topics() -> List[dict]:
    conn = get_connection()
    rows = conn.execute("SELECT * FROM topics ORDER BY score DESC, name ASC").fetchall()
    conn.close()
    return [dict(row) for row in rows]


def reset_topics() -> None:
    conn = get_connection()
    conn.execute("DELETE FROM topics")
    conn.commit()
    conn.close()

