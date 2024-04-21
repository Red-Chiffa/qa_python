import pytest


@pytest.mark.parametrize(
    'name,expected_result',
    [['', False],
     ['1', True],
     ['Слон и Моська', True],
     ['Очень длинное название книги проверка 40', True],
     ['Очень длинное название книги для проверки > 40', False]
     ]
)
def test_add_new_book_check_book_size(books_collector_obj, name, expected_result):
    books_collector_obj.add_new_book(name)
    actual_result = books_collector_obj.books_genre.get(name) is not None
    assert actual_result == expected_result


def test_add_new_book_added_book_has_no_genre(books_collector_obj):
    name = 'Слон и Моська'
    books_collector_obj.add_new_book(name)
    assert books_collector_obj.books_genre[name] == ''


def test_set_book_genre_added_book_set_genre(books_collector_obj):
    name = 'Слон и Моська'
    genre = 'Мультфильмы'
    books_collector_obj.add_new_book(name)
    books_collector_obj.set_book_genre(name, genre)
    assert books_collector_obj.books_genre[name] == genre


def test_get_book_genre(books_collector_obj):
    name = 'Слон и Моська'
    genre = 'Мультфильмы'
    books_collector_obj.add_new_book(name)
    books_collector_obj.set_book_genre(name, genre)
    assert books_collector_obj.get_book_genre(name) == genre


def test_get_books_with_specific_genre_book_and_genre_in_genre_show_books(books_collector_obj,
                                                                          set_books_genre_for_test):
    genre = 'Комедии'
    assert books_collector_obj.get_books_with_specific_genre(genre) == ['Бриллиантовая рука']


def test_get_books_genre_not_empty_books_genre(books_collector_obj, set_books_genre_for_test):
    book_genre = {'Фантастические твари': 'Фантастика',
                  'Крик': 'Ужасы',
                  'Шерлок Холмс': 'Детективы',
                  'Слон и Моська': 'Мультфильмы',
                  'Бриллиантовая рука': 'Комедии'}
    assert books_collector_obj.get_books_genre() == book_genre


def test_get_books_for_children_book_and_genre_in_genre_age_rating_show_books(books_collector_obj,
                                                                              set_books_genre_for_test):
    books_for_children = ['Фантастические твари', 'Слон и Моська', 'Бриллиантовая рука']
    assert books_collector_obj.get_books_for_children() == books_for_children


def test_get_books_for_children_book_and_genre_not_in_genre_age_rating_not_to_show_books(books_collector_obj,
                                                                                         set_books_genre_for_test):
    books_for_children = ['Крик', 'Шерлок Холмс']
    for book in books_for_children:
        assert book not in books_collector_obj.get_books_for_children()


def test_add_book_in_favorites_book_in_books_genre_book_added(books_collector_obj, set_books_genre_for_test):
    name = 'Шерлок Холмс'
    books_collector_obj.add_book_in_favorites(name)
    assert name in books_collector_obj.favorites


def test_delete_book_from_favorites_not_empty_favorites_book_deleted(books_collector_obj, set_books_genre_for_test,
                                                                     add_books_in_favorites_for_tests):
    name = 'Слон и Моська'
    books_collector_obj.delete_book_from_favorites(name)
    assert name not in books_collector_obj.favorites


def test_get_list_of_favorites_books_not_empty_favorites_show_books(books_collector_obj, set_books_genre_for_test,
                                                                    add_books_in_favorites_for_tests):
    favorites_books = ['Слон и Моська', 'Бриллиантовая рука']
    assert books_collector_obj.get_list_of_favorites_books() == favorites_books
