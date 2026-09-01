def withdrawal(amount):
    fee =  5 if amount <= 1000 else 15 if amount >= 1000 else 15
    return fee

def main():
    try:
        amount = int(input("Enter withdrawal amount: ").strip())
        total = amount + withdrawal(amount)
        print(f'Withdrawal: R{amount}')
        print(f'Fee: {withdrawal(amount)}')
        print(f'Total deducted R{total}')
        
    except ValueError:
        print("Invalid input.")
        return

if __name__ == '__main__':
    main()
