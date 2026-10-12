# 📝 Day 93 - Virtual Whiteboard App

Welcome to **Day 93** of my **100 Days, 100 Python Projects** challenge!

This project is a **Virtual Whiteboard App** built using Python. It demonstrates how a virtual whiteboard can manage different shapes, update their positions, maintain a history of board states, undo previous changes, and export board data to a JSON file.

The application uses Python dataclasses, object-oriented programming, lists, dictionaries, file handling, and JSON serialization to implement a simple whiteboard management system. It simulates API-style requests and responses through formatted JSON output in the terminal.

The whiteboard is titled **Sprint Planning** and contains two shapes: a yellow note for defining an API contract and a blue rectangle for building a service. The application moves the first shape, displays the updated board, and exports its current state to a JSON file.

---

## 📌 Project Overview

A virtual whiteboard allows users to organize ideas, create notes, arrange shapes, and plan tasks visually. It is commonly useful for brainstorming, sprint planning, team collaboration, and project organization.

This project demonstrates the backend logic of a virtual whiteboard without requiring a web server or graphical user interface.

The application follows a simple workflow:

- 🖼️ Create a whiteboard with a title.
- 📝 Add shapes such as notes, rectangles, circles, and lines.
- 📍 Assign coordinates to each shape.
- 🎨 Store text and color information for shapes.
- 🔄 Move existing shapes to new positions.
- 📸 Capture snapshots of the board before modifications.
- ↩️ Undo the most recent recorded change.
- 📋 Display the current board state.
- 💾 Export board information to a JSON file.
- 📊 Display operation results in a formatted JSON structure.

**Note:** This is a terminal-based backend simulation. It does not currently provide a live website, interactive drawing canvas, drag-and-drop functionality, database, or real HTTP endpoints.

---

## ✨ Features

- 🖼️ Virtual whiteboard backend simulation
- 🏷️ Custom whiteboard title
- 📝 Shape creation and management
- 🔷 Support for notes, rectangles, circles, and lines
- 📍 Coordinate-based shape positioning
- 🎨 Shape text and color properties
- 🔄 Shape movement functionality
- 📸 Board-state snapshots
- ↩️ Undo functionality for recorded changes
- 🔍 Shape lookup by ID
- ⚠️ Validation of supported shape types
- 🚨 Error handling for missing shapes
- 🧾 JSON file export
- 📊 Shape count reporting
- 📋 API-style request and response formatting
- 🧩 Modular Python project structure
- 🐍 Python standard-library implementation

---

## 🧱 Whiteboard Shape Model

The `Shape` dataclass in `board.py` defines the structure of an individual whiteboard object.

```python
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
```

### Attributes

| Attribute | Description |
|---|---|
| `id` | Unique identifier assigned to a shape within the current board |
| `kind` | Shape type, such as `note` or `rectangle` |
| `x` | Horizontal coordinate of the shape |
| `y` | Vertical coordinate of the shape |
| `text` | Text associated with the shape |
| `color` | Color assigned to the shape |

### Example Shape

The application creates a yellow note using:

```python
commands.add(
    "note",
    120,
    80,
    "Define API contract",
    "yellow"
)
```

The resulting shape has the following properties:

```json
{
  "id": 1,
  "kind": "note",
  "x": 120,
  "y": 80,
  "text": "Define API contract",
  "color": "yellow"
}
```

The `to_dict()` method uses Python's `asdict()` function to convert the dataclass instance into a dictionary. This makes the shape's data easier to display and serialize as JSON.

---

## 📋 Whiteboard Class

The `Whiteboard` class manages the main information associated with the board.

```python
class Whiteboard:
    def __init__(self, title):
        self.title, self.shapes, self.history = title, [], []

    def snapshot(self):
        return [shape.to_dict() for shape in self.shapes]
```

When a whiteboard is initialized, it stores three main properties:

- `title` — the name of the whiteboard.
- `shapes` — a list containing the current shape objects.
- `history` — a list of snapshots recorded before modifications.

The application creates the board using:

```python
board = Whiteboard("Sprint Planning")
```

### Responsibilities

- Maintain the board title.
- Store the current shapes.
- Provide a snapshot of the board's current state.
- Maintain a history of earlier states for undo operations.

### The `snapshot()` Method

The `snapshot()` method converts every shape into a dictionary and returns a list of those dictionaries.

```python
def snapshot(self):
    return [shape.to_dict() for shape in self.shapes]
```

For example, if the board contains two shapes, the snapshot contains two dictionaries describing their IDs, types, positions, text, and colors.

The snapshot creates new dictionaries containing the current shape data. This is important because historical board states should not change when the original shape objects are modified later.

---

## 🛠️ BoardCommands Class

The `BoardCommands` class in `commands.py` implements the operations that modify the whiteboard.

```python
from board import Shape

class BoardCommands:
    def __init__(self, board):
        self.board = board
```

It receives a `Whiteboard` object and uses it to add shapes, move shapes, and undo recorded changes.

The class contains three main methods:

1. `add()` — creates and adds a shape.
2. `move()` — changes the position of an existing shape.
3. `undo()` — restores the most recently recorded board state.

This separation keeps the whiteboard's data model independent from the operations performed on it.

---

## ➕ Adding Shapes

The `add()` method creates a new shape and appends it to the board.

```python
def add(self, kind, x, y, text="", color="black"):
    if kind not in {"note", "rectangle", "circle", "line"}:
        raise ValueError("Unsupported shape type")

    self.board.history.append(self.board.snapshot())

    shape = Shape(
        len(self.board.shapes) + 1,
        kind,
        x,
        y,
        text,
        color
    )

    self.board.shapes.append(shape)
    return shape
```

### How It Works

1. Check whether the requested shape type is supported.
2. Save a snapshot of the board before making the change.
3. Generate an ID using the current number of shapes plus one.
4. Create a `Shape` object with the supplied properties.
5. Append the shape to the board.
6. Return the newly created shape.

### Supported Shape Types

| Shape Type | Purpose |
|---|---|
| `note` | Represents a text note or planning item |
| `rectangle` | Represents a rectangular shape |
| `circle` | Represents a circular shape |
| `line` | Represents a line element |

The current implementation stores shape metadata only. It does not render these shapes visually.

### Example

```python
commands.add(
    "rectangle",
    360,
    80,
    "Build service",
    "blue"
)
```

The application assigns ID `2` to this rectangle because the note was created first.

**Important:** The current ID-generation approach uses the number of existing shapes plus one. If shapes are removed in a future implementation, this approach would need to be updated to avoid possible duplicate IDs.

---

## 📍 Moving Shapes

The `move()` method updates the coordinates of an existing shape.

```python
def move(self, shape_id, x, y):
    shape = next(
        (s for s in self.board.shapes if s.id == shape_id),
        None
    )

    if not shape:
        raise LookupError("Shape not found")

    self.board.history.append(self.board.snapshot())
    shape.x, shape.y = x, y
    return shape
```

### How It Works

1. Search the board for a shape matching the specified ID.
2. Raise a `LookupError` if the shape does not exist.
3. Save the current board state in the history list.
4. Update the shape's `x` and `y` coordinates.
5. Return the updated shape.

### Example

```python
commands.move(1, 160, 140)
```

Before the operation, the first shape is positioned at:

```text
X: 120
Y: 80
```

After the operation, its position becomes:

```text
X: 160
Y: 140
```

The shape retains its ID, type, text, and color. Only its coordinates change.

The application records the previous board state before moving the shape, allowing the movement to be undone.

---

## ↩️ Undo Functionality

The `undo()` method restores the most recently recorded board snapshot.

```python
def undo(self):
    if not self.board.history:
        raise ValueError("Nothing to undo")

    previous = self.board.history.pop()

    self.board.shapes = [
        Shape(**item) for item in previous
    ]

    return self.board.snapshot()
```

### How It Works

1. Check whether the history list contains any previous states.
2. Raise a `ValueError` if there is nothing to undo.
3. Remove the latest snapshot from the history list.
4. Reconstruct the shapes from the saved dictionaries.
5. Replace the current shape list with the restored shapes.
6. Return a snapshot of the restored board.

### Example Scenario

Suppose the board initially contains one note at `(120, 80)`.

- Add a rectangle: the original board state is saved.
- Move the note: the state containing both shapes is saved.
- Undo once: the board returns to the state before the note was moved.
- Undo again: the board returns to the state before the rectangle was added.

The current `main93.py` does not call `undo()` during its demonstration, but the functionality is implemented in `commands.py`.

**Limitation:** The history records board snapshots before adding or moving shapes. There is no redo functionality, and undo history is not saved to disk. Restoring a snapshot also reconstructs the shape objects, so references held elsewhere to the old shape objects will not point to the restored objects.

---

## 📸 Board Snapshot and State Management

A snapshot represents the board at a particular point in time.

For example, after the application creates two shapes and moves the first shape, the current board snapshot contains data similar to:

```json
[
  {
    "id": 1,
    "kind": "note",
    "x": 160,
    "y": 140,
    "text": "Define API contract",
    "color": "yellow"
  },
  {
    "id": 2,
    "kind": "rectangle",
    "x": 360,
    "y": 80,
    "text": "Build service",
    "color": "blue"
  }
]
```

Snapshots are useful for:

- Displaying the current board state.
- Exporting board data.
- Maintaining undo history.
- Inspecting the results of shape operations.
- Preparing data for a future graphical interface.

The `snapshot()` method does not modify the board. It returns a list of dictionaries representing the current shapes.

---

## 💾 BoardStorage Class

The `BoardStorage` class in `storage.py` handles exporting board data to a JSON file.

```python
import json

class BoardStorage:
    @staticmethod
    def export(board, path="whiteboard.json"):
        data = {
            "title": board.title,
            "shapes": board.snapshot()
        }

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

        return {
            "saved_to": path,
            "shape_count": len(board.shapes)
        }
```

### How It Works

1. Receive the whiteboard object.
2. Collect its title and current shape snapshot.
3. Open the destination file in write mode.
4. Serialize the data into readable JSON.
5. Return the output path and the number of saved shapes.

The default export filename is:

```text
whiteboard.json
```

### Exported Data Structure

The JSON file contains the board title and its shapes.

```json
{
  "title": "Sprint Planning",
  "shapes": [
    {
      "id": 1,
      "kind": "note",
      "x": 160,
      "y": 140,
      "text": "Define API contract",
      "color": "yellow"
    },
    {
      "id": 2,
      "kind": "rectangle",
      "x": 360,
      "y": 80,
      "text": "Build service",
      "color": "blue"
    }
  ]
}
```

This is an illustrative example of the expected exported data after the operations in `main93.py`.

### Export Response

The `export()` method returns a dictionary similar to:

```json
{
  "saved_to": "whiteboard.json",
  "shape_count": 2
}
```

The file is written to the current working directory unless another path is supplied.

**Important:** The export operation saves the current board state, not the board's undo history. The application also does not currently implement an import operation for restoring a board from a previously exported file.

---

## 🧾 API-Style Request and Response Format

The `show()` helper function in `main93.py` displays each operation in a structured format.

```python
def show(action, data, status=200):
    print(
        f"\nREQUEST {action}\n"
        f"RESPONSE {status}\n"
        f"{json.dumps(data, indent=2)}"
    )
```

The function prints:

- The operation label.
- A simulated response status.
- The returned data formatted as JSON.

### Operations Demonstrated

| Operation | Status Label | Purpose |
|---|---:|---|
| `POST /api/shapes` | `201` | Displays the result of adding the note |
| `POST /api/shapes` | `201` | Displays the result of adding the rectangle |
| `PATCH /api/shapes/1` | `200` | Displays the moved shape |
| `GET /api/board` | `200` | Displays the board title and current shapes |
| `POST /api/board/export` | `201` | Displays the JSON export result |

These labels resemble REST API operations, but they are printed by a Python function. The application does not create a real HTTP server, receive network requests, or implement actual API endpoints.

The `PATCH` operation label represents a partial update because the shape's coordinates are changed without replacing its other properties.

---

## 🔄 Complete Application Workflow

The application follows this workflow:

```text
Start Application
        |
        v
Create Whiteboard
        |
        v
Set Title: Sprint Planning
        |
        v
Create BoardCommands
        |
        v
Add Yellow Note
        |
        v
Save Previous Board Snapshot
        |
        v
Add Blue Rectangle
        |
        v
Save Previous Board Snapshot
        |
        v
Move Shape with ID 1
        |
        v
Save Previous Board Snapshot
        |
        v
Update Shape Coordinates
        |
        v
Display Current Board
        |
        v
Export Board to JSON
        |
        v
Display Export Result
```

This workflow demonstrates how the application separates data management, shape operations, history tracking, and file storage.

---

## 🏗️ Project Architecture

The project contains four main Python modules.

```text
                  main93.py
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       board.py   commands.py  storage.py
          |           |           |
          v           v           v
       Shape       Add/Move     JSON Export
       Model        Undo        File Storage
          |
          v
     Whiteboard
          |
          v
   Current Shapes
   and Snapshots
```

### Module Responsibilities

- **`main93.py`** — initializes the whiteboard, adds shapes, moves a shape, displays the board, and exports its data.
- **`board.py`** — defines the `Shape` dataclass and `Whiteboard` class.
- **`commands.py`** — implements shape creation, shape movement, validation, and undo operations.
- **`storage.py`** — exports the whiteboard title and current shapes to a JSON file.

This modular structure keeps the data model, operations, and storage logic separate, making the application easier to maintain and extend.

---

## 🖥️ Example Whiteboard Operations

The following operations are executed in `main93.py`.

### 1. Initialize the Whiteboard

```python
board = Whiteboard("Sprint Planning")
commands = BoardCommands(board)
```

The application creates a whiteboard titled `Sprint Planning` and initializes the command handler.

### 2. Add a Note

```python
commands.add(
    "note",
    120,
    80,
    "Define API contract",
    "yellow"
)
```

The first shape receives ID `1` and starts at coordinates `(120, 80)`.

### 3. Add a Rectangle

```python
commands.add(
    "rectangle",
    360,
    80,
    "Build service",
    "blue"
)
```

The second shape receives ID `2` and starts at coordinates `(360, 80)`.

### 4. Move the First Shape

```python
commands.move(1, 160, 140)
```

The first shape is moved to coordinates `(160, 140)`.

### 5. Display the Current Board

```python
show(
    "GET /api/board",
    {
        "title": board.title,
        "shapes": board.snapshot()
    }
)
```

The output contains the title and the latest state of both shapes.

### 6. Export the Board

```python
show(
    "POST /api/board/export",
    BoardStorage.export(board),
    201
)
```

The application writes the board data to `whiteboard.json` and prints the export information.

---

## 📊 Expected Results

After the application runs successfully, the current board should contain two shapes.

| ID | Type | Position | Text | Color |
|---:|---|---|---|---|
| 1 | `note` | `(160, 140)` | Define API contract | Yellow |
| 2 | `rectangle` | `(360, 80)` | Build service | Blue |

The exported JSON file should contain:

- Board title: `Sprint Planning`
- Shape count: `2`
- Updated coordinates of the first shape
- Original coordinates of the second shape
- Text and color properties for both shapes

The program also displays the simulated API-style responses in the terminal.

---

## 🛠️ Technologies Used

### 🐍 Python

Python is used to implement the whiteboard model, shape operations, history tracking, and data export.

### 🧩 Dataclasses

The `dataclasses` module defines structured shape objects.

```python
from dataclasses import asdict, dataclass
```

The `@dataclass` decorator automatically provides useful methods for the `Shape` class, while `asdict()` converts shape instances into dictionaries.

### 🏗️ Object-Oriented Programming

The project uses classes to separate responsibilities:

- `Shape` — represents an individual shape.
- `Whiteboard` — maintains the board's title and shapes.
- `BoardCommands` — implements operations on the board.
- `BoardStorage` — handles JSON export.

### 📋 Lists

Lists store the current shapes and the history of previous board snapshots.

### 🗂️ Dictionaries

Dictionaries represent shape properties and the board's exported data.

### 🧾 JSON

The `json` module converts Python dictionaries and lists into a readable JSON file and formatted terminal output.

### 📁 File Handling

Python's built-in `open()` function creates or overwrites the JSON export file.

### ⚠️ Exception Handling

The application uses:

- `ValueError` for unsupported shape types and attempts to undo when no history exists.
- `LookupError` when a requested shape cannot be found.

---

## 📦 Requirements

This project uses Python's standard library and does not require any external Python packages.

Check your Python installation:

```bash
python --version
```

### `requirements.txt`

```text
# No external dependencies required.
```

No database, API key, or third-party package installation is needed.

---

## 📂 Project Structure

```text
DAY_93/
│
├── main93.py
├── board.py
├── commands.py
├── storage.py
├── whiteboard.json
├── requirements.txt
└── README.md
```

The `whiteboard.json` file is generated when the program successfully completes its export operation. The `screenshots/` folder is optional and can be created to document the project.

### File Description

| File / Folder | Purpose |
|---|---|
| `main93.py` | Entry point and sample whiteboard workflow |
| `board.py` | Shape dataclass and whiteboard model |
| `commands.py` | Shape creation, movement, and undo functionality |
| `storage.py` | JSON export functionality |
| `whiteboard.json` | Generated file containing exported board data |
| `requirements.txt` | Documents dependency requirements |
| `README.md` | Project documentation |

---

## ▶️ How to Run the Application

### Step 1 — Install Python

Ensure that Python is installed on your computer.

```bash
python --version
```

### Step 2 — Open the Project Directory

Open a terminal in the `DAY_93` folder.

```bash
cd DAY_93
```

### Step 3 — Check the Files

Make sure the following Python files are present:

```text
main93.py
board.py
commands.py
storage.py
```

### Step 4 — Run the Application

Execute the following command:

```bash
python main93.py
```

### Step 5 — Review the Terminal Output

The terminal displays:

- The whiteboard title.
- The response for adding the first shape.
- The response for adding the second shape.
- The response for moving the first shape.
- The current board state.
- The JSON export response.

### Step 6 — Inspect the Exported File

After a successful run, open:

```text
whiteboard.json
```

The file contains the whiteboard title and the current shape data in JSON format.

**Note:** Running the program again in the same directory overwrites the existing `whiteboard.json` file because the export function opens it in write mode.

---

## ⚠️ Important Notes and Limitations

### 1. No Graphical Interface

The current application manages whiteboard data through Python objects. It does not visually draw shapes or provide a canvas.

### 2. No Real-Time Collaboration

The application supports a single in-memory whiteboard. Multiple users cannot connect or collaborate in real time.

### 3. No Actual HTTP API

The request labels are simulated terminal output. The project does not run a web server or expose real endpoints.

### 4. Limited Shape Operations

The application can add shapes, move them, and undo recorded changes. It does not currently support deleting, resizing, rotating, or editing existing shape properties.

### 5. Basic Shape ID Generation

IDs are generated using the number of current shapes plus one. If deletion is added later, a more robust ID-generation method will be necessary.

### 6. No Import Functionality

The project exports board data to JSON but does not load previously exported data back into a whiteboard.

### 7. Undo History Is In-Memory

Snapshots are maintained in a Python list. The history disappears when the program terminates and is not included in the exported JSON file.

### 8. No Redo Functionality

The application supports undo but does not provide a mechanism to redo an undone operation.

### 9. Limited Input Validation

The code validates shape types and shape IDs but does not explicitly validate coordinate types, text lengths, or color formats.

### 10. File Overwriting

The export method uses write mode, so exporting to an existing filename replaces its contents.

### 11. No Database

All board information is maintained in memory until exported. There is no database for persistent board management.

---

## 🧠 Concepts Practiced

This project provides practical experience with:

- Python dataclasses
- Object-oriented programming
- Lists and dictionaries
- Creating and managing objects
- Shape models and board state
- Coordinate-based data management
- Methods and class attributes
- Input validation
- Searching objects by ID
- Generator expressions and `next()`
- List comprehensions
- Dictionary unpacking with `**`
- State snapshots
- Undo operations
- JSON serialization
- File handling
- Static methods
- Exception handling
- Modular programming
- API-style response formatting

---

## 🎯 Learning Outcomes

By building this project, I practiced how to:

- Define structured shape objects using dataclasses.
- Create a whiteboard model with a title and shape collection.
- Add different types of shapes with coordinates, text, and colors.
- Assign IDs to newly created shapes.
- Validate supported shape types.
- Search for shapes by their IDs.
- Update the coordinates of an existing shape.
- Capture snapshots before modifying board data.
- Implement a basic undo mechanism using state history.
- Restore previous states from dictionaries.
- Convert Python objects into dictionaries.
- Export structured data to a JSON file.
- Separate board management, commands, and storage into different modules.
- Handle invalid operations with exceptions.
- Display structured operation results in the terminal.
- Build a foundation for a future graphical whiteboard application.

---

## 🔮 Future Improvements

Possible enhancements for future versions include:

- 🎨 Build an interactive drawing canvas using Tkinter or PyQt.
- 🌐 Develop a browser-based whiteboard using HTML, CSS, JavaScript, and Flask.
- 🖱️ Add drag-and-drop shape movement.
- ➕ Support creating shapes through mouse interactions.
- ✏️ Allow users to edit shape text and properties.
- 🗑️ Add shape deletion.
- 📐 Add shape resizing and rotation.
- 🎨 Provide a color picker and customizable styles.
- ↩️ Improve undo history management.
- 🔁 Implement redo functionality.
- 💾 Add automatic saving.
- 📂 Import previously exported JSON files.
- 🗄️ Store multiple boards in SQLite or PostgreSQL.
- 👤 Add user accounts and authentication.
- 🤝 Enable real-time collaboration using WebSockets.
- 💬 Add comments and annotations.
- 📤 Export boards to PNG, SVG, or PDF.
- 📱 Create a responsive interface for mobile devices.
- 🧪 Add automated unit tests.
- 🔐 Add validation and access controls.
- 🚀 Deploy the application as a web service.

---

## 📅 100 Days, 100 Python Projects

This project is part of my **100 Days, 100 Python Projects** challenge.

The goal of this challenge is to build one Python project every day to strengthen programming fundamentals, improve problem-solving skills, and gain practical software development experience.

**Day 93** focuses on **Virtual Whiteboard Development**, combining shape management, coordinate updates, state snapshots, undo operations, and JSON file export using Python.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍📝