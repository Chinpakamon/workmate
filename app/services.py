from typing import Dict, Type, List

from app.models import VideoMetric
from app.reports.base import BaseReport
from app.reports.clickbait import ClickbaitReport


REPORT_REGISTRY: Dict[str, Type[BaseReport]] = {
    "clickbait": ClickbaitReport,
}


def get_report(name: str) -> BaseReport:
    try:
        return REPORT_REGISTRY[name]()
    except KeyError:
        raise ValueError(f"Unknown report: {name}")


def build_report(report_name: str, data: List[VideoMetric]) -> List[VideoMetric]:
    report = get_report(report_name)
    return report.generate(data)
