from utils import format_account_number, get_current_datetime
from masks import mask_card_number, mask_account_number


def main():
    """Основная функция для демонстрации работы модулей."""
    print("=== Демонстрация работы модулей ===")

    print("\n[Модуль utils]")
    current_time = get_current_datetime()
    print("Текущая дата и время:", current_time)

    formatted_account = format_account_number("12345678901234567890")
    print("Форматированный счет:", formatted_account)

    print("\n[Модуль masks]")
    masked_card = mask_card_number("1234567890123456")
    print("Замаскированная карта:", masked_card)

    masked_account = mask_account_number("12345678901234567890")
    print("Замаскированный счет:", masked_account)


if __name__ == "__main__":
    main()
