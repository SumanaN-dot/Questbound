# Questbound

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
