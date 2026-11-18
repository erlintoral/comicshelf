# === Stage 1: Каркас модуля ===
# Project: ComicShelf
import random
from dataclasses import dataclass, field
from typing import List


@dataclass
class Issue:
    title: str
    number: int
    publisher: str
    state: str = "unknown"


def make_demo_issues() -> List[Issue]:
    data = [
        ("The Adventures of ComicShelf", 1, "DemoPress"),
        ("The Adventures of ComicShelf", 2, "DemoPress"),
        ("Mystery Series", 7, "MysteryHouse"),
        ("Space Odyssey", 12, "GalaxyBooks"),
        ("Space Odyssey", 13, "GalaxyBooks"),
        ("Space Odyssey", 14, "GalaxyBooks"),
        ("Space Odyssey", 15, "GalaxyBooks"),
        ("Space Odyssey", 16, "GalaxyBooks"),
    ]
    issues: List[Issue] = []
    for title, number, publisher in data:
        issues.append(Issue(
            title=title,
            number=number,
            publisher=publisher,
            state=random.choice(["read", "unread", "read", "lost", "unknown"]),
        ))
    return issues


def main() -> None:
    print("ComicShelf — Коллекция комиксов")
    print("=" * 30)
    for issue in make_demo_issues():
        print(f"[{issue.number}] {issue.title} ({issue.publisher}) — состояние: {issue.state}")
    print("=" * 30)


if __name__ == "__main__":
    main()
