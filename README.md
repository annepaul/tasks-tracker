# Task Tracker

A simple command-line to-do list written in Python. Tasks are saved
to a local JSON file, so they persist between sessions.

## Features

- we can add, list, complete and delete tasks
- Data is stored in a plain JSON file
- Tested with pytest
- Your tasks file will be present in your home folder

## Installation

```bash
git clone https://github.com/annepaul/tasks-tracker.git
cd YOUR-REPO
python -m venv venv
source venv/bin/activate    # Windows (Git Bash): source venv/Scripts/activate
pip install .
```

## Usage

```bash
python tasks.py add "Buy milk"
python tasks.py list
python tasks.py done 1
python tasks.py delete 1
```

Example output:

```
1. [ ] Buy milk
2. [x] watch tv
```

## Running tests

```bash
pytest
```

## What I Learned

Building this project taught me how to:

- Store and retrieve data using JSON files with Python's `pathlib` and `json` modules
- Build a command-line interface with `argparse` subcommands
- Handle edge cases, such as missing task IDs, with clear error messages
- Write automated tests with `pytest`, using fixtures like `tmp_path` and `monkeypatch` to keep tests isolated from real data
