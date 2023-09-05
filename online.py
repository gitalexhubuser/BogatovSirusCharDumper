import requests

# online
# https://sirus.su/base/character/57/9202/
url = input("Введите URL: ")
response = requests.get(url)

if response.status_code == 200:
    source = response.text
    # Дальнейшая обработка содержимого страницы
else:
    print("Ошибка при получении страницы:", response.status_code)
