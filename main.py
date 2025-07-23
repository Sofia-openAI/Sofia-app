import os
import requests

UPDATE_URL = "https://example.com/latest_version/main.py"

def check_for_updates():
    try:
        r = requests.get(UPDATE_URL)
        if r.status_code == 200:
            with open("main.py", "wb") as f:
                f.write(r.content)
            print("🔄 Обновление получено. Перезапуск...")
            os.execv(_file_, ['python'] + sys.argv)
    except Exception as e:
        print(f"Ошибка при обновлении: {e}")

check_for_updates()
def main():
    print("Привет, шеф!")
    input("Нажмите Enter для выхода...")

if __name__ == "__main__":
    main()
