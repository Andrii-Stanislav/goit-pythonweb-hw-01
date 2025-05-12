from abc import ABC, abstractmethod
from typing import List
from logger import get_logger

logger = get_logger()


class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: str) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass

    @abstractmethod
    def search_book(self, title: str) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break
        else:
            logger.info(f"Book with title '{title}' not found.")

    def show_books(self) -> None:
        for book in self.books:
            logger.info(book)

    def search_book(self, title: str) -> None:
        found = [book for book in self.books if book.title == title]
        if found:
            for book in found:
                logger.info(book)
        else:
            logger.info(f"Book with title '{title}' not found.")


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def run(self) -> None:
        while True:
            command = (
                input("Enter command (add, remove, show, search, exit): ")
                .strip()
                .lower()
            )

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
                logger.info("Invalid command. Please try again.")


def main() -> None:
    library = Library()
    manager = LibraryManager(library)
    manager.run()


if __name__ == "__main__":
    main()
