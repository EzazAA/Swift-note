

![Swift Note](https://github.com/user-attachments/assets/cae045ff-3412-4f46-8d1a-7b980ce36c6d)


---
<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python Version">
  </a>
  <a href="https://hacktoberfest.com">
    <img src="https://img.shields.io/badge/hacktoberfest-green" alt="Python Version">
  </a>
  <img src="https://img.shields.io/github/issues/EzazAA/Swift-Note" alt="Issues">
  <img src="https://img.shields.io/github/forks/EzazAA/Swift-Note" alt="Forks">
</p>


Swift-Note is a lightweight command-line application designed to take quick notes, review them, and delete them when needed. It's a simple yet effective tool for organizing your thoughts, tracking ideas, or keeping short reminders.

## Features

- **Create Notes**: Add notes with a category, name, and
body.
- **Review Notes**: List all notes neatly organized in a tabular format.
- **Delete Notes**: Remove notes by name or ID if multiple notes share the same name.
- **Unique Note Naming**: Automatically generates unique names for notes within the same category.
- **SQLite Database**: Persistent storage of notes in a local SQLite database.
- **Colorful Output**: Uses `Colorama` for a better terminal experience.

## Installation

### Prerequisites

- Python 3.8 or higher
- colorama and tabulate

```bash
pip install colorama tabulate
```

### Clone the Repository

```bash
git clone https://github.com/EzazAA/Swift-Note.git
cd Swift-Note
```

## Usage

1. Run the Swift-Note CLI application:

```bash
python swift_note.py
```

2. You'll be greeted with a menu to perform the following actions:

- **Create**: Add a new note.
- **Review**: List all notes in a table format.
- **Delete**: Remove notes by name or ID.
- **Exit**: Quit the application.

### Commands

- **Create a Note**: Input the category, name, and body of the note. If a note with the same name exists in the category, it will generate a unique name.
- **Review Notes**: Displays all stored notes in a tabular format with their category, name, and body.
- **Delete a Note**: Remove a note by entering its name. If multiple notes exist with the same name, you'll be prompted to choose by ID.

### Screenshot
![Command Prompt - powershell 01-10-2024 3 20 03 PM](https://github.com/user-attachments/assets/21bd52c5-ae6e-4053-96cb-934822c1a8e1)

### Project Structure

```
Swift-Note/
│
├── Src/
|   ├──main.py
|   ├──SwiftNote-database.db
├── README.md               # Project documentation
```

## Contributing

Contributions are welcome! Feel free to submit a Pull Request or open an Issue if you encounter any bugs or have suggestions.
Not only code, if you can update the documentation that would be very helpful.
#Hacktoberfest special project
Thanks

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

