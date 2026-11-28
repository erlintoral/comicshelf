# === Stage 6: Связи между сущностями ===
# Project: ComicShelf
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ComicIssue:
    title: str
    number: int
    publisher: str
    status: str


@dataclass
class ComicSeries:
    name: str
    publisher: str
    _issues: List[ComicIssue] = field(default_factory=list)

    def add_issue(self, issue: ComicIssue) -> None:
        self._issues.append(issue)

    def get_issues_by_number(self) -> dict:
        return {issue.number: issue for issue in self._issues}


@dataclass
class IntegrityChecker:
    series: List[ComicSeries] = field(default_factory=list)

    def add_series(self, series: ComicSeries) -> None:
        self.series.append(series)

    def get_all_series_for_issue(self, issue: ComicIssue) -> List[ComicSeries]:
        result = []
        for series in self.series:
            if series.publisher == issue.publisher:
                result.append(series)
        return result

    def check_integrity(self, issue: ComicIssue) -> dict:
        series_list = self.get_all_series_for_issue(issue)
        issues_by_number = []
        for series in series_list:
            series_issues = series.get_issues_by_number()
            for number, comic_issue in series_issues.items():
                if comic_issue.title == issue.title and comic_issue.number == issue.number:
                    issues_by_number.append((series.name, comic_issue.status))
        return {
            "title": issue.title,
            "number": issue.number,
            "publisher": issue.publisher,
            "series_count": len(series_list),
            "matching_issues": issues_by_number,
            "is_consistent": len(issues_by_number) == len(series_list),
        }


def build_series_for_issue(issues: List[ComicIssue]) -> List[ComicSeries]:
    series_map = {}
    for issue in issues:
        if issue.publisher not in series_map:
            series_map[issue.publisher] = ComicSeries(name=issue.publisher, publisher=issue.publisher)
        series_map[issue.publisher].add_issue(issue)
    return list(series_map.values())
