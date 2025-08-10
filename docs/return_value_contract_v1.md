# Return value contract (handlers & story) — v1
- Handlers (leftmain.py/rightmain.py) MUST return **strings**.
- Story functions (story.py) MUST return **strings**.
- Left-path outputs MUST include the literal “[LEFT]”.
- Right-path outputs MUST include the literal “[RIGHT]”.
- Story outputs MUST contain the word “grove”.
- Story outputs MUST NOT contain the substring “[PORTAL:”.
- Markers are plain-string literals (not Markdown).

**Tier 3 exception:** Tier 3 nodes may omit the [LEFT]/[RIGHT] markers; tests do not rely on them. Markers remain recommended to ease future upgrades and diagnostics.
