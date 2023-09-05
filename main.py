from bs4 import BeautifulSoup
from Libs.pycolors2 import PyColors

colors = PyColors() # Создаем экземпляр класса pycolors

# offline
with open("./_Target/index.html", encoding="utf8", errors='ignore') as file:
    source = file.read()
# print(f"source: {colors.YELLOW}{source}{colors.ENDC}")

soup = BeautifulSoup(source, "lxml")

title = soup.title.text
# print(f"title: {colors.YELLOW}{title}{colors.ENDC}")
# colors.yellow_print(title)

colors.yellow_print("title", title)