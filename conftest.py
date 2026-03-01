import pytest


from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def book_name():
    return "Гордость и предубеждение и зомби"


@pytest.fixture
def book_genre():
    return "Фантастика"


@pytest.fixture
def book_name_genre(collector, book_name):
    collector.add_new_book(book_name)
    return collector


@pytest.fixture
def book_with_genre(book_name_genre, book_name, book_genre):
    book_name_genre.set_book_genre(book_name, book_genre)
    return book_name_genre
