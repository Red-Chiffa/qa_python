import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def books_collector_obj():
    books_collector_obj = BooksCollector()
    return books_collector_obj


@pytest.fixture
def set_books_genre_for_test(books_collector_obj):
    books_collector_obj.books_genre['Фантастические твари'] = 'Фантастика'
    books_collector_obj.books_genre['Крик'] = 'Ужасы'
    books_collector_obj.books_genre['Шерлок Холмс'] = 'Детективы'
    books_collector_obj.books_genre['Слон и Моська'] = 'Мультфильмы'
    books_collector_obj.books_genre['Бриллиантовая рука'] = 'Комедии'


@pytest.fixture
def add_books_in_favorites_for_tests(books_collector_obj, set_books_genre_for_test):
    books_collector_obj.add_book_in_favorites('Слон и Моська')
    books_collector_obj.add_book_in_favorites('Бриллиантовая рука')
