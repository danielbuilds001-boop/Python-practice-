def password_check(password):
    return password == "1234"

def main():
    attempts = 0
    
    while attempts < 3:
        password = input("Enter password: ")
        
        if password_check(password):
            print("Access granted")
            return


        print("Access denied")
        attempts += 1
            
    print("Account locked.")

if __name__ == '__main__':
    main()
