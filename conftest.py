import pytest

from main import BooksCollector

@pytest.fixture # фикстура, которая создаёт компанию
def collector():
    collector = BooksCollector()

    return collector