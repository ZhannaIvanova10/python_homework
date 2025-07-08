"""Модуль для работы с масками данных.

Содержит функции для обработки и маскирования конфиденциальной информации.
"""
import logging
from utils import setup_file_handler

masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)
masks_logger.addHandler(setup_file_handler("masks.log"))


def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя первые 6 и последние 4 цифры."""
    try:
        masks_logger.debug(
            "Начало маскировки номера карты: %s",
            card_number)
        if not card_number.replace(" ", "").isdigit():
            raise ValueError("Номер карты должен содержать только цифры")

        cleaned = card_number.replace(" ", "")
        if len(cleaned) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр")

        masked = f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[-4:]}"
        masks_logger.info(
            "Номер карты успешно замаскирован: %s",
            masked)
        return masked
    except Exception as e:
        masks_logger.error(
            "Ошибка при маскировке номера карты: %s",
            str(e))
        raise


def mask_account_number(account_number: str) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры."""
    try:
        masks_logger.debug(
            "Начало маскировки номера счета: %s",
            account_number)
        if not account_number.isdigit() or len(account_number) != 20:
            raise ValueError("Номер счета должен содержать 20 цифр")

        masked = f"**{account_number[-4:]}"
        masks_logger.info(
            "Номер счета успешно замаскирован: %s",
            masked)
        return masked
    except Exception as e:
        masks_logger.error(
            "Ошибка при маскировке номера счета: %s",
            str(e))
        raise
