class Ebook():
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = 0
        self.is_open = False

    def show_status(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Number of pages: " + str(self.number_of_pages))
        print("Current page: " + str(self.current_page))
        if self.is_open:
            print("The book is open")
        else:
            print("The book is closed")


    def open(self):
        self.is_open = True
        self.current_page = 1
        print("Book opened")

    def close(self):
        self.is_open = False
        self.current_page = self.number_of_pages
        print("Book closed")

    def next_page(self):
        if self.is_open:
            self.current_page += 1
        else:
            print("The book is closed")

    def previous_page(self):
        if self.is_open:
            self.current_page -= 1
        else:
            print("The book is closed")

