import os

# Создали класс "Book". Объявили атрибуты и методы
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Функция "get_info" выводит все данные о книге
    def get_info(self):
        print('Название книги -', self.title)
        print('Автор книги -', self.author)
        print('Год издания -', self.year)


    # Функция "is_actual" определяет "возраст" книги 
    def is_actual(self):
        print("Введите настоящий год")
        a = int(input())
        if (a - self.year) > 5:
            pr = "старая"
        else:
            pr = "новая"  
        print(pr)

# Создание наследственного класса "EBook"
class EBook(Book):
    def __init__(self, title, author, year, file_size, format):
        super().__init__(title, author, year)
        self.file_size = file_size
        self.format = format

    # Создание метода tit
    def tit(self):
        book_titles = []
        for root, dirs, files in os.walk('Library'):
            print(files)
            book_titles = [book.rpartition('.')[0] for book in files]
            print(book_titles)
        return book_titles

    # Метод free для проверки бесплатности книги
    def free(self, book_titles):
        for i in range (0, len(book_titles)):
            if self.title in book_titles[i]:
                if "(free)" in book_titles[i]:
                    print("Данная книга бесплатна")
                else:
                    print("Данная книга не является бесплатной")
            else:
                pass

    # Импортировали функцию, выводящую информацию о книге
    def get_info(self):
        super().get_info()  # Используем метод родительского класса
        print('Количество страниц', self.file_size)
        print('Формат книги', self.format)

    # Ввели функцию, определяющую, есть ли книга с таким названием
    # (привели к нижнему регистру, убради пробелы)
    def search(self, book_titles):
        normalized_title = self.title.lower().replace(" (free)", "").strip()
        for title in book_titles:
            if normalized_title in title.lower():
                print("Есть в наличии")
                return
        print("Нет в наличии")

def main():

    my_book = EBook('War and Peace', 'Leo Tolstoy', 1972, 1300, 'средний')

    # Вызовите методы и передайте необходимые параметры
    titles = my_book.tit()  # Получим список названий книг
    my_book.free(titles)     # Передаем список названий
    my_book.get_info()       # Получаем информацию о книге
    my_book.search(titles)   # Проверяем наличие книги в списке

if __name__=="__main__":
    main()