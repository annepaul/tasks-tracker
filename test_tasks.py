import tasks
import pytest

@pytest.fixture(autouse=True)
def temp_file(tmp_path, monkeypatch):
    monkeypatch.setattr(tasks, "FILE", tmp_path / "tasks.json")

def test_add_task():
    tasks.add_task("Buy milk")

    result = tasks.load_tasks()
    assert len(result) == 1
    assert result[0]["title"] == "Buy milk"
    assert result[0]["done"] is False

def test_mark_done():
    tasks.add_task("watch tv")
    tasks.mark_done(1)

    result = tasks.load_tasks()
    assert len(result) == 1
    assert result[0]["title"] == "watch tv"
    assert result[0]["done"] is True

def test_delete_task():
    tasks.add_task("Brush")
    tasks.add_task("clean")
    tasks.delete_task(1)

    result=tasks.load_tasks()
    assert len(result) == 1
    assert result[0]["title"] == "clean"

def test_delete_missing_id(capsys):
    tasks.add_task("Brush")
    tasks.delete_task(99)

    output = capsys.readouterr().out
    assert "No task with id 99" in output

    result = tasks.load_tasks()
    assert len(result) == 1
    assert result[0]["title"] == "Brush"

