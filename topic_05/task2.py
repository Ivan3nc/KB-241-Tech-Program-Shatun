import requests

def get_exchange_rate(currency_code):
    """Отримує курс валют з API НБУ"""
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Шукаємо потрібну валюту у списку
        for item in data:
            if item['cc'] == currency_code:
                return item['rate']
        return None
    except Exception as e:
        print(f"Помилка з'єднання: {e}")
        return None

def main():
    print("--- Конвертер валют (NBU API) ---")
    available_currencies = ["USD", "EUR", "PLN"]
    
    # 1. Введення типу валюти
    currency = input(f"Введіть валюту {available_currencies}: ").upper()
    
    if currency not in available_currencies:
        print("Ця валюта не підтримується або введена неправильно.")
        return

    # 2. Введення суми
    try:
        amount = float(input("Введіть суму валюти: "))
    except ValueError:
        print("Сума має бути числом.")
        return

    # 3. Отримання курсу
    rate = get_exchange_rate(currency)
    
    if rate:
        # 4. Конвертація
        uah_result = amount * rate
        print(f"Курс {currency}: {rate}")
        print(f"Результат: {amount} {currency} = {round(uah_result, 2)} UAH")
    else:
        print("Не вдалося отримати курс валют.")

if __name__ == "__main__":
    main()