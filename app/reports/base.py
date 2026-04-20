from abc import ABC, abstractmethod
from typing import List

from app.models import VideoMetric


class BaseReport(ABC):
    @abstractmethod
    def generate(self, data: List[VideoMetric]) -> List[VideoMetric]:
        pass
