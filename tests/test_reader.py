import tempfile
import pytest

from app.reader import read_files


def test_read_files_success():
    content = """title,ctr,retention_rate\ntest,20,30\n"""

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(content)
        f.flush()

        result = read_files([f.name])

    assert len(result) == 1
    assert result[0].title == "test"


def test_read_files_not_found():
    with pytest.raises(FileNotFoundError):
        read_files(["non_existent.csv"])
