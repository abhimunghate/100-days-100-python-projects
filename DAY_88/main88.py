# This is Day 88 project : Social Media Backend

import json
from feed import FeedService
from posts import PostService
from users import UserService

def show(action, result, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(result, indent=2)}")
    
def main():
    print("Day 88 - Social Media Backend")
    users = UserService()
    posts = PostService(users)
    feed = FeedService(users, posts)
    
    show("FOLLOW USER", users.follow(1, 2))
    show("CREATE POST", posts.create(2, "Shipping my Python project today!").to_dict(), 201)
    show("GET FEED", {"posts": [p.to_dict() for p in feed.get(1)]})
    
if __name__ == "__main__":
    main()
    
# Done