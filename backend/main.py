from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from game_state import (
    create_session,
    get_state,
    update_state,
    add_event
)

app = FastAPI()


class GameState(BaseModel):
    location: str
    quest_goal: str
    hp: int
    ac: int
    inventory: List[str]
    last_events: List[str]


class StartResponse(BaseModel):
    session_id: str
    intro: str
    state: GameState


class ActionRequest(BaseModel):
    session_id: str
    action: str


class ActionResponse(BaseModel):
    dm_response: str
    state: GameState


@app.post("/start", response_model=StartResponse)
def start_game():
    session_id = create_session()
    state = get_state(session_id)

    intro_text = (
        "You awaken in a dimly lit tavern. Rain beats softly against the windows, "
        "and a hooded bartender watches you from behind the counter."
    )

    return {
        "session_id": session_id,
        "intro": intro_text,
        "state": state
    }


@app.post("/action", response_model=ActionResponse)
def process_action(req: ActionRequest):
    state = get_state(req.session_id)
    if not state:
        raise HTTPException(status_code=404, detail="Invalid session ID")

    action = req.action.lower()

   
    if "look" in action:
        dm_response = f"You carefully observe the {state['location']}. The air feels tense."
    elif "inventory" in action:
        dm_response = f"You carry: {', '.join(state['inventory'])}."
    elif "drink" in action:
        state["hp"] = min(state["hp"] + 1, 20)
        dm_response = "The ale is bitter, but it restores a bit of strength."
    elif "leave" in action:
        state["location"] = "Foggy Street"
        dm_response = "You step outside into the fog-covered street."
    else:
        dm_response = "You try the action. The world responds subtly."

    add_event(state, f"Player action: {req.action}")
    update_state(req.session_id, state)

    return {
        "dm_response": dm_response,
        "state": state
    }


@app.get("/")
def health():
    return {"status": "Adventure AI backend running"}