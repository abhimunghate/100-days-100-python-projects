# 🐾 Day 25 - Animal Sound Simulator

Welcome to **Day 25** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line **Animal Sound Simulator** built with Python using **Object-Oriented Programming (OOP)** concepts. It allows users to add different animals, simulate their sounds, remove animals, and play the sound of a randomly selected animal. The project demonstrates **Inheritance**, **Polymorphism**, and object management in Python.

---

## 📌 Project Overview

The application enables users to:

- 🐶 Add different types of animals
- 🎵 Play sounds of all added animals
- 🎲 Play the sound of a random animal
- ❌ Remove animals from the simulator
- 📊 View the total number of animals currently in the simulator

Each animal produces its own unique sound through **method overriding**, showcasing runtime polymorphism.

---

## ✨ Features

- 🐶 Add Dogs
- 🐱 Add Cats
- 🐄 Add Cows
- 🦆 Add Ducks
- 🎵 Play sounds of all animals
- 🎲 Generate a random animal sound
- ❌ Remove animals by name
- 📊 Display the total number of animals
- ✅ Prevent invalid object types
- 🖥️ Simple menu-driven command-line interface

---

## 🛠️ Technologies Used

- Python 3
- `random` Module
- Object-Oriented Programming (OOP)
- Inheritance
- Polymorphism
- Method Overriding

---

## 📂 Project Structure

```text
DAY_25/
│── main25.py
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the application:

```bash
python main25.py
```

---

## 💻 Sample Output

### Main Menu

```text
------ Animal Sound Simulator ------

1. Add Dog
2. Add Cat
3. Add Cow
4. Add Duck
5. Make All Sounds
6. Remove Animal
7. Random Animal Sound
8. Exit
```

---

### Adding Animals

```text
Enter your choice : 1

Dog added successfully.
Total Animals : 1

Enter your choice : 2

Cat added successfully.
Total Animals : 2
```

---

### Playing All Sounds

```text
------ Animal Sounds ------

1. Dog
Woof! Woof!

2. Cat
Meow! Meow!
```

---

### Random Animal Sound

```text
------ Random Animal ------

Random Animal : Cow
Sound : Moo! Moo!
```

---

### Removing an Animal

```text
Enter animal name to remove : Cat

Cat removed successfully.
Remaining Animals : 1
```

---

## 📚 Concepts Practiced

- Object-Oriented Programming (OOP)
- Classes and Objects
- Inheritance
- Polymorphism
- Method Overriding
- Object Composition
- Lists
- Functions
- Conditional Statements
- Loops
- User Input Handling
- Random Selection using `random.choice()`

---

## 🎯 Learning Outcome

This project helped me practice:

- Creating base and derived classes
- Implementing inheritance in Python
- Overriding methods for different behaviors
- Understanding runtime polymorphism
- Managing collections of objects
- Using the `random` module
- Building menu-driven applications
- Writing reusable and organized code

---

## ⚠️ Note

- Only valid animal objects can be added to the simulator.
- Animals can be removed by entering their class name (Dog, Cat, Cow, or Duck).
- Random sound generation requires at least one animal in the simulator.
- Multiple animals of the same type can be added.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- 🐴 Add more animal types
- 🎧 Play real animal sound effects using audio files
- 💾 Save and load animal collections using JSON
- 🖼️ Display ASCII art for each animal
- 🎮 Quiz mode to guess the animal from its sound
- 📊 Track the number of times each sound is played
- 🔍 Search animals by type
- 🏷️ Assign custom names to animals
- 🖥️ GUI version using Tkinter or CustomTkinter
- 🎨 Animated version using Pygame

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀