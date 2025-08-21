
ALLOWED_TOKENS = {"grove", "market", "channel", "pool", "moor", "gate"}

def assert_valid_locale(output: str):
    """
    Assert that the output string contains at least one allowed locale token (case-insensitive).
    Allowed tokens are defined in ALLOWED_TOKENS.
    """
    s = output.lower()
    if not any(token in s for token in ALLOWED_TOKENS):
        raise AssertionError(f"Output must contain one of {sorted(ALLOWED_TOKENS)}, got: {output!r}")
