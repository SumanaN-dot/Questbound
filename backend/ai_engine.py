import google.generativeai as genai
import os

# Setup Gemini with your API Key
# You can get a key at https://aistudio.google.com/
genai.configure(api_key="AIzaSyBuU-AsE0HOr1RsK0btvBEXW_wgmiSyFkc")

class AIEngine:
    @staticmethod
    def generate_story(player_name, action, roll, outcome):
        # We use Gemini 1.5 Flash - it's fast and perfect for games
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        system_instructions = "You are a classic D&D Dungeon Master. Be descriptive but brief (max 3 sentences)."
        
        # We combine the game data into a clear prompt for Gemini
        user_content = f"""
        Context for the story:
        - Player Name: {player_name}
        - Action Attempted: {action}
        - Dice Roll Result: {roll}
        - Success: {outcome['success']}
        - Damage Taken: {outcome['damage_taken']}
        - Critical Hit: {outcome.get('is_crit', False)}
        
        Based on these stats, narrate the outcome of the action.
        """

        # In Gemini, we can send the system instruction and user content together
        response = model.generate_content(
            f"{system_instructions}\n\n{user_content}"
        )
        
        return response.text