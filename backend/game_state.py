from typing import Dict, List
from uuid import uuid4


_sessions: Dict[str, dict] = {}

def create_initial_state() -> dict:
    return {
        "location": "Misty Tavern",
        "quest_goal": "Find the missing merchant",
        "hp": 20,
        "ac": 14,
        "inventory": ["Rusty Sword"],
        "last_events": []
    }

def create_session() -> str:
    session_id = str(uuid4())
    _sessions[session_id] = create_initial_state()
    return session_id


def get_state(session_id: str) -> dict | None:
    return _sessions.get(session_id)


def update_state(session_id: str, state: dict):
    _sessions[session_id] = state

def add_event(state: dict, event: str):
    state["last_events"].append(event)
    state["last_events"] = state["last_events"][-5:]