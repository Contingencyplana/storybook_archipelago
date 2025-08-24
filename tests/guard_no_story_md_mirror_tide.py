import os

OVERRIDE_FLAG = "ALLOW_MIRROR_TIDE_STORY_FILES"
TARGET_PREFIX = os.path.join("a0_0_sailing_mode", "a1_3_mirror_tide_minigame")

def test_no_story_md_in_mirror_tide():
    if os.path.exists(OVERRIDE_FLAG):
        return
    offenders = []
    for root, _, files in os.walk(TARGET_PREFIX):
        for f in files:
            if f.lower() == "story.md":
                offenders.append(os.path.join(root, f))
    assert not offenders, f"Mirror Tide story.md files are gated. Remove them or create {OVERRIDE_FLAG} to allow."
