# Personal Web Guard: AI-Integrated Security Monitor

A modular Python application designed to monitor website health and perform automated security audits using simulated Agentic AI reasoning.

## Project Structure
This project is built using a "modular architecture" to ensure scalability and clean code:

* `main.py`: The orchestrator that manages the monitoring loop.
* `scanner.py`: Handles HTTP networking and latency measurements.
* `security.py`: Performs deep-header inspection for security vulnerabilities.
* `ai_analyst.py`: Simulates an AI Security Agent that provides risk reasoning.
* `requirements.txt`: Lists necessary dependencies for easy setup.



## Key Features
* Health Monitoring: Tracks uptime and response latency for multiple endpoints.
* Security Auditing: Scans for missing HSTS and X-Frame-Options headers to identify protocol downgrade and clickjacking risks.
* AI Reasoning Agent: Leverages a simulated AI "brain" to explain the technical impact of discovered vulnerabilities.
* Automated Logging: Maintains a historical record of security posture and performance.

## 🛠️ Installation & Setup
1. Clone this repository.
2. Install dependencies using the requirements file:
   ```bash
 pip install -r requirements.txt