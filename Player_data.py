player = {}
player_items = {}

def create_player():
    user_name = input("Enter your username: ").strip()
    if user_name == "":
        print("Your name cannot be empty.")
        return
    try:
        starting_health = int(input("Enter your starting health: "))
        
        starting_level = int(input("Enter your starting level: "))
        player[user_name] = {"Profile":{"Health": starting_health,"Level": starting_level}}
        print(player)
    except ValueError:
        print("Invalid input please enter numbers only.")  

player_items = {}

def player_inventory():
    inventory = input("Item name: ").strip().lower()
    try:
        damage = int(input("Damage: "))
    
        player_items[inventory] = {
            "damage": damage
        }
    
        print(player_items)
    except ValueError:
        print("Invalid input please enter numbers only ")
while True:
    player_inventory()
    
