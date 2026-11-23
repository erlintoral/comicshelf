# === Stage 4: Редактирование записей ===
# Project: ComicShelf
from dataclasses import dataclass, field
from datetime import date
from typing import List, Dict, Any


@dataclass
class Issue:
    title: str
    number: int
    publisher: str
    status: str = "published"
    release_date: date | None = None
    description: str = ""


ALLOWED_FIELDS = ("title", "number", "publisher", "status", "release_date", "description")
VALID_STATUSES = ("published", "planned", "cancelled", "on_hold", "abandoned", "incomplete")


@dataclass
class IssueValidator:
    """Проверяет допустимость полей при редактировании выпуска."""

    valid_statuses: tuple[str, ...] = VALID_STATUSES

    def validate(self, data: Dict[str, Any], original: Issue) -> bool:
        if not isinstance(data, dict):
            raise TypeError("data должен быть словарём")

        for key in data:
            if key not in ALLOWED_FIELDS:
                raise ValueError(f"Недопустимое поле для редактирования: {key}")

        for key, value in data.items():
            if key == "status":
                if value not in self.valid_statuses:
                    raise ValueError(f"Недопустимое состояние: {value}")
            elif key == "release_date":
                if value is not None:
                    self._validate_date(value)
            elif key in ("title", "publisher", "description"):
                if not isinstance(value, str):
                    raise TypeError(f"Поле {key} должно быть строкой")
            elif key == "number":
                if not isinstance(value, int) or isinstance(value, bool):
                    raise TypeError("Поле number должно быть целым числом")

        return True

    def _validate_date(self, value: Any) -> None:
        if not isinstance(value, date):
            raise TypeError("release_date должна быть объектом date")


@dataclass
class IssueEditor:
    validator: IssueValidator = field(default_factory=IssueValidator)

    def edit(self, issue: Issue, data: Dict[str, Any]) -> Issue:
        self.validator.validate(data, issue)

        new_issue = Issue(
            title=issue.title,
            number=issue.number,
            publisher=issue.publisher,
            status=issue.status,
            release_date=issue.release_date,
            description=issue.description,
        )

        for key, value in data.items():
            setattr(new_issue, key, value)

        return new_issue
