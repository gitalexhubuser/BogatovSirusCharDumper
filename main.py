from bs4 import BeautifulSoup
from Libs.pycolors2 import PyColors

colors = PyColors() # Создаем экземпляр класса PyColors

def offlineParser(filePath):
    with open(filePath, encoding="utf8", errors='ignore') as file:
        source = file.read()
    # print(f"source: {colors.YELLOW}{source}{colors.ENDC}")

    soup = BeautifulSoup(source, "lxml")

    title = soup.title.string
    title1 = soup.title.text
    # print(f"title: {colors.YELLOW}{title}{colors.ENDC}")
    # colors.yellow_print(title)

    colors.yellow_print("title", title)
    colors.mass_print("title", title, title1)

    # .find() .find_all()


# offline
if __name__ == "__main__":
    offlineParser("./_Target/index.html")
