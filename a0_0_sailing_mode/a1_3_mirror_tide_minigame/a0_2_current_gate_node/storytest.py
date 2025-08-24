from . import story

def test_observe_story():
    out = story.observe({})
    assert "hinge" in out.lower() or "pull" in out.lower() or "gate" in out.lower()
