def handle_left(memory: dict) -> str:
    # Dry-run: plan a safe sweep of last 10 commit messages
    plan = (
        "You outline the sweep in chalk. [LEFT]\n"
        "- Tag safety point\n"
        "- Rewrite last 10 messages (dry-run narrative only)\n"
        "- Review log, then push with lease"
    )
    return plan
