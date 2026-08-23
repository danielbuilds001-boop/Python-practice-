class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{self.title} ~ {self.author}"
        
def main():
    b1 = Book("Atomic habits","James clear")
    print(b1)
if __name__ == '__main__':
    main()
