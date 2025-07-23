import os
import requests
import subprocess
import sys

UPDATE_URL = "https://raw.githubusercontent.com/Sofia-openAI/Sofia-app/main/main.py"

def check_for_updates():
    try:
        r = requests.get(UPDATE_URL)
        if r.status_code == 200:
            with open("main.py", "wb") as f:
                f.write(r.content)
            print("✅ Обновление получено. Перезапуск...")
            subprocess.Popen([sys.executable])
            sys.exit()
    except Exception as e:
        print(f"Ошибка при обновлении: {e}")

def main():
    print("Привет, шеф!")
    input("Нажмите Enter для выхода...")

check_for_updates()
main()
