from . import story

def test_observe_story():
    out = story.observe({})
    assert "drift" in out.lower() or "pressure" in out.lower() or "stillness" in out.lower()
