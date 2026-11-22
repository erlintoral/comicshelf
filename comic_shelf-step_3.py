# === Stage 3: Хранилище в памяти ===
# Project: ComicShelf
import hashlib


class ComicIssue:
    """Выпуск комикса."""

    def __init__(self, title, number, publisher, status):
        self.title = title
        self.number = number
        self.publisher = publisher
        self.status = status

    def to_dict(self):
        return {
            'title': self.title,
            'number': self.number,
            'publisher': self.publisher,
            'status': self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data['title'],
            number=data['number'],
            publisher=data['publisher'],
            status=data['status'],
        )


class IssueStore:
    """Хранилище в памяти для выпусков по хэшу идентификатора."""

    def __init__(self):
        self._issues = {}

    def add(self, issue):
        key = self._make_key(issue)
        self._issues[key] = issue
        return key

    def get(self, identifier):
        return self._issues.get(self._make_key(identifier))

    def list(self):
        return list(self._issues.values())

    def _make_key(self, issue):
        if isinstance(issue, ComicIssue):
            raw = f"{issue.title}|{issue.number}|{issue.publisher}|{issue.status}"
        else:
            raw = str(issue)
        return hashlib.sha256(raw.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    store = IssueStore()
    store.add(ComicIssue('Дэдпул', 1, 'Marvel', 'read'))
    store.add(ComicIssue('X-Men', 2, 'Marvel', 'pending'))
    print(store.get('0987654321'))
    for issue in store.list():
        print(issue.title, issue.number, issue.status)
