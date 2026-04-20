import csv
from pathlib import Path
from typing import Iterable, List

from app.models import VideoMetric


def read_files(file_paths: Iterable[str]) -> List[VideoMetric]:
    result: List[VideoMetric] = []

    for path in file_paths:
        file = Path(path)

        if not file.exists():
            raise FileNotFoundError(f"File not found: {path}")

        with file.open(newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                result.append(
                    VideoMetric(
                        title=row["title"],
                        ctr=float(row["ctr"]),
                        retention_rate=float(row["retention_rate"]),
                    )
                )

    return result
