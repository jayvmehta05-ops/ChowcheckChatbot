orders = [
    {'name': 'Mack Harrison', 'order_code': 1234, 'status': 'In Progress', 'problem': True},
    {'name': 'John Doe', 'order_code': 8932, 'status': 'Complete', 'problem': False},
    {'name': 'Pickle Minstrow', 'order_code': 9045, 'status': 'Not Started', 'problem': True},
    {'name': 'Isrili Mick', 'order_code': 3465, 'status': 'In Progress', 'problem': False},
    {'name': 'Robin Coolidge', 'order_code': 4321, 'status': 'Complete', 'problem': True}
]

def introduction():
    print("Hi there! I'm *Chowcheck*, your delivery assistant bot.")
    print("I help you track or solve problems with your order!\n")

    try:
        intro = int(input("Please enter your order code so I can look it up: "))
    except ValueError:
        print("That doesn't look like a valid order number. Try again!\n")
        return introduction()

    for order in orders:
        if order['order_code'] == intro:
            display_info(order)
            return
    
    print("Hmm, I couldn't find that order code in our system. Please double-check and try again.\n")
    return introduction()

def display_info(order):
    print(f"\n🔍 Checking delivery info for {order['name']} (Order #{order['order_code']})...")
    print("-------------------------------------------------------")

    if order['problem']:
        print("It looks like there's been a delay or issue with your delivery.")
        if order['status'] == 'Complete':
            print("Your order shows as *Complete*, but our system flagged a delivery issue.")
            print("I've notified our support team — they'll contact you soon to resolve it.")
        elif order['status'] == 'In Progress':
            print("Your order is still *In Progress*, and there might be a temporary delay.")
            print("Please hold tight — your package is being reviewed by our logistics team.")
        else:
            print("Your order hasn't been started yet. There might be a system hiccup.")
            print("I've sent an alert to prioritize your order right away.")
    else:
        print("No issues detected with your delivery!")
        if order['status'] == 'Complete':
            print("Your package has been successfully delivered — enjoy your meal!")
        elif order['status'] == 'In Progress':
            print("Your delivery is on its way and should arrive soon.")
        else:
            print("Your order is scheduled to start soon. Thanks for your patience!")

    print("\nTip: If your delivery still doesn't arrive in 24 hours, type 'support' next time to contact a live agent.")
    print("-------------------------------------------------------\n")
    print("Thanks for checking in with Chowcheck!")

def run_bot():
    while True:  
        introduction()
        again = input("\nWould you like to check another order? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThanks for using Chowcheck! Have a great day!")
            break  

run_bot()