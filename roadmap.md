# 🗺️ Roadmap — AI Security (2026-aktuell)

> Recherchiert aus aktuellen 2026-Quellen (Chip Huyen *AI Engineering*, TryHackMe SEC-Zertifizierungspfad, OWASP LLM Top 10, MITRE ATLAS).
> Bei 5–8 Std/Woche realistisch: **~14–16 Monate**. Konsistenz > Tempo.

---

## TEIL 1 · AI ENGINEERING (Monate 1–7)

### Phase A0 — Fundament (Wochen 1–3)
*Du hast Python-Vorerfahrung → hier geht's schnell.*
- Python-Auffrischung: async/await (kritisch für parallele API-Calls), venv, type hints
- Git-Workflow: branches, PRs, commits als Gewohnheit
- Dev-Setup: WSL2, VS Code, `uv` oder `pip`, `.env`-Handling
- **Mini-Projekt:** CLI-Tool, das eine Datei liest und via LLM-API zusammenfasst
- **Eval-Denkweise ab Tag 1:** Woher weißt du, dass die Zusammenfassung *gut* ist?

### Phase A1 — LLM-APIs & Prompt Engineering (Wochen 4–8)
- Anthropic API + OpenAI API: messages, system prompts, tokens, streaming
- Prompt Engineering: few-shot, structured output (JSON), Rollen
- Kosten- & Latenz-Tracking (Senior-Signal!)
- **Portfolio-Projekt 1:** Chatbot *mit Memory* — deploybar, mit Error-Handling
- **Ressourcen:** Anthropic Docs, DeepLearning.AI Short Courses

### Phase A2 — RAG (Wochen 9–16) ⭐ höchstes Interview-Signal
- Embeddings & Vektor-Mathematik (Intuition, nicht PhD)
- Vector DBs: Chroma (lokal starten) → später Pinecone/Qdrant
- Chunking, Retrieval, Re-Ranking
- **Evaluation:** Faithfulness, Relevancy, Context Recall (RAGAS)
- **Portfolio-Projekt 2:** Dokument-Q&A mit Zitaten + Latenz/Kosten-Tracking

### Phase A3 — Agents & MCP (Wochen 17–24)
- ReAct-Loop, Tool-Calling, Function-Calling
- Memory-Systeme für Agents
- **MCP (Model Context Protocol)** — 2026 Enterprise-Standard, wenige beherrschen es → Differenzierung
- FastAPI zum Wrappen · Docker zum Deployen
- **Portfolio-Projekt 3:** Agent, der eine echte Aufgabe löst (Tools sicher aufruft)

### Phase A4 — Production & LLMOps (Wochen 25–28)
- CI-Eval-Gates vor jedem Release
- Observability: Tracing jedes LLM-Calls
- Deployment: Cloud Run / Lambda / Container Apps

---

## TEIL 2 · CYBERSECURITY (Monate 8–13)

### Phase C0 — Fundament (Wochen 29–34)
*Skip NICHT — das trennt "Tool-User" von "Engineer".*
- Netzwerk: OSI, TCP/IP, DNS, DHCP, SSL/TLS, Subnetting
- Linux tiefer: Permissions, SSH, Cron, Bash-Scripting
- Windows: Active Directory Basics, PowerShell, Event Viewer
- Sicherheitskonzepte: CIA-Triade, Risk Management, AES/RSA
- **Plattform:** TryHackMe Pre-Security + SEC0 Pfad

### Phase C1 — Web-Security & OWASP (Wochen 35–42)
- OWASP Top 10: SQLi, XSS, SSRF, IDOR, Broken Access Control
- Tools: Nmap, Wireshark, Burp Suite
- **Plattform:** PortSwigger Web Security Academy (kostenlos, exzellent)
- **Writeups!** Jede Übung → `02_cybersecurity/writeups/`

### Phase C2 — Home Lab & Blue/Red (Wochen 43–50)
- Home Lab: Kali + Windows + Ubuntu VMs
- Angreifen: Nmap-Recon → Metasploit
- Verteidigen: Logs, ELK/Wazuh SIEM, MITRE ATT&CK
- **Attack & Detect:** Greife deine eigene Infra an, finde die Spuren in Logs
- **Plattform:** HackTheBox (realistischer, ungeführt)

---

## TEIL 3 · AI SECURITY (Monate 14–16) — DIE NISCHE

### Phase S1 — LLM-Angriffe
- OWASP LLM Top 10 (Prompt Injection, Insecure Output, Data Poisoning)
- MITRE ATLAS (Adversarial Threat Landscape for AI Systems)
- Übungsplattformen: Gandalf (Lakera), Garak (LLM-Vuln-Scanner)

### Phase S2 — LLM-Verteidigung
- Guardrails, Input/Output-Validierung
- Policy Gateway + Blocked-Action-Logging

### 🏆 FINALE CAPSTONE
Baue einen **RAG-Chatbot** → dann **greife ihn an** → dann **sichere ihn ab**.
Ein Projekt, das beide Disziplinen beweist. Dein Bewerbungs-Trumpf.

---

## 🎓 Job-Bezug (Senior-Level)
Was Hiring Manager 2026 erwarten:
- System-Design & Production-Deployment (nicht nur Demos)
- **Eval-Pipelines, Golden Datasets, LLM-as-a-Judge** ← am meisten unterschätzt
- Kostenoptimierung
- Portfolio auf GitHub, Writeups als Beweis
