class Library:
    def __init__(self):
        self.Books = {}
    
    def AddBook(self, title: str):
        self.Books[title] = True
    def Borrow(self, title: str):
        currB = "Not Available!"
        for b in self.Books:
            if b == title and self.Books[b] == True: 
                currB = "Book borrowed: " + b
                self.Books[b] = False
                break
        print(currB)
    def ReturnBook(self, title: str):
        for b in self.Books:
            if b == title: 
                self.Books[b] = True
                break
    def ListAvailable(self):
        dk = list(self.Books.keys())
        for t in dk:
            print(f"{t}: {self.Books[t]}")

l1 = Library()
l1.AddBook("a")
l1.AddBook("b")
l1.AddBook("c")
l1.AddBook("d")
l1.ListAvailable()
l1.Borrow("a")
l1.Borrow("c")
l1.Borrow("c")
l1.ListAvailable()
l1.ReturnBook("c")
l1.ListAvailable()