class Book:
    def __init__(self, title, author, year, borrowed=False):
        self.title = title
        self.author = author
        self.year = year
        self.borrowed = borrowed

    def borrowBook(self):
        if self.borrowed == False:
            self.borrowed = True
            print(f"Book '{self.title}' is now borrowed.")
        else:
            print(f"Book '{self.title}' is already borrowed.")

    def returnBook(self):
        if self.borrowed == True:
            self.borrowed = False
            print(f"Book '{self.title}' has been returned.")
        else:
            print(f"Book '{self.title}' was not borrowed.")

    def toString(self):
        return f"{self.title} by {self.author} ({self.year}) - {'borrowed' if self.borrowed else 'available'}"