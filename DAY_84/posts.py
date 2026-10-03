from dataclasses import asdict, dataclass, field

@dataclass
class Post:
    id: int
    author: str
    title: str
    body: str
    published: bool = False
    comments: list = field(default_factory=list)
    
    def to_dict(self):
        return asdict(self)
    
class PostService:
    def __init__(self):
        self.posts = {}
        
    def create(self, author, title, body):
        post = Post(len(self.posts)+1, author, title, body)
        self.posts[post.id] = post
        return post
    
    def get(self, post_id):
        post = self.posts.get(post_id)
        if not post:
            raise LookupError("Post not found")
        return post
    
    def publish(self, post_id):
        self.get(post_id).published = True
        return self.get(post_id)
    
    def public_posts(self):
        return [p for p in self.posts.values() if p.published]