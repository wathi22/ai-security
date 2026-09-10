"""
00_hallo_llm.py — Dein allererster LLM-API-Call.
Woche 1, Samstag. Ziel: eine echte Antwort vom Modell im Terminal sehen.

Vorher:
  pip install anthropic python-dotenv
  Lege eine Datei .env an mit einer Zeile:  ANTHROPIC_API_KEY=dein-key-hier
  (Diese Datei NIEMALS committen — sie steht in .gitignore.)

Starten:
  python 00_hallo_llm.py
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

# .env laden → Key aus Umgebung holen (nie im Code hardcoden!)
load_dotenv()

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# Der erste Call. Denk an ein Gespräch: du sagst was (user),
# das Modell antwortet (assistant). Der "system"-Prompt ist die Rolle.
antwort = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    system="Du bist ein geduldiger Mentor. Antworte auf Deutsch, kurz und klar.",
    messages=[
        {"role": "user", "content": "Erkläre mir in 2 Sätzen, was eine LLM-API ist."}
    ],
)

# Antwort ist eine Liste von Content-Blöcken. Text rausziehen:
print("── Antwort vom Modell ──")
for block in antwort.content:
    if block.type == "text":
        print(block.text)

# Senior-Reflex: immer Kosten/Tokens im Blick behalten.
print("\n── Tokens ──")
print(f"Input:  {antwort.usage.input_tokens}")
print(f"Output: {antwort.usage.output_tokens}")
