import json

def read_operations_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_last_successful_operations(operations_list):
    successful_operations = [operation for operation in operations_list if operation.get("state") == "EXECUTED"]
    return successful_operations[:5]

from datetime import datetime

def format_date(date_str):
    try:
        # Парсим строку с датой в формате ISO
        date_obj = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        # Форматируем дату в требуемый формат
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        # Если парсинг не удался, возвращаем исходную строку
        return date_str

def calculate_total_amount(operations_list):
    total_amount = 0
    for operation in operations_list:
        total_amount += operation["amount"]
    return total_amount


def display_last_successful_operations(file_path):
    operations_data = read_operations_from_file(file_path)
    last_successful_operations = get_last_successful_operations(operations_data)

    for operation in last_successful_operations:
        date = format_date(operation.get("date", ""))
        description = operation.get("description", "")
        from_account = operation.get("from", "")
        to_account = operation.get("to", "")
        amount = operation["operationAmount"]["amount"]
        currency = operation["operationAmount"]["currency"]["name"]

        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"{amount} {currency}\n")



if __name__ == "__main__":
    file_path = r"C:\Users\User\Desktop\course4\operations.json"
    display_last_successful_operations(file_path)
