import pytest

from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        "genre", ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"]
    )
    def test_set_book_genre_set_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    def test_get_book_genre_with_name(
        self, book_with_genre, book_name_genre, book_name, book_genre
    ):
        book_with_genre.get_book_genre(book_name_genre)
        assert book_name_genre.books_genre[book_name] == book_genre

    def test_get_books_with_specific_genre(
        self, book_with_genre, book_name, book_genre
    ):
        fantasy_books = book_with_genre.get_books_with_specific_genre(book_genre)
        assert fantasy_books == [book_name]

    def test_get_books_genre(self, book_with_genre, book_name, book_genre):
        expect = {book_name: book_genre}
        lst = book_with_genre.get_books_genre()
        assert lst == expect

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Винни-пух")
        collector.set_book_genre("Винни-пух", "Мультфильмы")
        children_book = collector.get_books_for_children()
        assert children_book == ["Винни-пух"]

    def test_get_books_for_children_not_for_children(self, collector):
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужастик")
        children_book = collector.get_books_for_children()
        assert children_book != ["Оно"]

    @pytest.mark.parametrize(
        "test_book_name", ["Винни-пух", "Гордость и предубеждение и зомби", "Оно"]
    )
    def test_add_book_in_favorites(self, collector, test_book_name):
        collector.add_new_book(test_book_name)
        collector.add_book_in_favorites(test_book_name)
        assert collector.favorites == [test_book_name]

    def test_delete_book_from_favorites(self, book_with_genre, book_name):
        book_with_genre.add_book_in_favorites(book_name)
        book_with_genre.delete_book_from_favorites(book_name)
        assert book_name not in book_with_genre.favorites

    @pytest.mark.parametrize(
        "test_book_name, test_genre",
        [
            ("Винни-пух", "Мультфильм"),
            ("Гордость и предубеждение и зомби", "Фантастика"),
        ],
    )
    def test_get_list_of_favorites_books(self, collector, test_book_name, test_genre):
        collector.add_new_book(test_book_name)
        collector.set_book_genre(test_book_name, test_genre)
        collector.add_book_in_favorites(test_book_name)

        collector.get_list_of_favorites_books()
        assert collector.favorites == [test_book_name]
