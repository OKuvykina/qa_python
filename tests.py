import pytest
from main import BooksCollector


class TestBooksCollector:

#тестируем органичение вводимого названия книги
    @pytest.mark.parametrize('name',
         [
            '',
            'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
         ]
    )
    def test_add_new_book_not_add_book(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        assert collector.get_books_genre() == {}

    # тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_this_book_empty_values(self):
        collector = BooksCollector()

        collector.add_new_book('101 долматинец')
        #проверяем что добавилась именно эта книга без жанра
        assert collector.get_books_genre() == {'101 долматинец':''}

    def test_set_book_genre_success_add_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Му-му')
        collector.set_book_genre('Му-му', 'Ужасы')

        assert collector.get_book_genre('Му-му') == 'Ужасы'


    def test_get_books_genre_is_empty(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    def test_get_books_with_specific_genre_have_book_with_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Операция Ы')
        collector.set_book_genre('Операция Ы', 'Комедии')
        assert collector.get_books_with_specific_genre('Комедии') == ['Операция Ы']

#проверяем что в детском списке нет книг с возрастным рейтингом
    def test_get_books_for_children_not_have_specific_genre_in_list(self):
        collector = BooksCollector()

        collector.add_new_book('Операция Ы')
        collector.set_book_genre('Операция Ы', 'Комедии')
        collector.add_new_book('Том и Джерри')
        collector.set_book_genre('Том и Джерри', 'Мультфильмы')
        assert (collector.get_books_with_specific_genre('Ужасы') and collector.get_books_with_specific_genre('Детективы')) not in collector.get_books_for_children()

        # добавляем 3 книги в Избранное
    def test_add_book_in_favorites_add_three_books(self):
        collector = BooksCollector()

        collector.add_new_book('Операция Ы')
        collector.add_new_book('Петр I')
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Операция Ы')
        collector.add_book_in_favorites('Петр I')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert len(collector.get_list_of_favorites_books()) == 3

        # удаляем книгу из Избранного
    def test_delete_book_from_favorites_not_success_del(self):
        collector = BooksCollector()

        collector.add_new_book('Операция Ы')
        collector.add_book_in_favorites('Операция Ы')
        collector.delete_book_from_favorites('Операция Ы ')
        assert 'Операция Ы' in collector.get_list_of_favorites_books()
