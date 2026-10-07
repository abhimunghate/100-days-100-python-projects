class FeedService:
    def __init__(self, users, posts):
        self.users, self.posts = users, posts
        
    def get(self, user_id):
        user = self.users.get(user_id)
        visible = user.following | {user_id}
        return [p for p in reversed(self.posts.posts) if p.user_id in visible]
    
# Done