
import os
from datetime import datetime


class JournalManager:
    FILE = "journal.txt"

    def add_entry(self):
        entry = input("Write your journal entry: ")
        with open(self.FILE, "a") as f:
            f.write(f"{datetime.now()} - {entry}\n")
        print("Entry saved!")

    def view_entries(self):
        try:
            with open(self.FILE, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No entries found.")

    def search_entry(self):
        word = input("Enter keyword or date: ")
        try:
            with open(self.FILE, "r") as f:
                results = [line for line in f if word.lower() in line.lower()]
            print("".join(results) if results else "No match found.")
        except FileNotFoundError:
            print("Journal file not found.")

    def delete_entries(self):
        confirm = input("Delete all entries? (yes/no): ")
        if confirm.lower() == "yes":
            try:
                os.remove(self.FILE)
                print("All entries deleted.")
            except FileNotFoundError:
                print("Journal file not found.")


journal = JournalManager()

while True:
    print("\n--- Personal Journal Manager ---")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Search Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        journal.add_entry()
    elif choice == "2":
        journal.view_entries()
    elif choice == "3":
        journal.search_entry()
    elif choice == "4":
        journal.delete_entries()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
