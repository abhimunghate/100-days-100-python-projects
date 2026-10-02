class ContentStorage:
    def __init__(self): 
        self.pages = {}
        
    def next_id(self): 
        return len(self.pages) + 1
    
    def save(self, page): 
        self.pages[page.id] = page
        
    def get(self, page_id): 
        return self.pages.get(page_id)
    
    def all(self): 
        return list(self.pages.values())
    
    def find_by_slug(self, slug): 
        return next((p for p in self.pages.values() if p.slug == slug), None)
    
# Done