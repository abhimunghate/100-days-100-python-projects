from dataclasses import asdict, dataclass
from datetime import datetime, timezone

@dataclass
class Post:
    id: int
    user_id: int
    text: str
    created_at: str
    
    def to_dict(self):
        return asdict(self)
    
class PostService:
    def __init__(self, users):
        self.users, self.posts = users, []
        
    def create(self, user_id, text):
        self.users.get(user_id)
        
        if not text.strip():
            raise ValueError("Post cannot be empty")
        
        post = Post(len(self.posts)+1, user_id, text, datetime.now(timezone.utc).isoformat())
        self.posts.append(post)
        return post
    
# Done