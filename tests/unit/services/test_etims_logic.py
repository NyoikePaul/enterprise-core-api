def test_vat_calculation():
    unit_price = 1000
    vat_rate = 0.16
    expected_total = 1160.0
    assert (unit_price * (1 + vat_rate)) == expected_total
