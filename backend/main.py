
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import traceback

import rules_engine
import game_state
from ai_engine import AIEngine


class ActionRequest(BaseModel):
	player_name: str
	action: str
	roll: int | None = None


app = FastAPI(title="Questbound API")

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/health")
def health():
	return {"status": "ok"}


@app.post("/session")
def create_session():
	session_id = game_state.create_session()
	state = game_state.get_state(session_id)
	return {"session_id": session_id, "state": state}


@app.get("/session/{session_id}")
def get_session(session_id: str):
	state = game_state.get_state(session_id)
	if state is None:
		raise HTTPException(status_code=404, detail="Session not found")
	return {"session_id": session_id, "state": state}


@app.post("/session/{session_id}/action")
def perform_action(session_id: str, req: ActionRequest):
	state = game_state.get_state(session_id)
	if state is None:
		raise HTTPException(status_code=404, detail="Session not found")

	# Resolve using the rules engine
	try:
		outcome = rules_engine.resolve_action(state, req.action, req.roll)
	except Exception as e:
		print(f"Rules engine error: {e}")
		raise HTTPException(status_code=500, detail="Rules engine error")

	# Apply outcome to state
	hp_before = state.get("hp", 0)
	hp_after = max(0, hp_before - outcome.get("damage_taken", 0))
	state["hp"] = hp_after

	# Record event
	event_text = f"{req.player_name} attempts: {req.action} (roll {outcome.get('roll')}) -> { 'SUCCESS' if outcome['success'] else 'FAIL' }"
	rules_engine_desc = rules_engine.describe_outcome(outcome)
	game_state.add_event(state, event_text + " -- " + rules_engine_desc)

	# Try to generate a short narrative via AI; if it fails, use rules engine fallback
	narrative = None
	try:
		print(f"Calling AI Engine for action: {req.action}")
		narrative = AIEngine.generate_story(req.player_name, req.action, outcome.get("roll"), outcome)
		print(f"AI returned: {narrative[:100]}...")
	except Exception as e:
		# don't crash if AI fails; use rules engine description as fallback
		print(f"AI Engine failed ({type(e).__name__}), using rules engine fallback: {e}")
		narrative = rules_engine_desc

	# Save updated state
	game_state.update_state(session_id, state)

	return {
		"session_id": session_id,
		"state": state,
		"outcome": outcome,
		"narrative": narrative,
	}


if __name__ == "__main__":
	try:
		uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
	except Exception:
		print("Failed to start server")
		traceback.print_exc()
