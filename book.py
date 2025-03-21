import os



# Создали класс "Book". Объявили атрибуты и методы
class Book():
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year


        #  Функция "get_info" выводит все данные о книге (Почему не выделяется)
        #========================================================================
        def get_info(self):
            print('Название книги -',self.title)
            print('Автор книги -', self.author)
            print('Год издания -',self.year)


        # Функция "is_actual" определяет "возраст" книги (Почему не выделяется)
        #=====================================================================
        def is_actual(self):
            print("Введите настоящий год")
            a = int(input())
            if (a - self.year) > 5:
                pr = "старая"
            else:
                pr = "новая"  
            # Вывели результат
            print(pr)

#  Создание наследственного класса "EBook", импортировали методы родительского класса, 
# объявили новые атрибуты
class EBook (Book):
    def __init__ (self,file_size, format):
        super().__init__()
        self.file_size = file_size
        self.format = format


    # Создание списков, необходимых для дальнейшей работы
    title_list = []
    new_list = []


# Создали функцию, которая удалит расширение и оставит только названия книг(пока засплитованные)
    def tit(title_list,new_list):

        # Перенесли названия файлов в список (Почему append не выводится, а дальше сплит)
        #=================================================================================
        for root, dirs, files in os.walk('Library'):
            for file in files:
                title_list.append(file)


        # Разделили элементы списка при (до точки - после точки), одновременно
        #  создали новый список cleaned_titles с новыми значениями
        cleaned_titles = [title.split('.') for title in title_list]

        #Создали цикл, который удалит расширение (Не хочет выводить в блокноте изменения)
        #===================================================================================
        for i in range (0,len(cleaned_titles)):
            cleaned = cleaned_titles[i]
            del cleaned[-1] # Расширение (система спискок внутри списка)
            if len(cleaned)>1:
                unification = ''.join(cleaned)
                new_list.append(unification)
            else:
                new_list.append(cleaned)
        print(new_list)
            



    # Импортировали функцию, выводящую информацию о книге с использованием
    #  новых атрибутов
    def get_info(self):
            print('Название книги -',self.title)
            print('Автор книги -', self.author)
            print('Год издания -',self.year)
            print('Количество страниц', self.file_size)
            print('Формат книги', self.format)


    
    