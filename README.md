# GIT Converter

Author: Alon Gritsovsky

Welcome to GIT Converter! This script allows you to convert a Power Test Campaign and its associated tests and procedures to a new location.

## Usage

1. Run the script `git_converter.py` in your Python environment.

2. Enter the project name: Provide a name for your project.

3. Enter the campaign path: Provide the file path of the Power Test Campaign you want to convert.

4. The script will create a new folder for the project and copy the campaign, tests, and procedures to their respective locations within the project folder.

5. The script will replace the file paths in the campaign file, test files, and procedure files to reflect the new locations.

6. Once the process is complete, you will see a success message.

## Requirements

- Python 3.5 or above
- `xml.etree.ElementTree` module

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to use and modify the script according to your needs.

## Author
Alon Gritsovsky
