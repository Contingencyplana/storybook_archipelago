
# Starfish Harbor – taskmaps

## 🎮 Controls

- Use lowercase l and r for choices in the terminal runner.
	Example: `python .\tools\play_node.py a0_0_sailing_mode\a0_1_starfish_harbor_minigame\a0_1_coral_quay_node\ --loop`

## 🎭 Camouflage Layers to Explore

- Fog – gentle recursion masking
- Silence – sound used to imply presence
- Mirror – player memory subtly reflected back
- Rhythm – poetic l/r choices with no immediate payoff

## 🧪 Testing and Build Flow

This minigame follows the 7-step workflow (see `workflow.md`), building one node at a time with green tests.

Required coverage:

- Integration routing
- Camouflage triggers
- Memory state validation
- l/r logic and required markers
- Story presentation and branching

## 🔁 Escalation Notes

If recursion fails during node construction (e.g., a logic loop, camouflage breakdown, or test gap):

- Log the event in `subtaskmap.md` of the affected node
- Escalate to `mirror_decisions/` if unrecoverable
- Postpone linking in `portalmap.md` until node passes `orchtest.py`, `camoutest.py`, and `storytest.py`

## 🔚 Closing Thought

Starfish Harbor doesn’t explain recursion; it lets the player feel it. It invites, not surprises.

> “Every first recursion is a kindness.”
