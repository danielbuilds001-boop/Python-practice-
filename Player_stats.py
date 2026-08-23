class Player:
    def __init__(self,name,health,level):
        self.name = name
        self.health = health
        self.level = level
        
    def __str__(self):
        return f"{self.name} | hp: {self.health} | {self.level}"
        
def main():
    p1 = Player("Daniel","100","Level: 3")
    print(p1)
    
if __name__ == '__main__':
    main()
