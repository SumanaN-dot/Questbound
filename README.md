# Questbound

https://github.com/user-attachments/assets/cac623ef-7f63-4ed6-bdd0-417e67ee4366

Team split (4 people)

Person 1 — Frontend / UI (Brooke)

Deliverables
    •    Landing page: “Start Adventure”
    •    Character creation (simple): name, class, 2–3 stats
    •    Chat-style interface + dice result panel
    •    “Export story” button (download transcript)

Tech: React or plain HTML/CSS/JS

⸻

Person 2 — Backend / Game State (Sumana)

Deliverables
    •    Session state store (in-memory or lightweight DB)
    •    API endpoints:
    •    /start (creates session, returns intro)
    •    /action (takes player action, returns DM response + state)
    •    State model:
    •    location, quest goal
    •    HP, AC, inventory
    •    last 5 events (for continuity)

Tech: Flask/FastAPI or Node/Express

⸻

Person 3 — AI Prompting / DM Brain (Pragna)

Deliverables
    •    System prompt + formatting rules
    •    “DM response schema” (so output is structured)
    •    Safety rails: keep it PG-13, no slurs, no explicit content
    •    A few premade “adventure seeds” (tavern, dungeon, forest)

Goal: make outputs consistent, not random spaghetti.

⸻

Person 4 — Dice + Rules Engine (Yoshna)

Deliverables
    •    Dice roller: d20, d6, advantage/disadvantage
    •    Skill check logic:
    •    DC tiers (10 easy, 15 medium, 20 hard)
    •    Modifiers based on class/stats
    •    Combat mini-system:
    •    Attack roll vs AC
    •    Damage roll
    •    Enemy HP
    •    Item effects (healing potion, torch, lockpick)

Purpose of the Project:

Questbound is an interactive, narrative-driven dungeon-crawler where the players choices shape the story in real time. 

We built a powerful backend that processes player actions using a custom rules engine, and it generates a dynamic story narration using AI.

Tools and Technologies Utilized:

Backend and Game Logic:
- Python 3.13
- FastAPI 
- Uvicorn - ASGI server 
- Custom Rules Engine - resolves dice rolls, difficulty checks, and outcomes 
- session manager - thread-safe in-memory state handling 

AI and Narrative Generation
- Google Gemini API - generates dynamic story narration

Frontend/ integration
- JSON based API, Figma AI

Version Control
- Git and Github 

Challenges we had:
1. Rules Engine not behaving as expected
    Problem: the difficulty values were being overwritten due to multiple if statements. Also the API wasn't getting the narrative story to generate accurately.
    Solution: Take the code step by step and add print statements throughout the blocks of code to see if each segment was working as expected or not. 

2. The main.py file was running as needed and the import statements weren't syncing with the code. The backend connection was crashing and wouldn't run the FASTAPI since it was not registering.
Solution: Modify the import statements and go line by line trying to fix all the FASTAPI statments and match the functions with the ones appearing in the ai_engine.py.
3. Having to recall certain CSS and HTML factors was also challenging at times, however through trial and error with the UI we were able to make the proper adjustments in order to get the pages looking how we wanted them to.  
4. Making the API key private
    At first we added the Gemini API key we were using to the ai_engine.py file on GitHub but we realized that API keys weren't meant to be shared publicly so we had to research how to hide the API key on GitHub while still making a functional app that could access the Gemini API. 
    Solution: We ended up using a .env file for the new private API key and deleting the old compromised API key so it couldn't be used. We had to import the dotenv package to read the API key from the .env file.

Credits and Framework Acknowledgements 
- FastAPI — https://fastapi.tiangolo.com

- Uvicorn — https://www.uvicorn.org

- Google Gemini API — https://ai.google.dev

- Figma AI - https://www.figma.com/make/kHtDLTX8nghEuv6JmcXD6w/AI-Dungeon-Master-Home-Page?p=f&t=VRoCfZvGVJJvsHcN-0 

