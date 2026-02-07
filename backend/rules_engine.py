from typing import Dict, Any
import random

'''
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

def attack_roll(attacker_stat, enemy_ac, weapon):
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

def resolve_action(state, action: str, forced_roll=None):
	action_lower = action.lower()
	inventory = state.get("inventory", [])
	player_stat = 12 #placeholder stat
	enemy_ac = 12 #placeholder enemy AC

	#1. Determining advantage from items
	advantage = "lockpick" in inventory and ("lock" in action_lower)

	#2. Rolling the dice
	roll = forced_roll if forced_roll is not None else roll_d20(advantage=advantage)

	#3. Attacking actions 
	if "attack" in action_lower or "strike" in action_lower:
		weapon = "sword" if "sword" in inventory else "dagger"
		atk = attack_roll(player_stat, enemy_ac, weapon)
		
		return {
			"success": atk["hit"],
			"damage_taken": 0 if atk["hit"] else roll_die(4),
			"is_crit": atk["is_crit"],
			"difficulty": enemy_ac,
			"roll": atk["roll"],
			"action": action, 
			"damage_dealt": atk["damage"]
		}

	#4. Skill Checks 
	if "sneak" in action_lower:
		dc = DC["medium"]
	elif "climb" in action_lower or "jump" in action_lower:
		dc = DC["easy"]
	else: 
		dc = DC["easy"]

	mod = get_modifier(player_stat)
	total = roll + mod
	success = total >= dc

	damage_taken = 0 if success else roll_die(4)

	return {
		"success": success, 
		"damage_taken": damage_taken, 
		"is_crit": roll == 20, 
		"difficulty": dc, 
		"roll": roll, 
		"action": action
	} 

def describe_outcome(outcome):
	if outcome["success"]:
		if outcome["is_crit"]:
			return "Critical Success! You perform the action flawlessly."
		return "You succeed."
	else: 
		return f"You fail and take {outcome['damage_taken']} damage."
