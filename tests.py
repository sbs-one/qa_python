import pytest


from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize("books, expected_length", [
        (['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'], 2),
        (["Властелин колец"], 1)
    ])
    def test_add_new_book_add_two_books(self, books, expected_length):
        collector = BooksCollector()
        for book in books:
            collector.add_new_book(book)
        assert len(collector.get_books_genre()) == expected_length

    @pytest.mark.parametrize("book, expected_genre", [
        ("Властелин колец", ''),
        ("Властелин колец", "Фантастика")
    ])
    def test_set_book_genre(self, book, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, expected_genre)
        assert collector.get_book_genre(book) == expected_genre

    @pytest.mark.parametrize("book, genre, expected_genre", [
        ("Властелин колец", "Фантастика", "Фантастика")
    ])
    def test_get_book_genre(self, book, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        genre = collector.get_book_genre(book)
        assert genre == expected_genre

    @pytest.mark.parametrize("genre, expected_books", [
        ("Фантастика", ["Властелин колец"])
    ])
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Властелин колец", "Фантастика")
        collector.add_new_book("ОНО")
        collector.set_book_genre("ОНО", "Ужасы")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        books = collector.get_books_with_specific_genre(genre)
        assert books == expected_books

    @pytest.mark.parametrize("books, expected_genres", [
        (["Властелин колец", "ОНО"], {"Властелин колец": "Фантастика", "ОНО": "Ужасы"})
    ])
    def test_get_books_genre(self, books, expected_genres):
        collector = BooksCollector()
        for book in books:
            collector.add_new_book(book)
        collector.set_book_genre("Властелин колец", "Фантастика")
        collector.set_book_genre("ОНО", "Ужасы")
        genres = collector.get_books_genre()
        assert genres == expected_genres

    @pytest.mark.parametrize("books, expected_children_books", [
        (["Властелин колец", "Винни Пух", "Трое в лодке не считая собаки"], ["Властелин колец", "Винни Пух", "Трое в лодке не считая собаки"])
    ])
    def test_get_books_for_children(self, books, expected_children_books):
        collector = BooksCollector()
        for book in books:
            collector.add_new_book(book)
        collector.set_book_genre("Властелин колец", "Фантастика")
        collector.set_book_genre("Винни Пух", "Мультфильмы")
        collector.set_book_genre("Трое в лодке не считая собаки", "Комедии")
        children_books = collector.get_books_for_children()
        assert children_books == expected_children_books

    @pytest.mark.parametrize("book, expected_favorites", [
        ("Властелин колец", ["Властелин колец"])
    ])
    def test_add_book_in_favorites(self, book, expected_favorites):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        favorites = collector.get_list_of_favorites_books()
        assert favorites == expected_favorites

    @pytest.mark.parametrize("book, initial_favorites, expected_favorites", [
        ("Властелин колец", ["Властелин колец"], [])
    ])
    def test_delete_book_from_favorites(self, book, initial_favorites, expected_favorites):
        collector = BooksCollector()
        collector.add_new_book(book)
        for favorite in initial_favorites:
            collector.add_book_in_favorites(favorite)
        collector.delete_book_from_favorites(book)
        favorites = collector.get_list_of_favorites_books()
        assert favorites == expected_favorites

    @pytest.mark.parametrize("books, expected_favorites", [
        (["Властелин колец", "Винни Пух"], ["Властелин колец", "Винни Пух"])
    ])
    def test_get_favorites_list(self, books, expected_favorites):
        collector = BooksCollector()
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        favorites = collector.get_list_of_favorites_books()
        assert favorites == expected_favorites
