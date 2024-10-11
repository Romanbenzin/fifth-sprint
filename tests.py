import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_zero_books(self):
        collector = BooksCollector()
        assert len(collector.books_genre) == 0
        assert collector.books_genre == {}

    def test_add_new_book_long_book_title_pass(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомбиГордость ')
        assert len(collector.books_genre) == 0

    def test_add_new_book_short_book_title_pass(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize('name, genre', [['Война и мир', 'Ужасы'],['Мир и война', 'Детективы']])
    def test_set_book_genre_add_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert genre in collector.books_genre[name]

    def test_set_book_genre_not_add_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert '' in collector.books_genre['Гордость и предубеждение и зомби']

    @pytest.mark.parametrize('name, genre', [['Война и мир', 'Ужасы'], ['Пила','Комедии']])
    def test_set_book_genre_if_book_not_in_list(self, name, genre):
        collector = BooksCollector()
        collector.set_book_genre(name, genre)
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize('name, genre', [['Война и мир', 'Ужасы'], ['Интерстеллар', 'Фантастика']])
    def test_get_book_genre_check_book_in_list(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert genre in collector.get_book_genre(name)

    def test_get_book_genre_non_existent_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Ужасы')

        assert 'Детектив' not in collector.get_book_genre('Война и мир')

    @pytest.mark.parametrize('name ,genre', [['Война и мир', 'Ужасы'], ['Собаки', 'Ужасы'], ['Кошки', 'Ужасы']])
    def test_get_books_with_specific_genre_check_count_book(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_new_book('Птицы')
        collector.set_book_genre('Птицы', 'Детективы')

        assert len(collector.get_books_with_specific_genre(genre)) == 1
        assert len(collector.get_books_with_specific_genre('Детективы')) == 1

    @pytest.mark.parametrize('name, genre', [['Война и мир', 'Ужас'],['Война и мир', 'Детектор']])
    def test_get_books_with_specific_genre_no_such_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 0

    @pytest.mark.parametrize('name, genre', [['Война и мир', 'Ужасы'],['Лунтик', 'Мультфильмы']])
    def test_get_books_genre_show_list(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        expected = {name: genre}
        assert collector.get_books_genre() == expected

    @pytest.mark.parametrize('name, genre', [['Лунтик', 'Мультфильмы'],['Бин', 'Комедии']])
    def test_get_books_for_children_show_list(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name,genre)
        expected = [name]
        assert collector.get_books_for_children() == expected

    @pytest.mark.parametrize('name, genre', [['Пила 1', 'Ужасы'], ['Пила 2', 'Ужасы'], ['Детектор', 'Детективы']])
    def test_get_books_for_children_add_horror(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Пила')
        collector.set_book_genre(name, genre)
        expected = []
        assert collector.get_books_for_children() == expected

    def test_add_book_in_favorites_add_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Пила')
        collector.set_book_genre('Пила', 'Ужасы')
        collector.add_book_in_favorites('Пила')
        assert 'Пила' in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name', ['Пила 1', 'Пила 2'])
    def test_add_book_in_favorites_book_not_in_favorites_list(self, name):
        collector = BooksCollector()
        collector.add_book_in_favorites(name)
        assert [] == collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name, genre', [['Пила 1', 'Ужасы'], ['Пила 2', 'Фантастика']])
    def test_delete_book_from_favorites_delete_book_from_list(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert [] == collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_non_existent_film(self):
        collector = BooksCollector()
        collector.add_new_book('Пила')
        collector.set_book_genre('Пила', 'Ужасы')
        collector.add_book_in_favorites('Пила')
        collector.delete_book_from_favorites('Не удаленный')
        assert ['Пила'] == collector.get_list_of_favorites_books()