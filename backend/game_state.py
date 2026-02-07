from typing import Dict
from uuid import uuid4
import threading


_sessions: Dict[str, dict] = {}
_lock = threading.Lock()


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
    with _lock:
        _sessions[session_id] = create_initial_state()
    return session_id


def get_state(session_id: str):
    """Return the live state dict for a session, or None if not found."""
    return _sessions.get(session_id)


def update_state(session_id: str, state: dict):
    """Replace the stored state for a session. Thread-safe for assignment."""
    with _lock:
        _sessions[session_id] = state


def add_event(state: dict, event: str):
    """Append an event to state's `last_events`, keeping only the last 5.

    This is intentionally tolerant if `last_events` is missing.
    """
    if state is None:
        return
    if "last_events" not in state or not isinstance(state["last_events"], list):
        state["last_events"] = []
    state["last_events"].append(event)
    # keep only most recent 5 events
    state["last_events"] = state["last_events"][-5:]


def delete_session(session_id: str) -> bool:
    """Delete a session. Returns True if removed."""
    with _lock:
        return _sessions.pop(session_id, None) is not None


def list_sessions() -> Dict[str, dict]:
    """Return a shallow copy of the sessions mapping."""
    with _lock:
        return dict(_sessions)