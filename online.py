import re, requests
from bs4 import BeautifulSoup
from Libs.pycolors2 import PyColors

colors = PyColors() # Создаем экземпляр класса PyColors

def onlineParser(url):

    response = requests.get(url)

    if response.status_code == 200:
        print("Ответ 200!")

        source = response.text
        print("source: ", source)

        # Дальнейшая обработка содержимого страницы

        if source is not None:
            sirus_site = BeautifulSoup(source, "lxml")
            ###########################################

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
            
            # Уровень экипировки
            user_itemLevel = sirus_site.find("div", class_="col pl-2 py-2 my-auto")
            if user_itemLevel:
                text = user_itemLevel.get_text()
                numbers = re.findall(r'\d+', text)  # Находим все цифры в тексте
                user_itemLevel = numbers[0]
            colors.mass_print("user_itemLevel", user_itemLevel)

            # Уровень персонажа
            user_level = sirus_site.find("div", class_="col pl-2 py-2 my-auto")
            if user_level:
                text = user_level.get_text()
                numbers = re.findall(r'\d+', text)  # Находим все цифры в тексте
                user_level = numbers[1]
            colors.mass_print("user_level", user_level)

            # Расса
            user_race = sirus_site.find("div", class_="col pl-2 py-2 my-auto")
            if user_race:
                user_race = user_race.find_all("span", class_="mr-1")
                if len(user_race) >= 4:
                    user_race = user_race[1].get_text()
            colors.mass_print("user_race", user_race)

            # Спек
            user_spec = sirus_site.find("div", class_="col pl-2 py-2 my-auto")
            if user_spec:
                user_spec = user_spec.find_all("span", class_="mr-1")
                if len(user_spec) >= 4:
                    user_spec = user_spec[2].get_text()
            colors.mass_print("user_spec", user_spec)

            # Класс
            user_class = sirus_site.find("div", class_="col pl-2 py-2 my-auto")
            if user_class:
                user_class = user_class.find_all("span", class_="mr-1")
                if len(user_class) >= 4:
                    user_class = user_class[3].get_text()
            colors.mass_print("user_class", user_class)

            # Реалм - Sirus x5
            user_realm = sirus_site.find("div", class_="col pl-2 py-2 my-auto")
            if user_realm:
                user_realm = user_realm.find("span", class_="mr-2")
                if user_realm:
                    user_realm = user_realm.get_text()
            colors.mass_print("user_realm", user_realm)

            # Очков достижений
            user_achievmentPoints = sirus_site.find("div", class_="ml-2 character-achievement--points")
            if user_achievmentPoints:
                achievement_points_text = user_achievmentPoints.get_text().strip()
                user_achievmentPoints = ''.join(filter(str.isdigit,  achievement_points_text))
            colors.mass_print("user_achievmentPoints", user_achievmentPoints)

            # Последние действия
            last10actions = sirus_site.select("div.card-body.card-datatable ul.list-group li.list-group-item")

            for index, action in enumerate(last10actions, start=1):
                achievement_text = action.get_text().strip().replace('\n', ' ').replace('  ', '')
                achievement_text = achievement_text.replace('над', 'над ').replace('потратив', ' потратив')
                # print(f"Ачивка {index} - {achievement_text}")
                colors.mass_print("achievement_text "+str(index), achievement_text)

            # TODO: что ещё ?
        
    else:
        return None
        print("Ошибка при получении страницы:", response.status_code)

# online
if __name__ == "__main__":
    url = input("Введите URL: ") # https://sirus.su/base/character/57/9202/
    onlineParser(url)
