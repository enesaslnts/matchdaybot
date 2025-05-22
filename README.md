# ⚽ MatchdayBot – Der IT-Sicherheits-Coach im Stadion der Container!

> DevSecOps mit Humor – Docker, Trivy, CI/CD, GitHub Actions, ArgoCD & Discord Webhooks

---

## 🧠 Was ist MatchdayBot?

MatchdayBot ist **nicht** einfach ein Bot – er ist dein digitaler **Fußballtrainer**, **Sicherheitsanalyst**, und **Live-Kommentator**, alles in einem!  
Er analysiert Docker-Images auf Schwachstellen mit **Trivy**, kommentiert die Sicherheitslücken wie ein leidenschaftlicher Fußballreporter und liefert dir alles direkt auf **Discord** – formatiert, bunt, dramatisch und absolut verständlich.

---

## ⚙️ Features

- 🛡 **Trivy-Vulnerability-Scan** für Docker-Images (`ghcr.io`)
- 🤖 **Discord-Integration**: Webhook & Bot mit Slash-Commands (`/scan`, `/erkläre`)
- 📊 Tabellenbasierte CVE-Zusammenfassung & Handlungsempfehlungen
- 📣 **Fußball-Metaphern** zur Erklärung von CVEs („Abseitsfalle in der Nachspielzeit!“)
- 💬 CVE-Erklärungen durch **DeepSeek** / GPT-Modelle
- 🔄 CI/CD: Automatischer Build & Deployment mit GitHub Actions & ArgoCD
- 🐳 Vollständig Dockerized & Kubernetes-ready
- 🎭 Humor-Modell (`model_prompt.md`) für unterhaltsame Sicherheitsberichte

---

## 📦 Technologien im Einsatz

| Tool / Framework   | Beschreibung                                                                 |
|--------------------|------------------------------------------------------------------------------|
| `Trivy`            | Scannt deine Docker-Images auf Sicherheitslücken                            |
| `Discord.py`       | Für den interaktiven Discord-Bot mit Slash-Commands                         |
| `Webhooks`         | Automatischer Versand von Scan-Ergebnissen mit Formatierung                 |
| `DeepSeek / OpenAI`| Erklärt CVEs mit verständlicher Sprache und Humor                           |
| `Docker`           | Containerisiert deinen Bot und seine Analyse-Funktionalität                 |
| `Kubernetes`       | Orchestriert die App, deployed mit ArgoCD                                   |
| `GitHub Actions`   | CI-Pipeline zum automatisierten Build & Push auf GitHub Container Registry  |
| `ArgoCD`           | CD-Tool zur kontinuierlichen Auslieferung nach jedem Commit                 |

---

## 🎮 Beispiel: Ein Spieltag auf Discord

```markdown
1. zlib1g (CVE-2023-45853): "Ein Heap-Overflow in der Nachspielzeit – der Gegner schießt durch! 🟥 Tor für die Sicherheit!"
2. libldap-common (CVE-2023-2953): "Ein Pass ins Nichts – NULL-Pointer! Der Gegner kontert und trifft!" 😱⚠️

