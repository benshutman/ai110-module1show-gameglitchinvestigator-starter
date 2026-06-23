from logic_utils import get_range_for_difficulty, check_guess, update_score

# ── Baseline / sanity ─────────────────────────────────────────────────────────


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high_outcome():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low_outcome():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# ── FIX: Bug 1: Normal and Hard difficulty ranges were swapped ─────────────────────
# Normal returned (1, 100) and Hard returned (1, 50) — they were reversed.


def test_difficulty_normal_upper_bound():
    _, high = get_range_for_difficulty("Normal")
    assert high == 50  # was 100


def test_difficulty_hard_upper_bound():
    _, high = get_range_for_difficulty("Hard")
    assert high == 100  # was 50


# ── FIX: Bug 2: "Go HIGHER" / "Go LOWER" hint messages were swapped ───────────────
# guess > secret showed "Go HIGHER" (wrong); guess < secret showed "Go LOWER" (wrong).


def test_too_high_message_says_lower():
    _, message = check_guess(60, 50)  # 60 > 50 → hint must say LOWER
    assert "LOWER" in message  # was "HIGHER"


def test_too_low_message_says_higher():
    _, message = check_guess(40, 50)  # 40 < 50 → hint must say HIGHER
    assert "HIGHER" in message  # was "LOWER"


# ── FIX: Bug 3: Secret was cast to str on even attempts ───────────────────────────
# The app converted secret to str every even attempt before calling check_guess.
# Python's string comparison makes "90" > "100" (True), so check_guess(90, "100")
# returned "Too High" instead of the correct "Too Low".


def test_check_guess_int_secret_90_vs_100():
    # With int secret (the fix): 90 < 100 → correct outcome
    outcome, _ = check_guess(90, 100)
    assert outcome == "Too Low"


def test_check_guess_str_secret_gives_wrong_result():
    # With str secret (the bug): "90" > "100" lexicographically → wrong outcome
    # This test documents the incorrect behaviour that the fix eliminates.
    outcome, _ = check_guess(90, "100")
    assert outcome == "Too High"  # wrong result produced by str comparison


# ── FIX: Bug 4: update_score returned +5 on even attempts instead of −5 ───────────
# For a "Too High" outcome, attempt_number % 2 == 0 triggered +5 instead of −5.


def test_update_score_too_high_even_attempt():
    score = update_score(100, "Too High", attempt_number=2)
    assert score == 95  # was 105


def test_update_score_too_high_another_even_attempt():
    score = update_score(0, "Too High", attempt_number=4)
    assert score == -5  # was +5


def test_update_score_too_high_odd_attempt_unchanged():
    # Odd attempts were never affected by the bug; verify they still pass.
    score = update_score(100, "Too High", attempt_number=3)
    assert score == 95


def test_update_score_too_low_always_deducts():
    score = update_score(100, "Too Low", attempt_number=2)
    assert score == 95
