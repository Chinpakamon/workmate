import pytest

from app.services import get_report


def test_get_report_success():
    report = get_report("clickbait")
    assert report is not None


def test_get_report_invalid():
    with pytest.raises(ValueError):
        get_report("unknown")
