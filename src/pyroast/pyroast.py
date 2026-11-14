import random
from typing import Optional

def roast_gpa(gpa: float) -> str:
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise TypeError(f"gpa must be a number, got {type(gpa).__name__}")

    if gpa < 0 or gpa > 4.0:
        raise ValueError(f"gpa must be between 0 and 4.0, got {gpa}")

    smart_roasts = [
        "I bet you've never known sleep before",
        "no network, no friends, just grind",
        "your favorite past time must be studying",
        "your blood must be pure energy drinks"
    ]

    average_roasts = [
        "I smell wasted potential",
        "mid doesn't cut it, you're just a statistic",
        "yeah sure, you and everyone else",
        "blends into the crowd so well, you become invisible"
    ]

    below_roasts = [
        "Are you even trying? Or is college just a networking event for you?",
        "let me guess, business major?",
        "let me guess, you think you're street smart and not book smart?",
        "its a slipery slope, but you love living on the edge huh?"
    ]

    low_roasts = [
        "at this point it would be better to drop out",
        "McDonalds is always hiring",
        "have you ever said I'm smart in my own way before?",
        "honestly, it may be harder to get this low than it is to be average"
    ]

    bad_roasts = [
        "I see you gave up, smartest choice you ever made",
        "A gpa that low actually exists? Behold, the 8th wonder of the world",
        "maybe you could be a youtuber?",
        "how did you make it this far anyways?"
    ]

    if gpa >= 3.9:
        return random.choice(smart_roasts)
    elif gpa >= 3.5:
        return random.choice(average_roasts)
    elif gpa >= 2.0:
        return random.choice(below_roasts)
    elif gpa >= 1.0:
        return random.choice(low_roasts)
    else:
        return random.choice(bad_roasts)


ROAST_DATA: dict[str, dict[str, list[str]]] = {
    "tree": {
        "standard": [
            "You might as well just be a tree!",
            "Are the clouds blocking your view down here?",
            "Do you need a permit to be that tall?",
            "Please watch out for low-flying aircraft.",
        ],
        "poem": [
            (
                "Your head is brushing past the clouds,\n"
                "You tower over earthly crowds.\n"
                "Before you take another stride,\n"
                "Please check for planes on either side."
            ),
            (
                "No ladder needed in your home,\n"
                "You practically touch the ceiling dome.\n"
                "The squirrels think you're one of theirs,\n"
                "And ceiling fans are your worst nightmares."
            ),
        ],
    },
    "funny_67": {
        "standard": [
            "Haha funny",
            "6'7? You hit the exact meme height jackpot.",
            "Spot on 6.7 feet, classic.",
        ],
        "poem": [
            (
                "Six point seven on the dot,\n"
                "You hit the internet's favorite spot.\n"
                "No taller, shorter, low, or high—\n"
                "Just a walking meme passing by."
            ),
        ],
    },
    "nba": {
        "standard": [
            "Too short to make it to the NBA. Almost there.",
            "Benchwarmer status in the league at best.",
            "So close to basketball glory, yet so far.",
            "Have you considered volleyball instead?",
        ],
        "poem": [
            (
                "You're tall enough to block the sun,\n"
                "Yet still too short to make the run.\n"
                "The NBA won't call your phone,\n"
                "Enjoy the bench you've made your throne."
            ),
            (
                "You've got the reach, you've got the height,\n"
                "Just not enough for Friday night.\n"
                "Forget the draft and pro-league fame—\n"
                "Stick to watching from the game."
            ),
        ],
    },
    "six_foot": {
        "standard": [
            "Yeah, sure you are.",
            "Tinder profile says 6'0, reality says 5'10.",
            "Are those shoes adding an extra two inches?",
            "Barely snuck into the six-foot club, didn't you?",
        ],
        "poem": [
            (
                "Your dating app says six-foot-flat,\n"
                "We both know there's a catch to that.\n"
                "Take off those chunky platform shoes,\n"
                "And watch your extra inches lose."
            ),
            (
                "You stand up straight and hold your breath,\n"
                "Defending six-foot to the death.\n"
                "A millimeter shy of fame,\n"
                "Still rounding up to stake your claim."
            ),
        ],
    },
    "weather": {
        "standard": [
            "How's the weather down there?",
            "Standing right on the edge of average.",
            "Neither short nor tall, just conveniently baseline.",
            "You blend into every crowd seamlessly.",
        ],
        "poem": [
            (
                "Not quite tall and not quite small,\n"
                "The most average stature of them all.\n"
                "You blend into the daily crowd,\n"
                "Completely unremarkable and proud."
            ),
        ],
    },
    "wonka": {
        "standard": [
            "Willy Wonka wants you back in the chocolate factory.",
            "Do you get a discount on kids' menu items?",
            "Watch out for the top shelf in the pantry.",
            "Do you need a step stool to reach the counter?",
        ],
        "poem": [
            (
                "The top shelf is a distant dream,\n"
                "The step stool is your favorite team.\n"
                "If Wonka calls, don't act surprised—\n"
                "Your shift starts now, you're fun-sized!"
            ),
            (
                "You ask for kids' menus when you dine,\n"
                "And need a boost to see a sign.\n"
                "At least on flights you've got the space,\n"
                "To stretch your legs in any place."
            ),
        ],
    },
    "impossible": {
        "standard": [
            "How is that possible?",
            "Are you measuring in yards by accident?",
            "Is this height scientifically verified?",
            "Did you shrink in the laundry?",
        ],
        "poem": [
            (
                "Did someone shrink you in the wash,\n"
                "Or misread inches just for gosh?\n"
                "Before we call a scientist in,\n"
                "Check which end of the tape you're in."
            ),
        ],
    },
}


def _get_height_category(height: float) -> str:
    
    if height > 6.7:
        return "tree"
    if height == 6.7:
        return "funny_67"
    if height >= 6.3:
        return "nba"
    if height >= 6.0:
        return "six_foot"
    if height >= 5.8:
        return "weather"
    if height >= 4.5:
        return "wonka"
    return "impossible"


def roast_height(height: float, style: Optional[str] = "standard") -> str:

    if isinstance(height, bool) or not isinstance(height, (int, float)):
        raise TypeError(
            f"height must be a number, got {type(height).__name__}"
        )

    if not (1 <= height <= 9):
        raise ValueError(
            f"height must be between 1 and 9 feet, got {height}"
        )

    if style is None or (isinstance(style, str) and not style.strip()):
        normalized_style = "standard"
    elif isinstance(style, str):
        normalized_style = style.strip().lower()
    else:
        raise TypeError(
            f"style must be a string or None, got {type(style).__name__}"
        )

    valid_styles = {"standard", "poem"}
    if normalized_style not in valid_styles:
        raise ValueError(
            f"style must be one of {sorted(valid_styles)}, got {style!r}"
        )

    category = _get_height_category(height)
    return random.choice(ROAST_DATA[category][normalized_style])

def roast_coffee(cups: int) -> str:
    """Roast the user based on how many cups of coffee they drink a day.

    cups must be a whole number of 0 or more.
    Raises TypeError for non-integer input and ValueError for negative values.
    """
    if isinstance(cups, bool) or not isinstance(cups, int):
        raise TypeError(f"cups must be a whole number, got {type(cups).__name__}")
    if cups < 0:
        raise ValueError(f"cups cannot be negative, got {cups}")

    if cups == 0:
        return "No coffee? You run on pure denial."
    elif cups <= 2:
        return "Less than 2 cups? Still on the free trial of adulthood."
    elif cups <= 4:
        return "Your coffee needs a coffee."
    else:
        return "Your blood has turned into espresso."


def roast_sleep(hours: float) -> str:
    """Roast the user based on how many hours they slept last night.

    hours must be a number between 0 and 24 inclusive.
    Raises TypeError for non-numeric input and ValueError for out-of-range values.
    """
    if isinstance(hours, bool) or not isinstance(hours, (int, float)):
        raise TypeError(f"hours must be a number, got {type(hours).__name__}")
    if hours < 0 or hours > 24:
        raise ValueError(f"hours must be between 0 and 24, got {hours}")

    if hours == 0:
        return "Zero hours? Your eye bags have eye bags."
    elif hours < 4:
        return "That's not sleep, that's a long blink."
    elif hours < 6:
        return "Running on vibes and caffeine, I see."
    elif hours < 8:
        return "Almost a functional adult. Almost."
    elif hours <= 10:
        return "Eight hours? Who are you, a wellness influencer?"
    else:
        return "You're not well-rested, you're hibernating."

def roast_age(age: int) -> str:
    """
    Roast the user based on their age. Takes only a whole number in years.
    Negative age is acceptable (will be considered unborn).
    """

    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError(f"Age should be a whole number of years, instead got {type(age).__name__}")

    if age > 99:
        return "Careful sandbag! Every second is a 50/50 gamble!"
    elif age > 89:
        return "Have your skin flaps grown mold yet?"
    elif age > 64:
        return "Has your family started digging your grave yet?"
    elif age > 39:
        return "We should bet on which organ starts giving up first."
    elif age > 31:
        return "Your bank account is looking pretty dry and your energy bar looks even drier."
    elif age > 27:
        return "Everyone else already has kids, a car, and a house... what are you still doing in your mom's basement?"
    elif age > 24:
        return "Quarter-life crisis mode: fully engaged."
    elif age > 19:
        return "How is the job search going? Still nothing?"
    elif age > 9:
        return "Keep eating that junk food! More joy now and more health problems later!"
    elif age > 0:
        return "You're probably a dirt eater."
    else:
        return "Did your mom's womb come with a computer?"

def roast_screen_time(time: float) -> str:
    if isinstance(time, bool) or not isinstance(time, (int, float)):
        raise TypeError(f"time must be a number, got {type(time).__name__}")
    
    if time < 0 or time > 24.0:
        raise ValueError(f"time must be between 0 and 24.0, got {time}")

    no_life_roasts = [
        "I just know that you have no life",
        "Very productive? Doubt it",
        "Sleep must be an urban myth to you",
        "Bro does photosynthesis with screen light"
    ]

    streamer_roasts = [
        "Dropped out to become a streamer?",
        "Quick question, ever heard of grass before?",
        "Your screen is costing half of the power grid",
        "Your glasses need glasses"
    ]

    college_roasts = [
        "Let me guess, college student?",
        "Either you're a CS major or a business major",
        "Another one has joined the doom scrollers",
        "Let me guess, Gen Z?"
    ]

    less_roasts = [
        "Tiger parent?",
        "Are you on probation?",
        "Bro probably has only 3 apps on his phone",
        "What did you do to get your parents that mad?"
    ]

    old_roasts = [
        "I bet you don't even know what AI is",
        "Do you still use those old dusty textbooks?",
        "My grandma has a bigger online personality than you",
        "Did your parents not let you have a phone until you were 18?"
    ]

    if time >= 18.0:
        return random.choice(no_life_roasts)
    elif time >= 12.0:
        return random.choice(streamer_roasts)
    elif time >= 8.0:
        return random.choice(college_roasts)
    elif time >= 4.0:
        return random.choice(less_roasts)
    else:
        return random.choice(old_roasts)