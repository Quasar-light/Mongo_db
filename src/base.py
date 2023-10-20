import requests
import pandas as pd

class Base:
    """ class that handles all connections tot he API object and returns a DataFrame form its initalization
    
    class has the following methods:
    
    return_url: returns the api_url we are currently working with
    get_data: scrapes the data from the API and creates a dataframea from it!
    
    """
    
    def __int__(self, url = 'https://api.scryfall.com/bulk-data'):
        self.__api_url = url
        self.get_data()
        
    def get_data(self):
        """scrapes data from the api and gets data from it"""
        self.df = pd.DataFrame.from_dict(requests.get(requests.get(self.__api_url).json()['data'][0]['download_url']).json())
        return self.df

if __name__ == '__main__':
    c = Base()
    print(c.df)
        
#to get into virtual enviroment 
#cd venv
#source venv/bin/activate
#Pip3 install requests pandas
        