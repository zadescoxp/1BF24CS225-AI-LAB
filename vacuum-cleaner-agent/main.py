import random
import time


class VacuumCleanerAI:

    def __init__(self):
        # Environment
        self.rooms = {
            "A": random.choice(["Clean", "Dirty"]),
            "B": random.choice(["Clean", "Dirty"])
        }

        # Starting position
        self.position = random.choice(["A", "B"])

    def show_environment(self):
        print("\n----------------------------")
        print(f"Room A: {self.rooms['A']}")
        print(f"Room B: {self.rooms['B']}")
        print(f"Vacuum position: {self.position}")
        print("----------------------------")

    def sense(self):
        """AI senses the current room."""
        return self.rooms[self.position]

    def decide_action(self):
        """AI decides what to do based on what it senses."""

        current_room = self.sense()

        if current_room == "Dirty":
            return "Suck"

        # Current room is clean, so move to the other room
        if self.position == "A":
            return "Move Right"
        else:
            return "Move Left"

    def perform_action(self, action):

        if action == "Suck":
            print("🧹 AI: Cleaning the room...")
            self.rooms[self.position] = "Clean"

        elif action == "Move Right":
            print("➡️ AI: Moving from A to B...")
            self.position = "B"

        elif action == "Move Left":
            print("⬅️ AI: Moving from B to A...")
            self.position = "A"

    def is_clean(self):
        return (
            self.rooms["A"] == "Clean"
            and self.rooms["B"] == "Clean"
        )

    def run(self):

        print("🤖 AI Vacuum Cleaner Started!")

        while not self.is_clean():

            self.show_environment()

            # 1. Sense
            current_state = self.sense()
            print(f"AI senses: {current_state}")

            # 2. Decide
            action = self.decide_action()
            print(f"AI decides: {action}")

            # 3. Act
            self.perform_action(action)

            time.sleep(1)

        self.show_environment()

        print("\n✅ All rooms are clean!")
        print("🤖 AI Vacuum Cleaner Finished!")


# Create AI
vacuum = VacuumCleanerAI()

# Start AI
vacuum.run()
