# utils.py

import re

OFFENSIVE_WORDS = [
    "ugly", "stupid", "kill", "loser", "hate", "terrorist", "abuse", "idiot",
    "cunt", "nigger", "whore", "slut", "dick", "motherfucker", "shit", "faggot",
    "asshole", "pissed", "wanker", "moron", "fuck", "die", "bastard", "bitch",
    "rape", "rapist"
]

def detect_and_replace_offensive(text, replacement='X'):
    # Regular expression pattern to match offensive words
    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in OFFENSIVE_WORDS) + r')\b', re.IGNORECASE)
    return pattern.sub(replacement, text)
