from utils import format_account_number, get_current_datetime
from masks import mask_card_number, mask_account_number


def main():
    """Основная функция для демонстрации работы модулей."""
    print("=== Демонстрация работы модулей ===")

    # Демонстрация utils
    print("\n[Модуль utils]")
    print("Текущая дата и время:", get_current_datetime())
    print("Форматированный счет:", format_account_number("12345678901234567890"))

    # Демонстрация masks
    print("\n[Модуль masks]")
    print("Замаскированная карта:", mask_card_number("1234567890123456"))
    print("Замаскированный счет:", mask_account_number("12345678901234567890"))


if __name__ == "__main__":
    main()
