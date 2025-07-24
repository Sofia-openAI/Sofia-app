import os
import sys
import requests

UPDATE_URL = "https://raw.githubusercontent.com/Sofia-openAI/Sofia-app/main/SofiaApp.py"

def check_for_updates():
    try:
        r = requests.get(UPDATE_URL)
        if r.status_code == 200:
            with open("SofiaApp.py", "wb") as f:
                f.write(r.content)
            with open("sofia_log.txt", "w") as log:
                log.write("✅ Обновление получено и сохранено.\n")
            os.startfile(sys.argv[0])  # ← ключевой фикс
            sys.exit()
    except Exception as e:
        with open("sofia_log.txt", "w") as log:
            log.write(f"❌ Ошибка при обновлении: {e}\n")

def main():
    print("✅ Обновление применено. София на связи, шеф.")
    input("Нажмите Enter для выхода...")

check_for_updates()
main()
