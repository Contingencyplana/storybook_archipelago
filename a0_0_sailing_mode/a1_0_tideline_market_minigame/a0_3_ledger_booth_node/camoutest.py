from . import camouflage
def test_apply_mood_noop_shape(): src = "hello" out = camouflage.apply_mood(src, {}) assert isinstance(out, str) and out == src
