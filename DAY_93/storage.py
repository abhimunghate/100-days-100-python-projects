import json

class BoardStorage:
    @staticmethod
    def export(board, path="whiteboard.json"):
        data = {"title": board.title, "shapes": board.snapshot()}
        
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
        return {"saved_to": path, "shape_count": len(board.shapes)}
    
# Done