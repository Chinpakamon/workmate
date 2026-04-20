from typing import List

from tabulate import tabulate

from app.models import VideoMetric


def print_report(data: List[VideoMetric]) -> None:
    table = [
        [v.title, v.ctr, v.retention_rate]
        for v in data
    ]

    print(tabulate(
        table,
        headers=["title", "ctr", "retention_rate"],
        tablefmt="github",
    ))
