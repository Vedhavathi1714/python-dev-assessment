class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        return 2026 - int(self.publication_year)

    def get_summary(self):
        return (
            f"Title: {self.title}, Author: {self.author}, "
            f"Published: {self.publication_year}"
        )

book1 = Book(
    "Harry Potter and the Philosopher's Stone",
    "J. K. Rowling",
    "9780747536699",
    "1997"
)

book2 = Book(
    "The Alchemist",
    "Paulo Coelho",
    "9780061122415",
    "1988"
)

book3 = Book(
    "A Man Called Ove",
    "Fredrik Backman",
    "9781476738024",
    "2012"
)

books = [book1, book2, book3]


for book in books:
    print("Title:", book.title)
    print("Author:", book.author)
    print("Age:", book.get_age(), "years")
    print(book.get_summary())
    print()
