import json
from discord_webhook import send_discord_message

def analyse_scan():
    try:
        with open("trivy_output.json", "r") as f:
            data = json.load(f)

        vulns = data.get("Results", [])[0].get("Vulnerabilities", [])
        if not vulns:
            msg = "✅ Kein Foulspiel entdeckt. Solides Spiel!"
        else:
            msg = "🟥 CVEs entdeckt – Taktikanalyse folgt:\n"
            for v in vulns[:3]:
                msg += f"⚠️ {v['VulnerabilityID']} | {v['PkgName']} | {v['Severity']}\n"

        send_discord_message(msg)

    except Exception as e:
        send_discord_message(f"❌ Fehler in der Analyse: {str(e)}")

if __name__ == "__main__":
    analyse_scan()
