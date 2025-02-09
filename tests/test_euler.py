import pytest
from euler_prime import (
    is_prime,
    digits_to_number,
    number_to_digits,
    find_prime_in_window,
    generate_e_digits,
    find_first_prime_in_e
)

def test_is_prime():
    """Test prime number checking functionality"""
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(7427466391)  # Our expected result
    assert not is_prime(7427466392)

def test_digits_to_number():
    """Test conversion from digits to number"""
    assert digits_to_number([1, 2, 3]) == 123
    assert digits_to_number([0, 0, 1]) == 1
    assert digits_to_number([7, 4, 2, 7, 4, 6, 6, 3, 9, 1]) == 7427466391

def test_number_to_digits():
    """Test conversion from number to digits"""
    assert number_to_digits(123) == [1, 2, 3]
    assert number_to_digits(7427466391) == [7, 4, 2, 7, 4, 6, 6, 3, 9, 1]

def test_find_prime_in_window():
    """Test finding prime in a window of digits"""
    digits = [1, 2, 3, 4, 5, 6, 7]
    assert find_prime_in_window(digits, 3) == 167  # 167 is prime
    
    # Test with known e digits
    e_digits = [7, 4, 2, 7, 4, 6, 6, 3, 9, 1]
    assert find_prime_in_window(e_digits, 10) == 7427466391

def test_generate_e_digits():
    """Test generating digits of e"""
    # First few digits of e after decimal: 7182818284...
    e_digits = generate_e_digits(10)
    assert e_digits[:10] == [7, 1, 8, 2, 8, 1, 8, 2, 8, 4]

def test_find_first_prime_in_e():
    """Test finding first prime in e"""
    result = find_first_prime_in_e(10)
    assert result == 7427466391

def test_performance():
    """Test that the solution runs within reasonable time"""
    import time
    start = time.time()
    find_first_prime_in_e(10)
    end = time.time()
    assert end - start < 1  # Should complete within 1 second
