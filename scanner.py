import requests
import time

def check_health(url):
    """Checks if the site is up and measures response speed."""
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        latency = round(time.time() - start_time, 3)
        return response, latency
    except Exception as e:
        print(f"Connection Error for {url}: {e}")
        return None, 0