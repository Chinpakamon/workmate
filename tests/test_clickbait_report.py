from app.models import VideoMetric
from app.reports.clickbait import ClickbaitReport


def test_clickbait_filtering_and_sorting():
    data = [
        VideoMetric("low_ctr", 10, 20),
        VideoMetric("high_ctr_bad_ret", 20, 50),
        VideoMetric("valid1", 18, 30),
        VideoMetric("valid2", 25, 20),
    ]

    report = ClickbaitReport()
    result = report.generate(data)

    assert len(result) == 2
    assert result[0].title == "valid2"
    assert result[1].title == "valid1"
