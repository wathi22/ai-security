# 🚀 SETUP — Schritt 1 (Woche 1, gemeinsam)

Folge dieser Liste **in Reihenfolge**. Haken setzen beim Erledigen.

---

## A) Diesen Vault einrichten (15 Min)

- [x] Diesen Ordner in dein bestehendes `learning-journal`-Repo kopieren
      (oder als neues Repo `ai-security-journey` anlegen)
- [x] **Obsidian** öffnen → "Open folder as vault" → diesen Ordner wählen
- [x] Templates-Plugin in Obsidian aktivieren, Ordner `templates/` als Vorlagen-Quelle setzen

## B) Git-Fundament (10 Min)

```bash
cd ai-security-journey
git init                 # falls neues Repo
git add .
git commit -m "chore: setup learning vault"
# .env NIEMALS committen:
echo ".env" >> .gitignore
echo "*.key" >> .gitignore
git add .gitignore && git commit -m "chore: gitignore secrets"
```

- [x] Repo auf GitHub pushen (via SSH-Key, den du schon hast)

## C) GitHub Projects Board (15 Min) — dein "Jira"

1. [x] Auf GitHub: Repo öffnen → Tab **Projects** → **New project** → Template **Board**
2. [x] Spalten: `Backlog` · `This Week` · `In Progress` · `Done`
3. [x] Erste Issues anlegen (das ist deine Sprint-Planung):
   - [x] `Issue: Erster Anthropic-API-Call (Woche 1)`
   - [x] `Issue: CLI-Summarizer bauen (Woche 2)`
   - [x] `Issue: Prompt Engineering Grundlagen (Woche 3)`
   - [x] `Issue: Chatbot mit Memory starten (Woche 4)`
1. [x] Woche-1-Issue nach `This Week` ziehen

> **Warum GitHub Projects statt Jira?** Es lebt neben deinem Code, kein Context-Switch.
> Die Konzepte (Boards, Issues, Sprints) sind identisch zu Jira — du lernst später in
> 2 Tagen die Jira-UI, wenn ein Arbeitgeber sie nutzt.

## D) API-Zugang (10 Min)

- [x] Anthropic Console → API-Key erstellen → in `.env` speichern (NICHT committen)
- [x] `pip install anthropic python-dotenv` (oder `uv add ...`)

## E) Anki (5 Min)

- [ ] Anki installieren → Deck "AI-Security Befehle" anlegen
- [ ] Erste Karte: `venv aktivieren (Linux/WSL)` :: `source .venv/bin/activate`

---

## ✅ Wenn alles gehakt ist:
Du hast das Fundament eines echten Engineering-Workflows. **Jetzt kommt der erste Code.**
Siehe `01_ai_engineering/notes/00_erster_api_call.md`.
