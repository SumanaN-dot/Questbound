from google import genai
from dotenv import load_dotenv
import os
import traceback

# Setup Gemini with your API Key
# You can get a key at https://aistudio.google.com/
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

class AIEngine:
    @staticmethod
    def generate_story(player_name, action, roll, outcome):
        try:
            system_instructions = "You are a classic D&D Dungeon Master. Be descriptive but brief (max 2-3 sentences). Make the narrative vary based on the action and outcome."
            
            # We combine the game data into a clear prompt for Gemini
            user_content = f"""
You are narrating a D&D game. The player just attempted an action. Create a unique, vivid response.

- Player Name: {player_name}
- Action Attempted: {action}
- Dice Roll Result: {roll}
- Success: {outcome['success']}
- Damage Taken: {outcome['damage_taken']}
- Critical Hit: {outcome.get('is_crit', False)}

Narrate what happens next based on the action and outcome. Be specific to the action (don't be generic).
If successful, describe a positive outcome. If failed, describe a consequence. If critical hit, describe something dramatic.
            """

            # Generate content using the new google-genai API
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=f"{system_instructions}\n\n{user_content}",
            )
            
            result = response.text.strip()
            if result:
                return result
            else:
                return "The Dungeon Master is silent, as if considering your fate..."
        except Exception as e:
            print(f"AI Engine error: {type(e).__name__}: {str(e)}")
            traceback.print_exc()
            # Return a more informative fallback
            raise