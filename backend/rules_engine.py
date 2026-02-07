from typing import Dict, Any
import random

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
    """Generate a varied fallback description based on outcome."""
    action = outcome.get("action", "your action").lower()
    roll = outcome.get("roll", 10)
    damage = outcome.get("damage_taken", 0)
    
    if outcome["is_crit"]:
        crit_msgs = [
            f"A CRITICAL SUCCESS! Your {action} is devastatingly effective!",
            f"Incredible! Your {action} succeeds spectacularly beyond your wildest dreams!",
            f"A natural 20! Your {action} achieves legendary status!",
        ]
        return random.choice(crit_msgs)
    
    if outcome["success"]:
        success_msgs = [
            f"Your {action} succeeds! You navigate the situation with skill.",
            f"Success! Your {action} has the desired effect.",
            f"The dungeon yields to your {action}. You advance cautiously.",
        ]
        return random.choice(success_msgs)
    else:
        fail_msgs = [
            f"Your {action} fails! You take {damage} damage as the dungeon punishes your hubris.",
            f"The dungeon rejects your attempt at {action}. You suffer {damage} damage.",
            f"Disaster! Your {action} backfires spectacularly, costing you {damage} HP.",
        ]
        return random.choice(fail_msgs)
