import pytest
from operations import format_date

def test_format_date():
    # Тестирование для корректных дат
    assert format_date("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert format_date("2019-07-03T18:35:29.512364") == "03.07.2019"
    assert format_date("2018-06-30T02:08:58.425572") == "30.06.2018"

    # Тестирование для некорректных дат
    assert format_date("invalid_date") == "invalid_date"
    assert format_date("") == ""

    # Тестирование для дат без времени (без дробной части секунды)
    assert format_date("2022-12-31T23:59:59") == "31.12.2022"
