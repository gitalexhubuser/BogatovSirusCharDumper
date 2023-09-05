from bs4 import BeautifulSoup
import requests

# online
# https://sirus.su/base/character/57/9202/

# offline
with open("./_Target/index.html") as file:
    source = file.read()
    print("source: ", source)

# soup = BeautifulSoup(source, "lxml")
