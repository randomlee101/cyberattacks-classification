from test import check_severity
from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)
x = ["Accessing Functionality Not Properly Constrained by ACLs", "Buffer Overflow via Environment Variables",
     "Basic Phishing Email for Login Credentials", "Zero-Day Exploit in Critical Infrastructure Control Systems.",
     "Ransomware Attack on Small Business Networks.", "Data Breach in Healthcare System Due to Insider Negligence.",
     "Malware Infection in Corporate Network via Unpatched Vulnerabilities.",
     "Nation-State Cyber Attack Disrupting Power Grid Infrastructure.", "Resource Leak Exposure", "File Discovery",
     "Traffic Injection", "Weakening of Cellular Encryption "]

print(check_severity(x))
# @app.get("/")
# def entry_point():
#     print(request.headers)
#     return "Hello World"
#
#
# if __name__ == "__main__":
#     serve(app, port=3000)
