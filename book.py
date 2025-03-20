import os

class Book():
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

        def get_info(self):
            print('Название книги -',self.title)
            print('Автор книги -', self.author)
            print('Год издания -',self.year)

        def is_actual(self):
            if self.year > 5:
                pr = "старая"
            else:
                pr = "новая"  

            print(pr)


class EBook (Book):
    def __init__ (self,file_size, format):
        super().__init__()
        self.file_size = file_size
        self.format = format
        for root, dirs, files in os.walk:
            for file in files:
                if file.endswith('.txt'):
                    print(os.path.join(root, file))
                elif file.endwith('.pdf'):
                    print(os.path.join(root, file))
                elif file.endwith('.fb2'):
                    print(os.path.join(root, file))
                elif file.endwith('cpub'):
                    print(os.path.join(root, file))

            

        