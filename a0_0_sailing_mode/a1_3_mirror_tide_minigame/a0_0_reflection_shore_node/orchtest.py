from . import orchestration

def test_fallback_message():
    msg = orchestration.fallback("?", {})
    assert "unknown" in msg.lower()
    assert "tide" in msg.lower()
