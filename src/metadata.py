"""Metadata for FastAPI application."""

TITLE = "Tastehub API"
DESCRIPTION = """
🍽️ Tastehub - REST API для управления заказами еды в ресторане

Сервис позволяет:
* **Управлять меню** - добавлять, просматривать и удалять блюда
* **Создавать заказы** - оформлять заказы с выбранными блюдами
* **Отслеживать статусы** - следить за процессом приготовления и доставки
* **Отменять заказы** - отменять заказы в статусе "в обработке"
"""
VERSION = "1.0.0"

TAGS_METADATA = [
    {
        "name": "dishes",
        "description": "Операции с блюдами меню",
    },
    {
        "name": "orders",
        "description": "Операции с заказами",
    },
]
