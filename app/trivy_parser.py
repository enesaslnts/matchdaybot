import json

def extract_vulnerabilities(path="trivy_output.json"):
    try:
        with open(path, "r") as file:
            data = json.load(file)
            vulns = []

            for result in data.get("Results", []):
                for vuln in result.get("Vulnerabilities", []):
                    vulns.append({
                        "PkgName": vuln.get("PkgName", "unknown"),
                        "VulnerabilityID": vuln.get("VulnerabilityID", ""),
                        "Severity": vuln.get("Severity", "UNKNOWN"),
                        "FixedVersion": vuln.get("FixedVersion", "N/A"),
                        "Title": vuln.get("Title", "")
                    })

            # Sort by severity
            severity_order = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNKNOWN"]
            return sorted(vulns, key=lambda v: severity_order.index(v["Severity"]))
    except Exception as e:
        print(f"❌ Fehler beim Parsen von Trivy Output: {e}")
        return []
