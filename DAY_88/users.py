from dataclasses import dataclass, field

@dataclass
class User:
    id: int
    name: str
    following: set[int] = field(default_factory=set)
    
class UserService:
    def __init__(self):
        self.users = {1: User(1, "Ava"), 2: User(2, "Noah")}
        
    def get(self, user_id):
        user = self.users.get(user_id)
        if not user:
            raise LookupError("User not found")
        return user
    
    def follow(self, user_id, target_id):
        user, target = self.get(user_id), self.get(target_id)
        
        if user_id == target_id:
            raise ValueError("Users cannot follow themselves")
        
        user.following.add(target_id)
        return {"message": f"{user.name} now follows {target.name}"}
    
# Done