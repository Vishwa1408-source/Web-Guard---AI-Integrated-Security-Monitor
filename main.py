from scanner import check_health
from security import run_header_audit
from ai_analyst import get_ai_insights
import time

SITES = ["https://www.acer.com", "https://www.webster.edu"]

def run_guard():
    print("🛡️ Modular Web Guard Starting...")
    while True:
        for url in SITES:
            print(f"\n--- {url} ---")
            resp, speed = check_health(url)
            
            if resp:
                issues = run_header_audit(resp)
                insights = get_ai_insights(issues)
                
                for line in insights:
                    print(f"🤖 {line}")
            else:
                print("❌ Site is down.")
        
        print("\n⏳ Next check in 02s...")
        time.sleep(2)

if __name__ == "__main__":
    run_guard()