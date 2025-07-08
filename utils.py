"""Модуль утилит для работы с банковскими данными.

Содержит вспомогательные функции для форматирования данных.
"""
import logging
from pathlib import Path
from datetime import datetime


def setup_file_handler(log_file: str) -> logging.FileHandler:
    """Создает и настраивает файловый обработчик для логов."""
    Path("logs").mkdir(exist_ok=True)
    handler = logging.FileHandler(f"logs/{log_file}", mode="w")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)
    return handler


utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)
utils_logger.addHandler(setup_file_handler("utils.log"))


def example_utils_function(param: int) -> int:
    """Пример функции модуля utils для тестирования."""
    try:
        utils_logger.debug(
            "Вызов example_utils_function с параметром: %d",
            param)
        result = param * 2
        utils_logger.info(
            "Функция выполнена успешно. Результат: %d",
            result)
        return result
    except Exception as e:
        utils_logger.error(
            "Ошибка в example_utils_function: %s",
            str(e))
        raise


def format_account_number(account_number: str) -> str:
    """Форматирование номера счета."""
    try:
        utils_logger.debug(
            "Начало форматирования номера счета: %s",
            account_number)
        if not account_number.isdigit() or len(account_number) != 20:
            raise ValueError("Номер счета должен содержать 20 цифр")

        formatted = f"Счет **{account_number[-4:]}"
        utils_logger.info(
            "Номер счета успешно отформатирован: %s",
            formatted)
        return formatted
    except Exception as e:
        utils_logger.error(
            "Ошибка при форматировании номера счета: %s",
            str(e))
        raise


def get_current_datetime() -> str:
    """Получение текущей даты и времени."""
    try:
        utils_logger.debug("Получение текущей даты и времени")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        utils_logger.info(
            "Текущая дата и время: %s",
            now)
        return now
    except Exception as e:
        utils_logger.error(
            "Ошибка при получении даты и времени: %s",
            str(e))
        raise
