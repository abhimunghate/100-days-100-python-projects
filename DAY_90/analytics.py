class AnalyticsService:
    def __init__(self, shortener):
        self.shortener = shortener
        
    def stats(self, code):
        item = self.shortener.urls.get(code)
        if not item:
            raise LookupError("Short URL not found")
        return {"code": item.code, "original_url": item.original_url, "clicks": item.clicks}
    
# Done