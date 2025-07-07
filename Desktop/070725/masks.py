import logging
from typing import Any


# Создаем логер для модуля masks
masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)

# Настраиваем обработчик для записи в файл
file_handler = logging.FileHandler(
    "logs/masks.log",
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
masks_logger.addHandler(file_handler)


def example_masks_function(param: Any) -> Any:
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
