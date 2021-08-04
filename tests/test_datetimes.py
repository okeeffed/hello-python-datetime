import datetime
from freezegun import freeze_time
from src.datetimes import is_date_before_today


def test_freeze_time():
    assert datetime.datetime.now() != datetime.datetime(2012, 1, 14)
    # Mocking the time to be 2012-01-14
    with freeze_time("2012-01-14"):
        assert datetime.datetime.now() == datetime.datetime(2012, 1, 14)
    # Without the mock, the time should be back to normal
    assert datetime.datetime.now() != datetime.datetime(2012, 1, 14)


@freeze_time("2012-01-14")
def test_freeze_time_with_decorator():
    # Testing with a decorator that mocks throughout the test
    assert datetime.datetime.now() == datetime.datetime(2012, 1, 14)

# Converting the output we expected from main.py into a set of tests.
# Mocking time unnecessary, but done for the sake of completion.


@freeze_time("2021-08-04")
def test_is_date_before_today():
    """Should return False"""
    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d')
    assert is_date_before_today(now_str) is False


@freeze_time("2021-08-04")
def test_is_one_day_ago_before_today():
    """Should return True"""
    now_subtract_one_day = datetime.datetime.now() - datetime.timedelta(days=1)
    now_subtract_one_day_str = now_subtract_one_day.strftime('%Y-%m-%d')
    assert is_date_before_today(now_subtract_one_day_str) is True


@freeze_time("2021-08-04")
def test_is_one_day_ahead_before_today():
    """Should return False"""
    now_add_one_day = datetime.datetime.now() + datetime.timedelta(days=1)
    now_add_one_day_str = now_add_one_day.strftime('%Y-%m-%d')
    assert is_date_before_today(now_add_one_day_str) is False
