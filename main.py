from scanner import check_health
from security import run_header_audit
from ai_analyst import get_ai_insights
import time
import sys

SITES = ["https://www.google.com", "https://accenture.com", "https://www.webster.edu"]

def run_guard():
    print("🛡️ Modular Web Guard Starting...")
    print("(Press Ctrl+C to stop at any time)\n")
    
    try:
        while True:
            for url in SITES:
                print(f"--- Scanning: {url} ---")
                resp, speed = check_health(url)
                
                if resp:
                    issues = run_header_audit(resp)
                    insights = get_ai_insights(issues)
                    
                    for line in insights:
                        print(f"🤖 {line}")
                else:
                    print("❌ Site is down.")
            
            print(f"\n⏳ Cycle complete. Next check in 05s...")
            time.sleep(5)
            
    except KeyboardInterrupt:
        # This code runs when you press Ctrl+C
        print("\n\n🛑 Shutdown signal received.")
        print("Cleaning up resources and exiting... Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    run_guard()