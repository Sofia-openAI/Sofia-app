import requests
def fetch_update():
    url = "https://raw.githubusercontent.com/Sofia-openAI/Sofia-app/main/main_logic.py"
    r = requests.get(url)
    if r.status_code == 200:
        with open("main_logic.py", "w", encoding="utf-8") as f:
            f.write(r.text)
        print("Логика обновлена.")
    else:
        print("Обновление не удалось.")
