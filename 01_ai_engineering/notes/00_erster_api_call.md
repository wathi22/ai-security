# 00 — Der erste API-Call

**Phase:** A0 · **Woche:** 1

## 1. In einem Satz (für ein Kind erklärt)
Eine LLM-API ist eine Telefonnummer, die du anrufst: du sagst deinen Satz, und am anderen Ende antwortet ein sehr belesener Gesprächspartner.

## 2. Alltagsbeispiel
Wie eine Bestellung am Drive-in-Schalter: Du (dein Code) sprichst in die Box (die API),
die Küche (das Modell) bereitet zu, und du bekommst dein Essen (die Antwort) zurück.
Der **system-Prompt** ist wie zu sagen "Bitte vegetarisch" — er setzt die Grundregeln.

## 3. Wie funktioniert es technisch?
- `messages` = der Gesprächsverlauf (user/assistant abwechselnd)
- `system` = die Rolle/Grundhaltung des Modells
- `max_tokens` = Obergrenze für die Antwortlänge
- Antwort kommt als Liste von **Content-Blöcken** → Text mit `block.type == "text"` rausziehen
- `usage.input_tokens` / `output_tokens` = wonach abgerechnet wird → **immer im Blick behalten**

## 4. Wo hakt mein Verständnis noch?
(hier eintragen, was unklar war → evtl. ins Problem-Log)

## 5. Verwandte Notizen
[[01_prompt_engineering]]

## 6. Anki-Karten daraus
- Was ist der system-Prompt?:: Setzt Rolle/Grundregeln des Modells, vor dem Gespräch.
- Wonach rechnet eine LLM-API ab?:: Input- + Output-Tokens.
