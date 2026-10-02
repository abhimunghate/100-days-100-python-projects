from dataclasses import asdict, dataclass

@dataclass
class Page:
    id: int
    title: str
    slug: str
    body: str
    status: str = "draft"
    def to_dict(self): return asdict(self)
    
class ContentManager:
    def __init__(self, storage): 
        self.storage = storage
        
    def create(self, title, slug, body):
        if not title or not slug: 
            raise ValueError("Title and slug are required")
        
        if self.storage.find_by_slug(slug): 
            raise ValueError("Slug already exists")
        
        page = Page(self.storage.next_id(), title, slug, body); self.storage.save(page); return page
    
    def publish(self, page_id):
        page = self.storage.get(page_id)
        if not page: 
            raise LookupError("Page not found")
        
        page.status = "published"; return page
        
    def published(self): 
        return [p for p in self.storage.all() if p.status == "published"]
    
# Done