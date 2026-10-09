# This is Day 90 project : URL Shortener Service

import json
from analytics import AnalyticsService
from shortener import ShortenerService

def show(action, result, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(result, indent=2)}")
    
def main():
    print("Day 90 - URL Shortener Service")
    shortener = ShortenerService()
    analytics = AnalyticsService(shortener)
    
    item = shortener.shorten("https://example.com/python/projects/day-90")
    show("SHORTEN URL", {"short_url": f"https://sho.rt/{item.code}", "code": item.code}, 201)
    show("RESOLVE URL", {"redirect_to": shortener.resolve(item.code)}, 302)
    show("GET ANALYTICS", analytics.stats(item.code))
    
if __name__ == "__main__":
    main()
    
# Done