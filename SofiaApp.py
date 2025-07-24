import os
import sys
import requests
import subprocess

UPDATE_URL = "https://raw.githubusercontent.com/Sofia-openAI/Sofia-app/main/SofiaApp.py"
LOCAL_FILE = "SofiaApp.py"

def download_update():
    try:
        r = requests.get(UPDATE_URL)
        if r.status_code == 200:
            with open(LOCAL_FILE, "wb") as f:
                f.write(r.content)
            with open("sofia_log.txt", "a", encoding="utf-8") as log:
                log.write("✅ Обновление получено и сохранено.\n")
        else:
            raise Exception(f"Статус обновления: {r.status_code}")
    except Exception as e:
        with open("sofia_log.txt", "a", encoding="utf-8") as log:
            log.write(f"❌ Ошибка при обновлении: {e}\n")

def main():
    if "--updated" not in sys.argv:
        download_update()
        subprocess.run(["python", LOCAL_FILE, "--updated"])
        return
    print("✅ София обновлена и активна. Шеф, я на связи.")
    input("Нажмите Enter для выхода...")

if _name_ == "_main_":
    main()
