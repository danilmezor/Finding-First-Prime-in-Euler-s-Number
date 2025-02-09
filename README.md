# First Prime in Euler's Number 🧮

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## The Billboard Puzzle 🤔

![Google Billboard Puzzle](https://www.hanshq.net/gfx/eprime.jpg)

*The mysterious mathematical billboard that appeared in Silicon Valley*

This project solves old mathematical puzzle that appeared on a billboard in Silicon Valley. The billboard showed a URL in the format:

```
{first 10-digit prime found in consecutive digits of e}.com
```

## The Solution 💡

The answer is `7427466391.com`. Our program finds this number in approximately 0.002 seconds!

### How it Works 🔧

The solution combines several mathematical and computational techniques:

1. **Generating e's Digits**
   - Uses scaled integer arithmetic for perfect precision
   - Implements the series: e = 2 + 1/1! + 1/2! + ...
   - Adds extra precision digits for accuracy

2. **Prime Testing**
   ```python
   def is_prime(number):
       if number < 2: return False
       if number == 2: return True
       if number % 2 == 0: return False
       
       for i in range(3, int(number ** 0.5) + 1, 2):
           if number % i == 0: return False
       return True
   ```

3. **Sliding Window Search**
   - Efficiently searches through consecutive digits
   - Converts digit sequences to numbers
   - Tests each number for primality

## Quick Start 🚀

```bash
# Clone the repository
git clone https://github.com/yourusername/euler-prime.git
cd euler-prime

# Run the main program
python euler_prime.py
```

## Results 📊

```python
First 10-digit prime in e: 7427466391
Time taken: 0.0023488998413085938 seconds
```

## Features ✨

- Pure Python implementation
- No external dependencies
- Fairly fast execution
- Well-covered test suite
- Well-documented code
- Mathematical elegance

## Usage Example 📝

```python
from euler_prime import find_first_prime_in_e

# Find first 10-digit prime in e
result = find_first_prime_in_e(10)
print(f"First 10-digit prime in e: {result}")
```

## Testing 🧪

Run the tests using pytest:

```bash
python -m pytest tests/
```

## Project Structure 📁

```
.
├── README.md
├── euler_prime.py     # Main implementation
├── tests/
│   └── test_euler.py # Test cases
├── requirements.txt   # Project dependencies
└── LICENSE           # MIT License
```

## The Math Behind It 📚

Euler's number (e) is a mathematical constant approximately equal to 2.71828... It can be represented as an infinite series:

```
e = 2 + 1/1! + 1/2! + 1/3! + 1/4! + ...
```

Our implementation uses this series along with scaled integer arithmetic to generate precise digits of e.

## Performance Optimization 🏃‍♂️

The solution employs several optimizations:
- Early termination in primality testing
- Efficient digit extraction
- Smart precision handling
- Sliding window optimization



## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author ✍️

[Danil Zanozin][https://github.com/danilmezor]

## Acknowledgments 🙏

- Google for creating this puzzle
- The mathematical beauty of Euler's number
- The open-source community

---
*Made with ❤️ and Python*
