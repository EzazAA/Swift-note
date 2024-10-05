import sqlite3
from colorama import Fore, Style, init
from tabulate import tabulate

# Initialize Colorama
init(autoreset=True)

# Connect to SQLite database
conn = sqlite3.connect('SwiftNote-database.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS Swiftnote (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                category TEXT, 
                name TEXT, 
                body TEXT
            )''')
conn.commit()

def get_unique_note_name(category, note_name):
    """
    Ensure that note names are unique by adding an incrementer if needed.
    """
    c.execute("SELECT name FROM Swiftnote WHERE category = ? AND name LIKE ?", (category, f"{note_name}%"))
    existing_names = [row[0] for row in c.fetchall()]

    if note_name not in existing_names:
        return note_name
    else:
        # Find the next available increment for the note name
        i = 1
        new_note_name = f"{note_name} ({i})"
        while new_note_name in existing_names:
            i += 1
            new_note_name = f"{note_name} ({i})"
        return new_note_name

# Function to create a new note
def create_note():
    note_category = input(Fore.LIGHTYELLOW_EX + "Enter the category of the note: " + Style.RESET_ALL).strip()
    note_name = input(Fore.LIGHTYELLOW_EX + "Enter the name of the note: " + Style.RESET_ALL).strip()
    note_body = input(Fore.LIGHTYELLOW_EX + "Enter the body of the note: " + Style.RESET_ALL).strip()

    # Ensure the note name is unique within the category
    unique_note_name = get_unique_note_name(note_category, note_name)

    # Insert the new note
    c.execute("INSERT INTO Swiftnote (category, name, body) VALUES (?, ?, ?)", 
              (note_category, unique_note_name, note_body))
    print(Fore.LIGHTGREEN_EX + f"New note '{unique_note_name}' added to category '{note_category}'!" + Style.RESET_ALL)

    # Commit changes to the database
    conn.commit()

# Function to review existing notes
def review_notes():
    c.execute("SELECT category, name, body FROM Swiftnote")
    notes = c.fetchall()

    if not notes:
        print(Fore.LIGHTRED_EX + "Nothing here, start taking notes to fill it up!" + Style.RESET_ALL)
    else:
        # Display notes in a table format
        headers = ["Category", "Note Name", "Note Body"]
        print(Fore.LIGHTCYAN_EX + tabulate(notes, headers=headers, tablefmt="fancy_grid") + Style.RESET_ALL)

# Function to delete a note by name
def delete_note():
    note_name = input(Fore.LIGHTYELLOW_EX + "Enter the name of the note to delete: " + Style.RESET_ALL).strip()

    # Check if the note exists
    c.execute("SELECT id, name FROM Swiftnote WHERE name = ?", (note_name,))
    notes_found = c.fetchall()

    if not notes_found:
        print(Fore.LIGHTRED_EX + f"No note found with the name '{note_name}'!" + Style.RESET_ALL)
    else:
        # If multiple notes with the same name exist, list them for clarification
        if len(notes_found) > 1:
            print(Fore.LIGHTYELLOW_EX + "Multiple notes found with that name. Please choose one:" + Style.RESET_ALL)
            for note in notes_found:
                print(f"ID: {note[0]}, Name: {note[1]}")

            # Ask the user to specify the ID of the note they want to delete
            note_id = input(Fore.LIGHTYELLOW_EX + "Enter the ID of the note you want to delete: " + Style.RESET_ALL).strip()

            # Delete the note by ID
            c.execute("DELETE FROM Swiftnote WHERE id = ?", (note_id,))
        else:
            # If only one note matches, delete it directly
            c.execute("DELETE FROM Swiftnote WHERE name = ?", (note_name,))

        # Commit the changes
        conn.commit()
        print(Fore.LIGHTGREEN_EX + f"Note '{note_name}' has been deleted!" + Style.RESET_ALL)

# Function to start the CLI
def start_cli():
    print(Fore.LIGHTYELLOW_EX + "Welcome to Swift-Note!" + Style.RESET_ALL)
    print("An app to take quick notes, review them, and change them.\n" + "=" * 70)
    
    while True:
        task = input(Fore.LIGHTBLUE_EX + "What would you like to do? (create/review/delete/exit): " + Style.RESET_ALL).strip().lower()
        
        if task == "create":
            create_note()
        elif task == "review":
            review_notes()
        elif task == "delete":
            delete_note()
        elif task == "exit":
            print(Fore.LIGHTYELLOW_EX + "Exiting Swift-Note. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.LIGHTRED_EX + "Invalid input, please enter 'create', 'review', 'delete', or 'exit'." + Style.RESET_ALL)

# Run the CLI
if __name__ == "__main__":
    start_cli()

# Close the connection when done
conn.close()
