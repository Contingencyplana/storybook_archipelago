from . import orchestration

def test_fallback_message():
    msg = orchestration.fallback("?", {})
    assert "unknown" in msg.lower()
    assert "gate" in msg.lower() or "pressure" in msg.lower()
