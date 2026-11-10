import pytest
from pyroast import pyroast

class Test:
    # GPA roast
    def test_roast_gpa(self):
        '''
        Verify roast_gpa() returns a non-empty string.
        '''
        actual = pyroast.roast_gpa(3.86)
        assert isinstance(actual, str), f"Expected roast_gpa() to return a string. Instead, it returned {actual}"
        assert len(actual) > 0, f"Expected roast_gpa() not to be empty. Instead, it returned a string with {len(actual)} characters"

    def test_roast_gpa_thresholds(self):
        '''
        Verify roast_gpa() across various thresholds
        '''
        sample_gpa = [1.0, 2.6, 2.9, 2.0, 3.6, 4.0]
        for g in sample_gpa:
            actual = pyroast.roast_gpa(g)
            assert isinstance(actual, str), f"Expected roast_gpa() to return a string for gpa {g}. Instead, it returned {actual}"
            assert len(actual) > 0, f"Expected roast_gpa() not to be empty for gpa {g}. Instead, it returned a string with {len(actual)} characters"

    def test_roast_gpa_sleep(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 3.9
        '''
        actual = pyroast.roast_gpa(4.0)
        assert actual == "I bet you've never known sleep before"

    
    def test_roast_gpa_smell(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 3.5
        '''
        actual = pyroast.roast_gpa(3.6)
        assert actual == "I smell wasted potential"

    def test_roast_gpa_network(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 3.0
        '''
        actual = pyroast.roast_gpa(3.1)
        assert actual == "Are you even trying? Or is college just a networking event for you?"

    def test_roast_gpa_quit(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 2.5
        '''
        actual = pyroast.roast_gpa(2.6)
        assert actual == "At this point, it might be better to give up"

    def test_roast_gpa_choice(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 2.0
        '''
        actual = pyroast.roast_gpa(2.1)
        assert actual == "I see you gave up, smartest choice you've ever made"

    def test_roast_gpa_drop(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 1.5
        '''
        actual = pyroast.roast_gpa(1.9)
        assert actual == "Gonna drop out soon?"

    def test_roast_gpa_low(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 1.0
        '''
        actual = pyroast.roast_gpa(1.1)
        assert actual == "McDonalds is always hiring"

    def test_roast_gpa_lower(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 0.5
        '''
        actual = pyroast.roast_gpa(0.9)
        assert actual == "Your GPA is lower than my room temperature"

    def test_roast_gpa_lowest(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 0.0
        '''
        actual = pyroast.roast_gpa(0.0)
        assert actual == "A gpa that low actually exists? Behold the 8th wonder of the world!"
    
    # Height roast
    def test_roast_height(self):
        """Verify roast_height() returns a non-empty string."""
        actual = pyroast.roast_height(6.0)
        assert isinstance(actual, str), f"Expected string, got {type(actual)}"
        assert len(actual) > 0, "Expected non-empty string"

    def test_roast_height_thresholds(self):
        """Verify roast_height() across different height thresholds."""
        sample_heights = [7.0, 6.7, 6.4, 6.1, 5.9, 5.0, 3.0]
        for h in sample_heights:
            actual = pyroast.roast_height(h)
            assert isinstance(actual, str), f"Expected string for height {h}, got {type(actual)}"
            assert len(actual) > 0, f"Expected non-empty string for height {h}"

    def test_roast_height_exact_messages(self):
        """Verify roast_height returns exact strings for specific height bands."""
        assert pyroast.roast_height(6.7) == "Haha funny"
        assert pyroast.roast_height(7.0) == "You might as well just be a tree!"
        assert pyroast.roast_height(4.0) == "How is that possible?"

    def test_roast_height_boundaries(self):
        """Values on the edge of height thresholds fall into the expected band."""
        assert pyroast.roast_height(6.3) == pyroast.roast_height(6.6)
        assert pyroast.roast_height(6.0) == pyroast.roast_height(6.29)
        assert pyroast.roast_height(5.8) == pyroast.roast_height(5.99)
        assert pyroast.roast_height(4.5) == pyroast.roast_height(5.79)

    def test_roast_height_accepts_int_and_float(self):
        """Ints and floats in the same band return identical roasts."""
        assert pyroast.roast_height(6) == pyroast.roast_height(6.0)
        assert pyroast.roast_height(7) == pyroast.roast_height(7.0)

    def test_roast_height_boundaries(self):
        """
        Verify values on the edge of each band land in the expected band.
        """
        assert pyroast.roast_height(6.7) == "Haha funny"
        assert pyroast.roast_height(6.71) == pyroast.roast_height(8.0)
        assert pyroast.roast_height(6.3) == pyroast.roast_height(6.69)
        assert pyroast.roast_height(6.0) == pyroast.roast_height(6.29)
        assert pyroast.roast_height(5.8) == pyroast.roast_height(5.99)
        assert pyroast.roast_height(4.5) == pyroast.roast_height(5.79)
        assert pyroast.roast_height(1) == pyroast.roast_height(4.49)

    def test_roast_height_rejects_out_of_range(self):
        """
        Heights below 1 ft or above 9 ft raise ValueError.
        """
        with pytest.raises(ValueError):
            pyroast.roast_height(0)
        with pytest.raises(ValueError):
            pyroast.roast_height(-5.5)
        with pytest.raises(ValueError):
            pyroast.roast_height(9.1)

    def test_roast_height_rejects_non_numbers(self):
        """
        Strings, None and booleans raise TypeError.
        """
        with pytest.raises(TypeError):
            pyroast.roast_height("six feet")
        with pytest.raises(TypeError):
            pyroast.roast_height(None)
        with pytest.raises(TypeError):
            pyroast.roast_height(True)

    # Coffee roast
    def test_roast_coffee(self):
        """
        Verify roast_coffee() returns a non-empty string.
        """
        actual = pyroast.roast_coffee(3)
        assert isinstance(actual, str), f"Expected string, got {type(actual)}"
        assert len(actual) > 0, "Expected a non-empty string"

    def test_roast_coffee_thresholds(self):
        """
        Verify roast_coffee() across different coffee thresholds.
        """
        sample_cups = [0, 1, 2, 3, 4, 5, 10]
        for cups in sample_cups:
            actual = pyroast.roast_coffee(cups)
            assert isinstance(actual, str), f"Expected string for {cups} cups"
            assert len(actual) > 0, f"Expected non-empty string for {cups} cups"

    def test_roast_coffee_espresso(self):
        """
        Verify high coffee consumption returns the espresso roast.
        """
        actual = pyroast.roast_coffee(6)
        assert actual == "Your blood has turned into espresso."

    def test_roast_coffee_boundaries(self):
        """
        Verify each band boundary gives the expected roast.
        """
        assert pyroast.roast_coffee(0) == "No coffee? You run on pure denial."
        assert pyroast.roast_coffee(1) == pyroast.roast_coffee(2)
        assert pyroast.roast_coffee(3) == pyroast.roast_coffee(4)
        assert pyroast.roast_coffee(5) == pyroast.roast_coffee(100)
        assert pyroast.roast_coffee(2) != pyroast.roast_coffee(3)

    def test_roast_coffee_rejects_negative(self):
        """
        Negative cup counts raise ValueError.
        """
        with pytest.raises(ValueError):
            pyroast.roast_coffee(-1)
        with pytest.raises(ValueError):
            pyroast.roast_coffee(-100)

    def test_roast_coffee_rejects_non_integers(self):
        """
        Floats, strings, None and booleans raise TypeError.
        """
        with pytest.raises(TypeError):
            pyroast.roast_coffee(2.5)
        with pytest.raises(TypeError):
            pyroast.roast_coffee("three")
        with pytest.raises(TypeError):
            pyroast.roast_coffee(None)
        with pytest.raises(TypeError):
            pyroast.roast_coffee(False)