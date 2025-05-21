class Book:
    total_books = 0

    @classmethod
    def increament_books_count(cls):
     cls.total_books +=1

Book.increament_books_count()
Book.increament_books_count()

print(f"Total books in the library: {Book.total_books}")