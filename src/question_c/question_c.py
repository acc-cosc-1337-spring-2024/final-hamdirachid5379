#write functions here, don't add input('') statements here!



class Stock:
      
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    
    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
class MSFT:

    # Create a Stock object
    stock = Stock("MSFT", "Microsoft")
    
    # Display symbol and company name
    print("Symbol:", stock.get_symbol())
    print("Company Name:", stock.get_company_name())




 