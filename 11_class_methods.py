class Book:
  total_books = 0 # class veriable

  def __init__(self, title, author):  # instance attributes or veriable
    self.title = title
    self.author = author

    # call Class Method
    Book.increment_book_count()

  @classmethod
  def increment_book_count(cls):        # class Methods
    cls.total_books += 1

  def display_book_info(self):         # instance Methods
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    print()
    
  @classmethod                             # class Methods
  def display_total_books(cls):
    print(f"Total Books: {Book.total_books}")

book1 = Book("Python Programming", "Asad Ali")   # Object
book2 = Book("Data Science", "Ali")
book1.display_book_info()
book2.display_book_info()

Book.display_total_books()  # class Method Call

