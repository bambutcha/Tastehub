from enum import Enum


class OrderStatus(str, Enum):
    PROCESSING = "в обработке"
    COOKING = "готовится"
    DELIVERING = "доставляется"
    COMPLETED = "завершен"
    CANCELLED = "отменен"

    @classmethod
    def get_valid_transitions(cls, current_status: str) -> list[str]:
        transitions = {
            cls.PROCESSING: [cls.COOKING, cls.CANCELLED],
            cls.COOKING: [cls.DELIVERING],
            cls.DELIVERING: [cls.COMPLETED],
            cls.COMPLETED: [],
            cls.CANCELLED: [],
        }
        return transitions.get(current_status, [])
    