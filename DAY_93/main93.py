# This is Day 93 project : Virtual Whiteboard App

import json
from board import Whiteboard
from commands import BoardCommands
from storage import BoardStorage

def show(action, data, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(data, indent=2)}")
    
def main():
    print("Day 93 - Virtual Whiteboard App")
    board = Whiteboard("Sprint Planning")
    commands = BoardCommands(board)
    
    show(
        "POST /api/shapes",
        commands.add("note", 120, 80, "Define API contract", "yellow").to_dict(),
        201
    )
    show(
        "POST /api/shapes",
        commands.add("rectangle", 360, 80, "Build service", "blue").to_dict(),
        201
    )
    show("PATCH /api/shapes/1", commands.move(1, 160, 140).to_dict())
    show("GET /api/board", {"title": board.title, "shapes": board.snapshot()})
    show("POST /api/board/export", BoardStorage.export(board), 201)
    
if __name__ == "__main__":
    main()
    
# Done