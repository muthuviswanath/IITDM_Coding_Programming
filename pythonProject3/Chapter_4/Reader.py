class Nathanya:
    def reads(self,book):
        print(f"Nathanya reads {book.name}")
class Book:

    def __init__(self):
        self.name = "Rich Dad Poor Dad"

fb = Book()
n = Nathanya()
n.reads(fb)