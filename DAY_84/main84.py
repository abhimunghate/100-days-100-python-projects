# This is Day 84 project : Blog Platform

import json
from comments import CommentService
from posts import PostService

def show(action, result, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(result, indent=2)}")
    
def main():
    print("Day 84 - Blog Platform")
    posts = PostService()
    comments = CommentService(posts)
    
    post = posts.create("Maya", "Learning Python", "Build one project each day.")
    show("CREATE POST", post.to_dict(), 201)
    show("PUBLISH POST", posts.publish(post.id).to_dict())
    show("ADD COMMENT", comments.add(post.id, "Leo", "Great advice!"), 201)
    show("LIST POSTS", {"posts": [p.to_dict() for p in posts.public_posts()]})
    
if __name__ == "__main__":
    main()