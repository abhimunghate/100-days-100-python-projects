class CommentService:
    def __init__(self, posts):
        self.posts = posts
        
    def add(self, post_id, name, text):
        post = self.posts.get(post_id)
        if not post.published:
            raise ValueError("Post must be published before comments are accepted")
        
        comment = {"id": len(post.comments)+1, "name": name, "text": text}
        post.comments.append(comment)
        return comment