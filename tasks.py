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

def mark_done(task_id):
    tasks=load_tasks()
    for t in tasks:
        if t["id"]==task_id:
            t["done"]=True
            save_tasks(tasks)
            print(f"Marked task {task_id} as done")
            return
    print(f"No task with id {task_id}")

def delete_task(task_id):
    tasks = load_tasks()
    remaining = [t for t in tasks if t["id"] != task_id]
    if len(remaining) == len(tasks):
        print(f"No task with id {task_id}")
        return
    save_tasks(remaining)
    print(f"Deleted task {task_id}")

import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple task tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task description")

    subparsers.add_parser("list", help="Show all tasks")

    done_parser = subparsers.add_parser("done", help="Completed a task")
    done_parser.add_argument("id", type=int, help="Task id")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task id")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_done(args.id)
    else:
        delete_task(args.id)

if __name__ == "__main__":
    main()