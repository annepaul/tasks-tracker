import json
from pathlib import Path

FILE = Path("tasks.json")

def load_tasks():
    if not FILE.exists():
        return []
    return json.loads(FILE.read_text())

def save_tasks(tasks):
    FILE.write_text(json.dumps(tasks, indent=2))

def add_task(title):
    tasks= load_tasks()
    new_id= max((t["id"] for t in tasks), default=0) + 1
    new={"id": new_id,"title":title,"done":False}
    tasks.append(new)
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        mark = "[x]" if t["done"] else "[ ]"
        print(f"{t['id']}. {mark} {t['title']}")