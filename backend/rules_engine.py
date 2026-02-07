'''
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
<<<<<<< HEAD
	if outcome["success"]:
		if outcome["is_crit"]:
			return "A brilliant success — you landed a critical blow!"
		return "You succeed at the action."
	return f"You fail and take {outcome['damage_taken']} damage."
'''

import random 

def roll_dice(sides: int) -> int:
	return random.randint(1, sides)

def roll_d20(advantage=False, disadvantage =False) -> int:
	r1 = roll_dice(20)
	r2 = roll_dice(20)

	if advantage:
		return max(r1, r2)
	if disadvantage:
		return min(r1, r2)
	return r1

def get_modifier(stat: int) -> int:
	if stat <= 3: return -2
	if stat <= 7: return -1
	if stat <= 12: return 0
	if stat <= 16: return 1
	return 2

DC = {
	"easy": 10,
	"medium": 15,
	"hard": 20
}

# Attacking the System 
WEAPON_DAMAGE = {
	"dagger": lambda: roll_die(4),
	"sword": lambda: roll_die(6),
	"greatsword": lambda: roll_die(6) + roll_die(6),
	"bow": lambda: roll_die(6)
}

def attack_rol(attacker_stat, enemy_ac, weapon):
	roll = roll_d20()
	mod = get_modifier(attacker_stat)
	total = roll + mod
	

	hit = total >= enemy_ac
	damage = WEAPON_DAMAGE.get(weapon, lambda: 0)() if hit else 0

	return {
		"roll": roll,
		"mod": mod,
		"total": total,
		"hit": hit,
		"damage": damage,
		"is_crit": roll == 20
	}

def use_item(item: str):
	if item == "healing_potion":
		return {"heal": roll_die(6) + 2}
	if item == "torch":
		return {"light": True}
	if item == "lockpick":
		return {"advantage": True}
	return {}
=======
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
>>>>>>> e577f5a4ff8bf8813694a41ec5896d6b8900f4a7
