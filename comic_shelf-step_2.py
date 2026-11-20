# === Stage 2: Проверка полей ===
# Project: ComicShelf
import re


def normalize_title(title: str) -> str:
    if title is None:
        raise ValueError("Название не может быть пустым")
    cleaned = title.strip()
    if not cleaned:
        raise ValueError("Название не может быть пустым")
    return cleaned


def normalize_issue_number(issue: str) -> int:
    if issue is None:
        raise ValueError("Номер выпуска должен быть целым числом")
    cleaned = str(issue).strip()
    if not re.fullmatch(r"[+-]?\d+", cleaned):
        raise ValueError("Номер выпуска должен быть целым числом")
    return int(cleaned)


def normalize_publisher(publisher: str) -> str:
    if publisher is None:
        raise ValueError("Издательство не может быть пустым")
    cleaned = publisher.strip()
    if not cleaned:
        raise ValueError("Издательство не может быть пустым")
    return cleaned


def normalize_status(status: str) -> str:
    status = str(status).strip()
    if not status:
        raise ValueError("Состояние не может быть пустым")
    return status
