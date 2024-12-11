from typing import List
from book import Book
import os
import sys
from datetime import datetime

books: List[Book] = []
        
def main():
    
    readBooks()
    cls()
    mainMenu()

def mainMenu():
    print("=== Library Manager ===")
    print("1. Add Book")
    print("2. List All Books")
    print("3. Search Books")
    print("4. Borrow/Return Book")
    print("5. Save and Exit")

    command = input("Input: ").strip().lower()

    match command:
        case "1":
            addBook()
        case "2":
            printBooks()
        case "3":
            searchBooks()
        case "4":
            borrowReturnBook()
        case "5":
            saveAndExit()
        case _:
            cls()
            print("Unsupported Input. Please enter a number between 1 and 5.\n")
            mainMenu()

def readBooks():

    global books
    books = []

    try:
        with open("library.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue
                
                props = line.split("|")
                title, author, year, borrowed = props
                borrowed = True if borrowed == "borrowed" else False
                year = int(year)

                books.append(Book(title, author, year, borrowed))
    except Exception as e:
        print(f"Could not read library file: '{e}'")

def addBook():
    cls()
    print("== Add book ==")
    author =  input("Author: ").strip().lower()
    title =  input("Title: ").strip().lower()
    year =  input("Year: ").strip().lower()

    if not year.isnumeric() or int(year) <= 0 or int(year) > datetime.now().year:
        print("Please enter a valid release year. Press any key to start again.")
        input()
        addBook()
        return

    newBook = Book(title, author, year)

    for book in books:
        if(book.title.lower() == newBook.title.lower()):
            print(f"The Book '{book.title}' is already in the library")
            return False

    saveBook(newBook)
    books.append(newBook)
    mainMenu()

def saveBook(book: Book, verbose=True):
    bookBorrowedString = "borrowed" if book.borrowed else "available"
    #f"..." -> formated string
    bookAsString = f"{book.title}|{book.author}|{book.year}|{bookBorrowedString}\n"

    try:
      #with -> context manager automatically closes file and creates the file in case it doesnt exist
      with open("library.txt", "a", encoding="utf-8") as file:
          file.write(bookAsString)
          if verbose:
            print(f"Book '{book.title}' was added to library")
    except Exception as e:
        print(f"Error while saving book '{book.title}': {e}")

def printBooks():
    cls()
    print("== List of Books ==")
    
    for book in books:
        print(f"{book.toString()}")

    print()
    mainMenu()

def searchBooks():
    cls()
    print("== Search Book ==")
    searchStr = input("Search for: ").strip().lower()

    found = False

    for book in books:
      
      if searchStr in book.author.lower() or searchStr in book.title.lower():
        print(f"Found book: {book.toString()}")
        found = True

    if not found:
        print("No Book matched the given search string.")

    print()
    mainMenu() 

def borrowReturnBook():
    cls()
    print("== Borrow/Return Book ==")
    for index, book in enumerate(books):
      print(f"{index+1}. {book.toString()}")

    print()
    command = input("Enter Book Nr: ").strip().lower()

    if not command.isnumeric() or int(command) <= 0 or int(command) > len(books):
        print("Please enter a valid book number. Press any key to start again.")
        input()
        borrowReturnBook()
        return

    selectedBook = books[int(command) - 1]

    if not selectedBook.borrowed:
      selectedBook.borrowBook()
    else:
      selectedBook.returnBook()
    
    print()

    mainMenu()

def saveAndExit():
    try:
      with open("library.txt", "r+", encoding="utf-8") as file:
          file.truncate(0)
    except Exception as e:
        print(f"Error while clearing library file: {e}")

    for book in books:
        saveBook(book, False)

    sys.exit()
    

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

main()