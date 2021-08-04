from datetime import date


def is_date_before_today(date_str: str):
    """Check if date is before today

    Args:
        date_str (str): String of a date to pass

    Returns:
        bool: Value of if date is before today
    """
    try:
        date_obj = date.fromisoformat(date_str)
        return date_obj < date.today()
    except Exception:
        return False
