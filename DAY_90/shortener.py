from dataclasses import dataclass
from hashlib import sha256
from urllib.parse import urlparse

@dataclass
class ShortURL:
    code: str
    original_url: str
    clicks: int = 0
    
class ShortenerService:
    def __init__(self):
        self.urls = {}
        
    def shorten(self, original_url):
        parsed = urlparse(original_url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("Valid HTTP or HTTPS URL required")
        code = sha256(original_url.encode()).hexdigest()[:7]
        self.urls.setdefault(code, ShortURL(code, original_url))
        return self.urls[code]
    
    def resolve(self, code):
        item = self.urls.get(code)
        if not item:
            raise LookupError("Short URL not found")
        item.clicks += 1
        return item.original_url
    
# Done