import json

def load_stock_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def display_home_menu(stock_data):
    try:
        print("Select a stock exchange:")
        index = 1  
        for exchange in stock_data:
            print(str(index) + ". " + exchange['stockExchange'])
            index += 1  

        choice = int(input("Enter your choice (number): "))
        if 0 < choice <= len(stock_data):
            display_stock_menu(stock_data[choice - 1])
        else:
            print("Invalid choice. Please try again.")
            display_home_menu(stock_data)
    except KeyboardInterrupt:
        print("\nProgram exited by user.")
        return

def display_stock_menu(exchange):
    try:
        print("Top stocks for " + exchange['stockExchange'] + ":")
        index = 1  
        for stock in exchange['topStocks']:
            print(str(index) + ". " + stock['stockName'])
            index += 1  

        print(str(len(exchange['topStocks']) + 1) + ". Go back to Home Menu")
        choice = int(input("Enter your choice (number): "))
        if choice == len(exchange['topStocks']) + 1:
            display_home_menu(data)
        elif 0 < choice <= len(exchange['topStocks']):
            stock = exchange['topStocks'][choice - 1]
            print("Current price of " + stock['stockName'] + ": " + str(stock['price']))
            display_stock_menu(exchange)
        else:
            print("Invalid choice. Please try again.")
            display_stock_menu(exchange)
    except KeyboardInterrupt:
        print("\nProgram exited by user.")
        return

data = load_stock_data("Chatbot - stock data.json")
display_home_menu(data)

