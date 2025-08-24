import os

OVERRIDE_FLAG = "ALLOW_ECHOING_GROTTO_STORY_FILES"
TARGET_PREFIX = os.path.join("a0_0_sailing_mode", "a1_2_echoing_grotto_minigame")

def test_no_story_md_in_echoing_grotto():
    if os.path.exists(OVERRIDE_FLAG):
        return
    offenders = []
    for root, _, files in os.walk(TARGET_PREFIX):
        for f in files:
            if f.lower() == "story.md":
                offenders.append(os.path.join(root, f))
    assert not offenders, f"Echoing Grotto story.md files are gated. Remove them or create {OVERRIDE_FLAG} to allow."
