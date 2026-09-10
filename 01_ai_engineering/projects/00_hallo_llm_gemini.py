"""
00_hallo_llm.py — Dein erster LLM-API-Call, jetzt mit Google Gemini (kostenlos).

Vorher:
  pip install google-genai python-dotenv
  In die .env eine Zeile:  GEMINI_API_KEY=dein-key-aus-google-ai-studio
  Key holen: https://aistudio.google.com  →  Get API key
  (Die .env NIEMALS committen — steht in .gitignore.)

Starten:
  python 00_hallo_llm.py
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

# .env immer aus dem Ordner laden, in dem dieses Skript liegt
load_dotenv(Path(__file__).parent / ".env")

# --- Key-Check: sauber prüfen, bevor der Call rausgeht ---
key = os.environ.get("GEMINI_API_KEY")
if not key:
    print("⚠️  Kein GEMINI_API_KEY gefunden. Liegt .env im selben Ordner? Richtiger Name?")
    raise SystemExit(1)
print(f"✅ Key geladen (beginnt mit: {key[:6]}...)")

# Client bauen
client = genai.Client(api_key=key)

# Der erste Call.
# - model:   welches Modell (Flash = schnell & im Gratis-Kontingent)
# - contents: deine Nachricht
# - system_instruction: die Rolle (wie der system-Prompt bei Anthropic)
antwort = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Erkläre mir in 2 Sätzen, was eine LLM-API ist.",
    config=types.GenerateContentConfig(
        system_instruction="Du bist ein geduldiger Mentor. Antworte auf Deutsch, kurz und klar.",
        max_output_tokens=1000,
    ),
)

print("\n── Antwort vom Modell ──")
print(antwort.text)

# Senior-Reflex: Token-Verbrauch immer im Blick behalten.
print("\n── Tokens ──")
u = antwort.usage_metadata
print(f"Input:  {u.prompt_token_count}")
print(f"Output: {u.candidates_token_count}")
