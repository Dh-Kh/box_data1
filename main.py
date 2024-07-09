from dotenv import load_dotenv
from typing import Dict, Any
import requests
import os
import openpyxl

load_dotenv()

API_URL = os.getenv("API_URL")

class Countries(object):
    
    def __init__(self, initial_url: str):
        self.initial_url = initial_url

    def _retrieve_data(self) -> Dict[str, Any]:
        r = requests.get(self.initial_url)
        return r.json()
    
    def get_data(self) -> None:
        
        workbook = openpyxl.Workbook()
        
        sheet = workbook.active 
        
        sheet.append(["name", "capital", "flag"])
        
        country_data = self._retrieve_data()
        
        for country in country_data:
            name = country.get("name", {}).get("common")
            capital = country.get("capital")
            if isinstance(capital, list) and len(capital) > 0:
                capital = capital[0]
            else:
                capital = "No data"
            flag = country.get("flags", {}).get("png")
            sheet.append([name, capital, flag])
        
        workbook.save("data.xlsx")
    
if __name__ == "__main__":
    c = Countries(API_URL)
    print("Executing...")
    c.get_data()
    print("Microsoft Excel data has been loaded!")