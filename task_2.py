from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title, author, year):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass

    @abstractmethod
    def show_books(self):
        pass

    @abstractmethod
    def search_book(self, title):
        pass

class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break
        else:
            print(f"Book with title '{title}' not found.")

    def show_books(self):
        for book in self.books:
            print(book)
            
    def search_book(self, title):
        found = [book for book in self.books if book.title == title]
        if found:
            for book in found:
                print(book)
        else:
            print(f"Book with title '{title}' not found.")

class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def run(self):
        while True:
            command = input("Enter command (add, remove, show, search, exit): ").strip().lower()
            
            if command == "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                self.library.add_book(title, author, year)
            elif command == "remove":
                title = input("Enter book title to remove: ").strip()
                self.library.remove_book(title)
            elif command == "show":
                self.library.show_books()
            elif command == "search":
                title = input("Enter book title to search: ").strip()
                self.library.search_book(title)
            elif command == "exit":
                break
            else:
                print("Invalid command. Please try again.")

def main():
    library = Library()
    manager = LibraryManager(library)
    manager.run()

if __name__ == "__main__":
    main()

