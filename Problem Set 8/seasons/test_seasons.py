from seasons import convert_age_to_minutes

def test_convert_age_to_minutes():
    assert convert_age_to_minutes(2020, 4, 12) == "One million, eight hundred ninety-seven thousand, nine hundred twenty minutes"
    assert convert_age_to_minutes(1993, 1, 6) == "Sixteen million, two hundred thirty-seven thousand, four hundred forty minutes"

