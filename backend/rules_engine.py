from typing import Dict, Any
import random


def resolve_action(state: Dict[str, Any], action: str, roll: int | None = None) -> Dict[str, Any]:
	"""
	Very small rules resolver used by the backend.
	- If no roll is passed, roll a d20.
	- Success if roll + 0 >= difficulty (we keep difficulty simple).
	- Damage is randomly chosen when the player fails.
	Returns a dict with keys: success (bool), damage_taken (int), is_crit (bool), difficulty (int)
	"""
	if roll is None:
		roll = random.randint(1, 20)

	# simple difficulty heuristics: neighboring locations or actions might be harder
	difficulty = 10
	action_lower = action.lower()
	if "attack" in action_lower or "strike" in action_lower:
		difficulty = 8
	if "sneak" in action_lower or "stealth" in action_lower:
		difficulty = 12
	if "climb" in action_lower or "jump" in action_lower:
		difficulty = 11

	is_crit = roll == 20
	success = roll >= difficulty

	if success:
		damage_taken = 0
	else:
		# damage scales with how badly you failed
		margin = difficulty - roll
		damage_taken = random.randint(1, max(1, margin))

	return {
		"success": success,
		"damage_taken": damage_taken,
		"is_crit": is_crit,
		"difficulty": difficulty,
		"roll": roll,
		"action": action,
	}


def describe_outcome(outcome: Dict[str, Any]) -> str:
	if outcome["success"]:
		if outcome["is_crit"]:
			return "A brilliant success — you landed a critical blow!"
		return "You succeed at the action."
	return f"You fail and take {outcome['damage_taken']} damage."
