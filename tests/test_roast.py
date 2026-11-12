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

    def test_roast_gpa_bounds(self):
        '''
        Verify roast_gpa() raises ValueError for values out of the bounds of 0.0 o 4.0
        '''
        with pytest.raises(ValueError):
            pyroast.roast_gpa(-0.1)
        with pytest.raises(ValueError):
            pyroast.roast_gpa(4.1)

    def test_roast_gpa_non_numbers(self):
        '''
        Verify roast_gpa() raises TypeError for Strings, None, and boolean
        '''
        with pytest.raises(TypeError):
            pyroast.roast_gpa("3.5")
        with pytest.raises(TypeError):
            pyroast.roast_gpa(None)
        with pytest.raises(TypeError):
            pyroast.roast_gpa(True)
    
    # Height roast multi-choice test suite
    def test_roast_height(self):
        '''Verify roast_height() returns a non-empty string.'''
        actual = pyroast.roast_height(6.0)
        assert isinstance(actual, str), f"Expected string, got {type(actual)}"
        assert len(actual) > 0, "Expected non-empty string"

    def test_roast_height_thresholds(self):
        '''Verify roast_height() across different height thresholds.'''
        sample_heights = [7.0, 6.7, 6.4, 6.1, 5.9, 5.0, 3.0]
        for h in sample_heights:
            actual = pyroast.roast_height(h)
            assert isinstance(actual, str), f"Expected string for height {h}, got {type(actual)}"
            assert len(actual) > 0, f"Expected non-empty string for height {h}"

    def test_roast_height_pool_membership(self):
        '''Verify returned roast belongs to the expected pool for each bracket.'''
        valid_67_roasts = [
            "Haha funny",
            "6'7? You hit the exact meme height jackpot.",
            "Spot on 6.7 feet, classic.",
        ]
        actual = pyroast.roast_height(6.7)
        assert actual in valid_67_roasts, f"Unexpected roast returned: {actual}"

    def test_roast_height_tree_pool(self):
        '''Verify heights above 6.7 return a roast from the tree pool.'''
        valid_tree_roasts = [
            "You might as well just be a tree!",
            "Are the clouds blocking your view down here?",
            "Do you need a permit to be that tall?",
            "Please watch out for low-flying aircraft.",
        ]
        actual = pyroast.roast_height(7.2)
        assert actual in valid_tree_roasts

    def test_roast_height_wonka_pool(self):
        '''Verify heights between 4.5 and 5.8 return a roast from the Wonka pool.'''
        valid_wonka_roasts = [
            "Willy Wonka wants you back in the chocolate factory.",
            "Do you get a discount on kids' menu items?",
            "Watch out for the top shelf in the pantry.",
            "Do you need a step stool to reach the counter?",
        ]
        actual = pyroast.roast_height(5.0)
        assert actual in valid_wonka_roasts

    def test_roast_height_randomness_returns_variety(self):
        '''Verify calling roast_height multiple times produces valid non-empty responses.'''
        results = set()
        for _ in range(20):
            res = pyroast.roast_height(6.7)
            assert isinstance(res, str)
            results.add(res)
        # Verify at least one valid string was selected
        assert len(results) >= 1

    def test_roast_height_default_style_fallbacks(self):
        '''Verify omitted, empty, None, or uppercase 'standard' returns a standard roast.'''
        valid_67_roasts = [
            "Haha funny",
            "6'7? You hit the exact meme height jackpot.",
            "Spot on 6.7 feet, classic.",
        ]
        for style_input in ("standard", "STANDARD", "  standard  ", "", "   ", None):
            actual = pyroast.roast_height(6.7, style=style_input)
            assert actual in valid_67_roasts, f"Unexpected roast for style={style_input!r}: {actual}"

    def test_roast_height_poem_style(self):
        '''Verify style='poem' returns a multi-line poem from the expected bracket.'''
        valid_67_poems = [
            (
                "Six point seven on the dot,\n"
                "You hit the internet's favorite spot.\n"
                "No taller, shorter, low, or high—\n"
                "Just a walking meme passing by."
            ),
        ]
        for style_input in ("poem", "POEM", "  Poem  "):
            actual = pyroast.roast_height(6.7, style=style_input)
            assert actual in valid_67_poems

    def test_roast_height_poem_thresholds(self):
        '''Verify poem style works across all height brackets.'''
        sample_heights = [7.0, 6.7, 6.4, 6.1, 5.9, 5.0, 3.0]
        for h in sample_heights:
            actual = pyroast.roast_height(h, style="poem")
            assert isinstance(actual, str)
            assert "\n" in actual, f"Expected multi-line poem for height {h}, got {actual!r}"

    def test_roast_height_rejects_out_of_range(self):
        '''Heights below 1 ft or above 9 ft raise ValueError.'''
        with pytest.raises(ValueError):
            pyroast.roast_height(0)
        with pytest.raises(ValueError):
            pyroast.roast_height(-5.5)
        with pytest.raises(ValueError):
            pyroast.roast_height(9.1)

    def test_roast_height_rejects_non_numbers(self):
        '''Strings, None and booleans raise TypeError.'''
        with pytest.raises(TypeError):
            pyroast.roast_height("six feet")
        with pytest.raises(TypeError):
            pyroast.roast_height(None)
        with pytest.raises(TypeError):
            pyroast.roast_height(True)

    def test_roast_height_rejects_invalid_style(self):
        '''Unrecognized style strings raise ValueError and non-strings raise TypeError.'''
        with pytest.raises(ValueError):
            pyroast.roast_height(6.0, style="haiku")
        with pytest.raises(ValueError):
            pyroast.roast_height(6.0, style="rap")
        with pytest.raises(TypeError):
            pyroast.roast_height(6.0, style=123)
        with pytest.raises(TypeError):
            pyroast.roast_height(6.0, style=True)

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
        """Verify exact roast messages at each band boundary."""
        actual = pyroast.roast_coffee(0)
        assert actual == "No coffee? You run on pure denial."
        actual = pyroast.roast_coffee(1)
        assert actual == "Less than 2 cups? Still on the free trial of adulthood."
        actual = pyroast.roast_coffee(2)
        assert actual == "Less than 2 cups? Still on the free trial of adulthood."
        actual = pyroast.roast_coffee(3)
        assert actual == "Your coffee needs a coffee."
        actual = pyroast.roast_coffee(4)
        assert actual == "Your coffee needs a coffee."
        actual = pyroast.roast_coffee(5)
        assert actual == "Your blood has turned into espresso."
        actual = pyroast.roast_coffee(100)
        assert actual == "Your blood has turned into espresso."

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
        with pytest.raises(TypeError):
            pyroast.roast_coffee(True)
        with pytest.raises(TypeError):
            pyroast.roast_coffee(2.0)