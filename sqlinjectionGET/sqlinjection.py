import requests
target = input("SQL injection (GET) zafiyeti bulunan URL'yi giriniz: ")
payload = input("Denemek istediğiniz SQL injection payload'unu giriniz: ")

try:
    response = requests.get(f"{target}?name={payload}")

    if ("admin" in response.content.decode('utf-8') or
        "root" in response.content.decode('utf-8') or
        "syntax" in response.content.decode('utf-8') or
        "error" in response.content.decode('utf-8') or
        "ORDER BY" in response.content.decode('utf-8')):
        print("Zafiyet bulundu. SQL Injection başarılı!")
    else:
        print("Zafiyet bulunamadı.")
except Exception as e:
    print(f"Hata: {e}")
