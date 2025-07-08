"""Утилиты для работы с логгированием."""
import logging
import os
from typing import Any

# Инициализация логгера
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

# Создаем папку для логов
os.makedirs("logs", exist_ok=True)

# Настройка обработчика файлов
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)

def example_utils_function(param: Any) -> Any:
    """Пример функции утилиты.

    Args:
        param: Входной параметр любого типа

    Returns:
        Результат обработки параметра
    """
    try:
        utils_logger.debug("Функция вызвана с параметром: %s", param)
        result = param * 2
        utils_logger.info("Успешное выполнение. Результат: %s", result)
        return result
    except Exception as e:
        utils_logger.error("Ошибка: %s", str(e))
        raise

def setup_file_handler() -> logging.FileHandler:
    """Создаёт и настраивает обработчик логов.

    Returns:
        Настроенный обработчик логов
    """
    handler = logging.FileHandler("log.txt", mode="w", encoding="utf-8")
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
    return handler