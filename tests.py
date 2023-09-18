import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        assert "Властелин колец" in collector.get_books_genre()

    @pytest.mark.parametrize(
        'book, genre',
        [
            ["Властелин колец", "Фантастика"],
            ["ОНО", "Ужасы"]
        ]
    )
    def test_set_book_genre(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert genre in collector.get_book_genre(book)

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Властелин колец", "Фантастика")
        genre = collector.get_book_genre("Властелин колец")
        assert "Фантастика" in genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Властелин колец", "Фантастика")
        collector.add_new_book("ОНО")
        collector.set_book_genre("ОНО", "Ужасы")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        books = collector.get_books_with_specific_genre("Фантастика")
        assert "Властелин колец" in books

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Властелин колец", "Фантастика")
        collector.add_new_book("ОНО")
        collector.set_book_genre("ОНО", "Ужасы")
        genres = collector.get_books_genre()
        assert "Властелин колец" in genres and genres["Властелин колец"] == "Фантастика"
        assert "ОНО" in genres and genres["ОНО"] == "Ужасы"

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Властелин колец", "Фантастика")
        collector.add_new_book("Винни Пух")
        collector.set_book_genre("Винни Пух", "Мультфильмы")
        collector.add_new_book("Трое в лодке не считая собаки")
        collector.set_book_genre("Трое в лодке не считая собаки", "Комедии")
        collector.add_new_book("ОНО")
        collector.set_book_genre("ОНО", "Ужасы")
        children_books = collector.get_books_for_children()
        assert set(children_books) == {"Винни Пух", "Властелин колец", "Трое в лодке не считая собаки"}

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.add_book_in_favorites("Властелин колец")
        favorites = collector.get_list_of_favorites_books()
        assert "Властелин колец" in favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.add_book_in_favorites("Властелин колец")
        collector.delete_book_from_favorites("Властелин колец")
        favorites = collector.get_list_of_favorites_books()
        assert "Властелин колец" not in favorites

    def test_get_favorites_list(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.add_book_in_favorites("Властелин колец")
        collector.add_new_book("Винни Пух")
        collector.add_book_in_favorites("Винни Пух")
        favorites = collector.get_list_of_favorites_books()
        assert set(favorites) == {"Властелин колец", "Винни Пух"}
