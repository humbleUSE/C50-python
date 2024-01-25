from working import convert
import pytest


def test_convert_valid_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("11:00 AM to 12:00 PM") == "11:00 to 12:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:00 PM to 8:00 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("12:30 PM to 12:00 AM") == "12:30 to 00:00"


def test_convert_invalid_time():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("19:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM  17:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM : 17:00 PM")
