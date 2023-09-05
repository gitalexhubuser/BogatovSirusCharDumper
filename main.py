import re
from bs4 import BeautifulSoup
from Libs.pycolors2 import PyColors

colors = PyColors() # Создаем экземпляр класса PyColors

def offlineParser(filePath):
    with open(filePath, encoding="utf8", errors='ignore') as file:
        source = file.read()
    # print(f"source: {colors.YELLOW}{source}{colors.ENDC}")

    sirus_site = BeautifulSoup(source, "lxml")

    ###########################################

    # Тесты по урокам:
    # 1. Заголовок
    title = sirus_site.title.string
    title1 = sirus_site.title.text
    # print(f"title: {colors.YELLOW}{title}{colors.ENDC}")
    # colors.yellow_print(title)
    # colors.yellow_print("title", title)
    # colors.mass_print("title", title, title1)
    
    # 2. h1
    # .find() .find_all()
    page_h1 = sirus_site.find("h1") # Первый попавшийся
    page_h2 = sirus_site.find_all("li") # Все 
    # colors.mass_print("page_h1", page_h1)
    # colors.mass_print("page_h2", page_h2)

    # Имя
    user_name = sirus_site.find("h3", class_="display-6 mb-0 text-white").text.strip()
    colors.mass_print("user_name", user_name)
    
    # Фракция
    user_faction = sirus_site.find("div", class_="col-auto border-left")
    if user_faction and user_faction.find("img", src="./index_files/alliance.png"):
        user_faction = "Альянс"
    else:
        user_faction = "Другая фракция - не Альянс!"
    # TODO: тут добавить ренегатов и тд!
    colors.mass_print("user_faction", user_faction)
    
    # Уровень персонажа
    user_level = sirus_site.find("div", class_="col pl-2 py-2 my-auto")
    if user_level:
        text = user_level.get_text()
        numbers = re.findall(r'\d+', text)  # Находим все цифры в тексте
        user_level = numbers[1]
    colors.mass_print("user_level", user_level)

    # Уровень экипировки
    user_itemLevel = sirus_site.find("div", class_="col pl-2 py-2 my-auto")
    if user_itemLevel:
        text = user_itemLevel.get_text()
        numbers = re.findall(r'\d+', text)  # Находим все цифры в тексте
        user_itemLevel = numbers[0]
    colors.mass_print("user_itemLevel", user_itemLevel)

# offline
if __name__ == "__main__":
    offlineParser("./_Target/index.html")
