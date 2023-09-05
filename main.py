from bs4 import BeautifulSoup
from Libs.pycolors2 import PyColors

colors = PyColors() # Создаем экземпляр класса PyColors

def offlineParser(filePath):
    with open(filePath, encoding="utf8", errors='ignore') as file:
        source = file.read()
    # print(f"source: {colors.YELLOW}{source}{colors.ENDC}")

    sirus_site = BeautifulSoup(source, "lxml")

    # 1. Заголовок
    title = sirus_site.title.string
    title1 = sirus_site.title.text
    # print(f"title: {colors.YELLOW}{title}{colors.ENDC}")
    # colors.yellow_print(title)

    colors.yellow_print("title", title)
    colors.mass_print("title", title, title1)
    
    # 2. h1
    # .find() .find_all()
    page_h1 = sirus_site.find("h1") # Первый попавшийся
    page_h2 = sirus_site.find_all("li") # Все 
    colors.mass_print("page_h1", page_h1)
    colors.mass_print("page_h2", page_h2)


# offline
if __name__ == "__main__":
    offlineParser("./_Target/index.html")
