from . import orchestration

def test_fallback_message():
    msg = orchestration.fallback("?", {})
    assert "unknown" in msg.lower()
    assert "quiet" in msg.lower() or "settle" in msg.lower()
