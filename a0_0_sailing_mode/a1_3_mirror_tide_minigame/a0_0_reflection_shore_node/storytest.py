from . import story

def test_observe_story():
    out = story.observe({})
    assert "shore" in out.lower() or "seashells" in out.lower()
