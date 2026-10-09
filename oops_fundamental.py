class Book:
  def __init__(self, title, author, age, summary):
    self.title = title
    self.author = author
    self.age = age
    self.summary = summary
    
  def display_details(self):
    print("Title:", self.title)
    print("Author:", self.author)
    print("Age:", self.age)
    print("Summary:', self.summary)
book1 = book("Harry Potter and the Philosopher's Stone", "J. K. Rowling","1997", "A young wizard who discovers his magical heritage.")
book2 = book("The Alchemist", "	Paulo Coelho", "1988", "A shepherd boy, in his journey across North Africa to the Egyptian pyramids after he dreams of finding treasure there.")
book3 = book("A Man Called Ove", "Fredrik Backman", "2012", "A grumpy man finds friendship and purpose.")

    book1.display_details()
    print()
    book2.display_details()
    print()
    book3.display_details()
    print()
    
