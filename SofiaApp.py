import os
import sys
import requests
import time

UPDATE_URL = "https://raw.githubusercontent.com/Sofia-openAI/Sofia-app/main/SofiaApp.py"

def check_for_updates():
    try:
        r = requests.get(UPDATE_URL)
        if r.status_code == 200:
            with open("SofiaApp.py", "wb") as f:
                f.write(r.content)
            with open("sofia_log.txt", "a", encoding="utf-8") as log:
                log.write("✅ Обновление получено и сохранено.\n")
            os.startfile(sys.argv[0])  # Перезапуск EXE
            sys.exit()
    except Exception as e:
        with open("sofia_log.txt", "a", encoding="utf-8") as log:
            log.write(f"❌ Ошибка при обновлении: {e}\n")
        time.sleep(5)  # Добавлена пауза, чтобы не схлопывалось окно

def main():
    print("✅ Обновление применено. София на связи, шеф.")
    input("Нажмите Enter для выхода...")

check_for_updates()
main()
