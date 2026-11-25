# === Stage 5: Удаление и восстановление ===
# Project: ComicShelf
import uuid


class ComicIssue:
    """Модель выпуска комикса с возможностью мягкого удаления."""

    def __init__(self, title, issue_number, publisher, status):
        self.id = uuid.uuid4()
        self.title = title
        self.issue_number = issue_number
        self.publisher = publisher
        self.status = status
        self.deleted = False

    def soft_delete(self):
        self.deleted = True

    def restore(self):
        self.deleted = False

    def __repr__(self):
        if self.deleted:
            return f'<ComicIssue deleted id={self.id}>'
        return f'<ComicIssue {self.id} title={self.title} issue={self.issue_number}>'


class ComicSeries:
    """Модель серии комиксов, содержащей выпуски."""

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.issues = []

    def add_issue(self, issue):
        self.issues.append(issue)

    def remove_issue(self, issue):
        self.issues.remove(issue)
        issue.soft_delete()

    def restore_issue(self, issue):
        issue.restore()
        self.issues.append(issue)

    def get_active_issues(self):
        return [i for i in self.issues if not i.deleted]

    def get_missing_issues(self, total_count):
        active = self.get_active_issues()
        active_numbers = sorted(i.issue_number for i in active)
        missing = []
        for number in range(1, total_count + 1):
            if number not in active_numbers:
                missing.append(number)
        return missing

    def __repr__(self):
        return f'<ComicSeries {self.id} name={self.name} issues={len(self.get_active_issues())}>'
