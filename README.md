# Text based game in Python
A simple text based game made in Python with Anisble and Batchfile for automatic instalaltion of Python and Python dependencies

## Requirements

- **Python 3.12.10 or lower**
- **Colorama**
> **Note:** pygame references in the code are currently unused/commented out. Only `colorama` is required to run the game.

---

## Getting Started
 
### Linux / macOS - Ansible
 
The included `setup.yml` playbook checks for Python and `colorama`, installs them if missing, and launches the game automatically.
 
**1. Install Ansible:**
 
| OS | Command |
|----|---------|
| macOS | `brew install ansible` |
| Ubuntu/Debian | `sudo apt install ansible` |
| Other Linux | `pip3 install ansible` |
 
**2. Run the playbook:**
 
```bash
ansible-playbook setup.yml
```

---
 
### Windows - Batch Script
 
The `install.bat` script checks for Python, installs `colorama`, and launches the game. It does **not** install Python itself.
 
**1. Make sure Python 3 is installed.**
If not, download it from [python.org/downloads](https://www.python.org/downloads/).
 
**2. Run the script:**
 
```bat
.\install.bat
```
 
---
 
### Manual Setup (python dependencies only)
 
If you'd rather run things yourself:
 
```bash
# Install the dependency
pip install colorama
# or, for a specific Python version:
py -3.12 -m pip install colorama
 
# Launch the game
python3 game.py
```
