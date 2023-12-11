import os
import pickle
from rich.console import Console

class LiteraryArchive:
    def __init__(self, filename="literary_archive.pkl"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def save_books(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.books, file)

    def clear_screen(self):
        console = Console()
        console.clear()

    def display_books(self):
        self.clear_screen()
        console = Console()
        console.print("*** Literary Archive ***")
        if not self.books:
            console.print("Your literary archive is empty.")
        else:
            for book in self.books:
                console.print(book)

    def add_book(self):
        self.clear_screen()
        console = Console()
        console.print("Acquiring a new literary treasure...")
        title = input("Enter the title of the book >>>")
        author = input("Enter the name of the author >>>")
        read_status = input("Have you read it before? >>>")
        pages = input("Enter the number of pages >>>")
        self.books.append({"Title": title, "Author": author, "Read Status": read_status, "Pages": pages})
        console.print("Book successfully added to your literary archive!")

    def search_books(self):
        self.clear_screen()
        console = Console()
        console.print("Searching the literary archive...")
        keyword = input("Enter search term: ")
        found_books = [book for book in self.books if any(keyword.lower() in value.lower() for value in book.values())]

        if not found_books:
            console.print("No matching books found in your archive.")
        else:
            for book in found_books:
                console.print(book)

    def run(self):
        console = Console()
        choice = 0

        while choice != 4:
            console.print("*** Literary Archive Manager ***")
            console.print("1) Add a new book")
            console.print("2) Search your literary archive")
            console.print("3) Display all books")
            console.print("4) Save and Exit")
            console.print("5) Exit without saving")
            choice = int(input())

            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.search_books()
            elif choice == 3:
                self.display_books()
            elif choice == 4:
                self.save_books()
                console.print("Your literary archive has been updated. Exiting.")
            elif choice == 5:
                console.print("Exiting without saving your literary archive.")
            else:
                console.print("Invalid choice. Please try again.")

if __name__ == "__main__":
    literary_archive = LiteraryArchive()
    literary_archive.run()
