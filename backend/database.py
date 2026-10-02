import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "bac_genus.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

SCHEMA = """
CREATE TABLE IF NOT EXISTS lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    summary TEXT,
    content TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson_id INTEGER,
    level TEXT NOT NULL,
    question TEXT NOT NULL,
    answer TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lesson_id) REFERENCES lessons(id)
);

CREATE TABLE IF NOT EXISTS topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    score INTEGER DEFAULT 0,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS uploads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name TEXT NOT NULL,
    original_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()

    seed_default_lessons()


def seed_default_lessons():
    conn = get_connection()
    existing = conn.execute("SELECT COUNT(*) FROM lessons").fetchone()[0]
    if existing > 0:
        conn.close()
        return

    default_lessons = [
        {
            "title": "المعرفة والواقع",
            "summary": "مفهوم المعرفة، مصادرها، وارتباطها بالواقع والوعي.",
            "content": "المعرفة هي إدراك الواقع بواسطة العقل. تنشأ المعرفة من الحواس، العقل، والتجربة. من أهم أسئلة الفلسفة: ما حقيقة المعرفة؟ هل هي موضوعة في الحس أم في العقل؟",
            "source": "محتوى أساسي"
        },
        {
            "title": "الوجود والإنسان",
            "summary": "الإنسان كوجود فلسفي، وارتباطه بالوجود والوعي.",
            "content": "الوجود سؤال فلسفي أساسي يطرحه الإنسان حول كيانه، الغاية، والاختيار. الإنسان كائن متأمل، يبحث عن معنى وجوده في العالم.",
            "source": "محتوى أساسي"
        },
        {
            "title": "الأخلاق والحرية",
            "summary": "العلاقة بين الأخلاق والحرية، والاختيار الإنساني.",
            "content": "الأخلاق تدور حول القيم والواجبات التي يختارها الإنسان. الحرية تعني قدرة الإنسان على اتخاذ القرار ويكون مسؤولاً عن أفعاله.",
            "source": "محتوى أساسي"
        }
    ]

    conn.executemany(
        "INSERT INTO lessons (title, summary, content, source) VALUES (?, ?, ?, ?)",
        [(item["title"], item["summary"], item["content"], item["source"]) for item in default_lessons]
    )
    conn.commit()
    conn.close()

