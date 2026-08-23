class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"{self.name} - R{self.price}"
        
def main():
    p1 = Product("Laptop",5999)
    p2 = Product("Phone",3499)
    p3 = Product("Headphones",899)
    print(p1)
    print(p2)
    print(p3)
    
if __name__ == '__main__':
    main()
