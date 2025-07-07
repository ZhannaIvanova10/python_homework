import logging
import os
from typing import Any


# Создаем папку logs, если ее нет
if not os.path.exists("logs"):
    os.makedirs("logs")

# Создаем логер для модуля utils
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

# Настраиваем обработчик для записи в файл
file_handler = logging.FileHandler(
    "logs/utils.log",
    mode="w",
    encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)

# Настраиваем форматтер
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логеру
utils_logger.addHandler(file_handler)


def example_utils_function(param: Any) -> Any:
    try:
        utils_logger.debug(
            "Функция example_utils_function вызвана с параметром: %s",
            param
        )
        result = param * 2
        utils_logger.info(
            "Функция example_utils_function выполнена успешно. Результат: %s",
            result
        )
        return result
    except Exception as e:
        utils_logger.error(
            "Ошибка в функции example_utils_function: %s",
            str(e)
        )
        raise
