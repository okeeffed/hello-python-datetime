from datetime import date, datetime, timedelta


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


print(is_date_before_today("2019-01-01"))
print(is_date_before_today("2022-01-01"))
print(is_date_before_today("2021-08-03"))
print(is_date_before_today("2021-08-04"))

now = datetime.now()
now_str = now.strftime('%Y-%m-%d')
print(now_str)
print(is_date_before_today(now_str))

now_subtract_one_day = now - timedelta(days=2)

now_subtract_one_day_str = now_subtract_one_day.strftime('%Y-%m-%d')
print(now_subtract_one_day_str)
print(is_date_before_today(now_subtract_one_day_str))

now_add_one_day = now + timedelta(days=1)

now_add_one_day_str = now_add_one_day.strftime('%Y-%m-%d')
print(now_add_one_day_str)
print(is_date_before_today(now_add_one_day_str))
