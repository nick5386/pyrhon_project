"""A collection of test function for my project."""

from functions import base_premium_price, calc_discount, calc_additional_premium, calc_options_cost

def test_base_premium_price():
    assert callable(base_premium_price)
    assert isinstance(base_premium_price(1500), int)
    assert base_premium_price(1500) == 1000
    assert base_premium_price(3000) == 1500
    assert base_premium_price(4500) == 2000
    
def test_calc_discount():
    assert callable(calc_discount)
    assert isinstance(calc_discount(65, 'no', 1000), float)
    assert calc_discount(65, 'no', 1000) == 90.0
    assert calc_discount(25, 'yes', 1500) == 75.0
    assert calc_discount(30, 'no', 2000) == 0
    
def test_calc_additional_premium():
    assert callable(calc_additional_premium)
    assert isinstance(calc_additional_premium(5, 'yes', 1000), float)
    assert calc_additional_premium(5, 'yes', 1000) == 30.0
    assert calc_additional_premium(4, 'yes', 2000) == 40.0
    assert calc_additional_premium(5, 'no', 2000) == 20.0
    assert calc_additional_premium(4, 'no', 1500) == 0
    
def test_calc_options_cost():
    assert callable(calc_options_cost)
    assert isinstance(calc_options_cost('hurricane', 1000), float)
    assert calc_options_cost('hurricane', 1000) == 30.0
    assert calc_options_cost('hurricane, flood', 1500) == 75.0 
    assert calc_options_cost('hurricane, flood, earthquake', 1000) == 90.0
    
def run_all_tests():
    test_base_premium_price()
    test_calc_discount()
    test_calc_additional_premium()
    test_calc_options_cost()    
                 
run_all_tests()     