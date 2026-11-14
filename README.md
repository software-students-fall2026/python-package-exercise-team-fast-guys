# PyRoast

## Build and test status

[![build and test](https://github.com/software-students-fall2026/python-package-exercise-team-fast-guys/actions/workflows/build.yml/badge.svg)](https://github.com/software-students-fall2026/python-package-exercise-team-fast-guys/actions/workflows/build.yml)

## Description
pyroast is a lighthearted Python package designed to roast users based on their personal statistics. By taking info like GPA, height, sleep duration, age, screen time, and coffee intake, the package evaluates each value to return customized, sarcastic commentary.

## PyPI Package Link
[Install PyRoast from PyPI](https://pypi.org/project/team-fast-pyroast/0.1.2/)

## Installation

Install from PyPI:

```bash
pip install team-fast-pyroast==0.1.2
```

Then import the functions you want:

```python
from pyroast import roast_gpa, roast_height, roast_sleep, roast_coffee, roast_age, roast_screen_time
```

or use the package namespace:

```python
import pyroast
print(pyroast.roast_sleep(5))
```

## Usage

### roast_gpa

#### Evaluates a student's Grade Point Average (GPA) and returns a customized roast.

Parameters: gpa (float | int): The GPA score (e.g., 3.86) between 0.0 and 4.0 inclusive.

Returns: str — A randomly selected roast string based on the GPA.

Raises:

TypeError: If gpa is not a float nor an int or is a boolean.

ValueError: If gpa is less than 0.0 or if gpa is greater than 4.0.

### roast_height

#### Generates a roast based on height measured in feet.

Parameters:

- height (float | int): Height in feet (e.g., 6.0, 5.8) where height is between 1 and 9 feet inclusive.
- style (str | None, optional): Format of the roast — `"standard"` (default, also used if empty or `None`) for a one-liner, or `"poem"` for a short verse.

Returns: str — A roast string or multi-line poem evaluating the input height.

Raises:

TypeError: If height is not an integer or a float (or is a boolean), or if style is not a string or None.

ValueError: If the height is less than 1 or greater than 9, or if style is not `"standard"` or `"poem"`.

### roast_sleep

#### Roasts the user based on how many hours of sleep they got last night.

Parameters: hours (float | int): Hours of sleep achieved. Must be a number between 0 and 24 inclusive.

Returns: str — A roast string tailored to the sleep duration.

Raises:

TypeError: If hours is non-numeric or a boolean.

ValueError: If hours is less than 0 or greater than 24.

### roast_coffee

#### Evaluates daily caffeine intake and returns a roast based on the number of coffee cups consumed.

Parameters: cups (int): Number of cups of coffee drank today.

Returns: str — A roast assessing caffeine dependence.

Raises:

TypeError: If the input is not an integer or is a boolean.

ValueError: If the number of cups is negative.

### roast_age

#### Evaluates the user's age in years and returns an age roast.

Parameters: age (int): Age in years. Can be a negative number (counts as "unborn").

Returns: str — A roast string based on the user's age bracket.

Raises:

TypeError: If age is not an integer or is a boolean.

### roast_screen_time

#### Roasts the user based on their daily screen time

Parameters: time (float | int): Number of hours spend on screens per day between 0 and 24 inclusive

Returns: str — A randomly selected roast string based on the user's screen time

Raises:

TypeError: If time is non-numeric or a boolean.

ValueError: If time is less than 0 or greater than 24.

## Program Examples

All examples assume `from pyroast import *` or the explicit import above.

### High GPA

```python
print(roast_gpa(3.95))
# One of several possible roasts:
# I bet you've never known sleep before
```

### Tall height (standard)

```python
print(roast_height(6.8))
# one of several roasts for this height, for example:
# You might as well just be a tree!
```

### Tall height (poem)

```python
print(roast_height(6.8, style="poem"))
# Your head is brushing past the clouds,
# You tower over earthly crowds.
# Before you take another stride,
# Please check for planes on either side.
```

### 0 hours sleep

```python
print(roast_sleep(0))
# Zero hours? Your eye bags have eye bags.
```

### A lot of coffee

```python
print(roast_coffee(5))
# Your blood has turned into espresso.
```

### Mid 20s

```python
print(roast_age(25))
# Quarter-life crisis mode: fully engaged.
```


### High Screen Time

```python
print(roast_screen_time(24))
# One of several possible roasts:
# I just know that you have no life
```

### Invalid input

Every function validates its argument and raises a standard Python error you can catch:

```python
try:
    roast_sleep(30)
except ValueError as e:
    print(e)   # hours must be between 0 and 24, got 30

try:
    roast_age("twenty")
except TypeError as e:
    print(e)   # Age should be a whole number of years, instead got str
```

## Example Program

For a complete working example that demonstrates all six package functions in a single script, see:
* 📄 [**Example Script (`__main__.py`)**](./src/pyroast/__main__.py)

## Development setup

### Setting Up Virtual Environment and Dependencies
1. Install `pipenv` if you have not yet using `pip install --user pipenv`.
2. Install dependencies and set up virtual environment using `pipenv install`.
3. Activate the virtual environment using `pipenv shell`.
4. To install the package locally for development run `pipenv install -e .`.

### Adding and Running Tests
1. Add a new Python file in the `tests` directory for your added method/unit.
    1. Import `pytest` and `pyroast`.
    2. Create a class using `Test` as a prefix and enter methods within it with `test_` as a prefix.
2. Run `pytest` to run tests in the `tests` directory.

### Building the Package
To build the package and generate distribution files in the `dist/` directory, run:

```bash
pipenv run python -m build
```

Pull requests will build and test with Github Actions.

## Team members

- [Robert Fang](https://github.com/rfang1224)

- [James Li](https://github.com/DyingRavioli)

- [Danial Sagimbayev](https://github.com/catw1thtea)

- [Pranay Engineer](https://github.com/PranayEng) 

- [Daniyal Malik](https://github.com/DaniyalMlk) 

