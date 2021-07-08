
#* Data mining Script
from bs4 import BeautifulSoup
class mining:
    def __init__(self, page_source):
        self.soup = BeautifulSoup(page_source, "html.parser")
    
    def FindAll(self):
        return self.soup.find_all(
        "div", 
        {"class": "newtddata col-lg-5 col-md-5 col-xs-12 col-sm-5"}
        )
        
    def warning (self):
        return self.soup.find("div", {"class": "alert alert-danger"})

    def security(self):
        return self.soup.find(id ="imgCaptcha")