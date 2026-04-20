from typing import List

from app.models import VideoMetric
from app.reports.base import BaseReport


class ClickbaitReport(BaseReport):
    def generate(self, data: List[VideoMetric]) -> List[VideoMetric]:
        filtered = [
            v for v in data
            if v.ctr > 15 and v.retention_rate < 40
        ]

        return sorted(filtered, key=lambda x: x.ctr, reverse=True)
