# Auto Text Replacer

The **Auto Text Replacer** is a simple utility that replaces predefined text shortcuts with longer phrases as you type. It runs in the background and allows you to customize your text replacements through a separate file.

## Features

- **Macro Replacement**: Automatically replaces text shortcuts with predefined phrases.
- **User-Friendly UI**: A simple graphical interface for easy interaction.
- **Edit Macros**: Quickly open and edit the macros file from the UI.
- **Real-Time Text Replacement**: Macros are replaced as you type, enhancing productivity.
- **Automatic Macro File Creation**: If the `macros.txt` file is missing, it will be created with default macros.

## Installation

1. Download the latest version of the executable from the [releases](https://github.com/ericjada/MyFirstPythonProjects/releases/tag/v1.0-auto-text-replacer) section.
2. Extract the files to a desired location on your computer.

## Usage

1. Run the `AutoTextReplacer.exe` executable.
2. A window will open, indicating that the macro replacement is running.
3. To edit your text replacements:
   - Click the **Edit Macros** button, which opens the `macros.txt` file in Notepad.
   - Add or modify the macros in the format: `shortcut: replacement`.
4. **Note**: After editing `macros.txt`, you need to restart the application for changes to take effect.

## Requirements

- Windows OS (tested on Windows 11)
- Python (for development; not required for the executable)

## Contributing

Feel free to contribute by creating pull requests or reporting issues in the repository.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to the [keyboard](https://keyboard.readthedocs.io/en/latest/) and [Tkinter](https://docs.python.org/3/library/tkinter.html) libraries for making this project possible.
