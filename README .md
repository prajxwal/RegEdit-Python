# WinReg-Python-Utils

WinReg-Python-Utils is a Python script for interacting with the Windows Registry. This utility simplifies tasks such as creating, reading, and deleting registry keys and values under the HKEY_CURRENT_USER hive.

## Features

- Easily manage application settings in the Windows Registry.
- Set or remove startup configurations.
- Python script example for Windows Registry operations.
- Suitable for system administrators and developers.

## Usage

1. Clone or download the repository.
2. Run the `winreg_utils.py` script to perform Windows Registry operations.
3. Follow the prompts to create, read, delete keys/values, or the whole registry subkey.

## Example
```python
Add a new startup setting
set_value("startup", "1")

Read the startup setting
value = get_value("startup")
print("Startup setting:", value)

Delete the startup setting
delete_value("startup")

Delete the whole registry subkey
delete_subkey()
``` 
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Prajwal J

