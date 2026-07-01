
import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry:\n")
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

            with open(self.filename, "a") as file:  # append mode
                file.write(f"{timestamp}\n{entry}\n\n")

            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied while writing to the file.")

    def view_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("\nNo journal entries found. Start by adding a new entry!")
                return

            with open(self.filename, "r") as file:
                content = file.read()

            if content.strip() == "":
                print("\nNo journal entries found.")
            else:
                print("\nYour Journal Entries:")
                print("----------------------------------")
                print(content)

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
        except Exception:
            print("An unexpected error occurred while reading the file.")

    def search_entry(self):
        try:
            if not os.path.exists(self.filename):
                print("\nError: The journal file does not exist. Please add a new entry first.")
                return

            keyword = input("\nEnter a keyword or date to search: ").lower()

            with open(self.filename, "r") as file:
                lines = file.readlines()

            matches = []
            current_block = []

            for line in lines:
                if line.strip() == "":
                    if current_block:
                        block_text = " ".join(current_block).lower()
                        if keyword in block_text:
                            matches.append("".join(current_block))
                        current_block = []
                else:
                    current_block.append(line)

            if matches:
                print("\nMatching Entries:")
                print("----------------------------------")
                for m in matches:
                    print(m)
            else:
                print(f"\nNo entries were found for the keyword: {keyword}.")

        except Exception:
            print("An unexpected error occurred while searching.")

    def delete_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("\nNo journal entries to delete.")
                return

            confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").lower()

            if confirm == "yes":
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")
            else:
                print("\nDeletion cancelled.")

        except PermissionError:
            print("Error: Permission denied while deleting the file.")
        except Exception:
            print("An unexpected error occurred while deleting the file.")


def main():
    jm = JournalManager()

    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:\n")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nInvalid option. Please select a valid option from the menu.")
            continue

        if choice == 1:
            jm.add_entry()
        elif choice == 2:
            jm.view_entries()
        elif choice == 3:
            jm.search_entry()
        elif choice == 4:
            jm.delete_entries()
        elif choice == 5:
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("\nInvalid option. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()