"""Модуль для работы с масками данных.

Содержит функции для обработки и маскирования конфиденциальной информации.
"""
import logging
from typing import Any
from utils import setup_file_handler

# Создаем логер для модуля masks
masks_logger = logging.getLogger("masks")
file_handler = setup_file_handler()

# Добавляем обработчик к логеру
masks_logger.addHandler(file_handler)

def example_masks_function(param: Any) -> Any:
    """Обрабатывает данные, применяя необходимые маски.

    Args:
        param: Входные данные для обработки

    Returns:
        Обработанные данные с масками
    """
    try:
        masks_logger.debug(
            "Функция example_masks_function вызвана с параметром: %s",
            param
        )
        result = str(param) + "_masked"
        masks_logger.info(
            "Функция example_masks_function выполнена успешно. Результат: %s",
            result
        )
        return result
    except Exception as e:
        masks_logger.error(
            "Ошибка в функции example_masks_function: %s",
            str(e)
        )
        raise
