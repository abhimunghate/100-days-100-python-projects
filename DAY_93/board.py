from dataclasses import asdict, dataclass

@dataclass
class Shape:
    id: int
    kind: str
    x: int
    y: int
    text: str = ""
    color: str = "black"
    
    def to_dict(self):
        return asdict(self)
    
class Whiteboard:
    def __init__(self, title):
        self.title, self.shapes, self.history = title, [], []
        
    def snapshot(self):
        return [shape.to_dict() for shape in self.shapes]
    
# Done