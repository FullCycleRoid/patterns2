class Book:
    def __init__(self, content):
        self.content = content

    def read(self):
        return f"Reading book content: {self.content}"

class Ebook:
    def __init__(self, content):
        self.content = content

    def show(self):
        return f"Displaying ebook content: {self.content}"

class EbookAdapter:
    def __init__(self, ebook):
        self.ebook = ebook

    def read(self):
        return self.ebook.show()

# Использование
book = Book("A great story")
ebook = Ebook("An amazing digital story")

ebook_adapter = EbookAdapter(ebook)

print(book.read())
print(ebook_adapter.read())