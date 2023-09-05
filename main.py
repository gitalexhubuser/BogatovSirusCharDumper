from bs4 import BeautifulSoup
import requests
from Libs.pycolors import pycolors

colors = pycolors() # Создаем экземпляр класса pycolors

# online
# https://sirus.su/base/character/57/9202/

# offline
with open("./_Target/index.html", encoding="utf8", errors='ignore') as file:
    source = file.read()
    print(f"source: {colors.YELLOW}{source}{colors.ENDC}")

# soup = BeautifulSoup(source, "lxml")
