import random
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess, get_range_for_difficulty


def test_check_guess_higher_than_secret_returns_too_high_and_lower_hint():
    outcome, message = check_guess(60, 50)

    assert outcome == "Too High"
    assert "LOWER" in message


def test_check_guess_lower_than_secret_returns_too_low_and_higher_hint():
    outcome, message = check_guess(40, 50)

    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_easy_difficulty_secret_generated_within_easy_range():
    low, high = get_range_for_difficulty("Easy")
    secret = random.randint(low, high)

    assert (low, high) == (1, 20)
    assert low <= secret <= high


def test_hard_difficulty_secret_generated_within_hard_range():
    low, high = get_range_for_difficulty("Hard")
    secret = random.randint(low, high)

    assert (low, high) == (1, 50)
    assert low <= secret <= high
