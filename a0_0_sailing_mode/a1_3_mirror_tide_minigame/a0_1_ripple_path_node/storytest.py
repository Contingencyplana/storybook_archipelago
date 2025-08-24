from . import story

def test_observe_story():
    out = story.observe({})
    assert "ripples" in out.lower() or "path" in out.lower()
