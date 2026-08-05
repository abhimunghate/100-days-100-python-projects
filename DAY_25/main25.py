# This is Day 25 project : Animal Sound Simulator

import random

class Animal:
    def make_sound(self):
        print("Some generic animal sound")
        
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")
        
class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")
        
class Cow(Animal):
    def make_sound(self):
        print("Moo! Moo!")
        
class Duck(Animal):
    def make_sound(self):
        print("Quack! Quack!")
        
class AnimalSoundSimulator:
    def __init__(self):
        self.animals = []
        
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.__class__.__name__} added successfully.")
            print(f"Total Animals : {len(self.animals)}")
        else:
            print("Invalid animal type")
            
    def make_all_sounds(self):
        if not self.animals:
            print("No animals in the simulator")
        else:
            print(f"\nTotal Animals : {len(self.animals)}")
            print("\n------ Animal Sounds ------\n")
            for i, animal in enumerate(self.animals, start=1):
                print(f"{i}. {animal.__class__.__name__}")
                animal.make_sound()
                print()
                
    def remove_animal(self, animal_name):
        for animal in self.animals:
            if animal.__class__.__name__.lower() == animal_name.lower():
                self.animals.remove(animal)
                print(f"{animal.__class__.__name__} removed successfully.")
                print(f"Remaining Animals : {len(self.animals)}")
                return
        print("Animal not found.")
    
    def random_sound(self):
        if not self.animals:
            print("No animals in the simulator.")
            return
        animal = random.choice(self.animals)
        print("\n------ Random Animal ------")
        print(f"\nRandom Animal: {animal.__class__.__name__}")
        print("Sound :", end=" ")
        animal.make_sound()
                
simulator = AnimalSoundSimulator()

while True:
    print("\n------ Animal Sound Simulator ------\n")
    print("1. Add Dog")
    print("2. Add Cat")
    print("3. Add Cow")
    print("4. Add Duck")
    print("5. Make All Sounds")
    print("6. Remove Animal")
    print("7. Random Animal Sound")
    print("8. Exit")
    
    choice = input("\nEnter your choice (1-8) : ")
    
    if choice == "1":
        simulator.add_animal(Dog())
    elif choice == "2":
        simulator.add_animal(Cat())
    elif choice == "3":
        simulator.add_animal(Cow())
    elif choice == "4":
        simulator.add_animal(Duck())
    elif choice == "5":
        simulator.make_all_sounds()
    elif choice == "6":
        animal_name = input("\nEnter animal name to remove : ").strip()
        simulator.remove_animal(animal_name)
    elif choice == "7":
        simulator.random_sound()
    elif choice == "8":
        print("\nExiting the simulator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
# Done