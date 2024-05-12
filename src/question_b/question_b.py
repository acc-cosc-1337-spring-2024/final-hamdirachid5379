#write functions here, don't add input('') statements here!

from ast import main

from question_d.main import create_multiplication_table, display_multiplication_table
 

#def main():

class Stock:
    stocks =  0
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    
    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
    def __str__(self):
     print(str)

    def stock_purchase_history():
       stocks = [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]

    # Add stocks to dictionary
    stock_dict = {stock.get_symbol(): stock.get_company_name() for stock in stocks}

    # Display stock purchase history
    print("Stock Purchase History:")
    print("Symbol\tCompany Name")
    for symbol, company_name in stock_dict.items():
        print(f"{symbol}\t{company_name}")
def main():
    
    while True:
        # Create multiplication table
        table = create_multiplication_table()
        
        # Display multiplication table
        display_multiplication_table(table)
        
        # Ask user if they want to continue
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
