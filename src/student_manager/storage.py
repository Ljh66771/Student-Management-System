from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
DATA_FILE = DATA_DIR / "students.json"

def save_students(students):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

def load_students():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding = "utf_8") as f:
        return json.load(f)

if __name__ == "__main__":
    students = load_students()
    print(students)
    print(type(students))