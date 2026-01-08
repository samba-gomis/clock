# Grandma's Clock
### A simple console python alarm clock
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/release/python-3120/)

```
   ______                     __               _      
  / ____/________ _____  ____/ /___ ___  ____ ( )_____
 / / __/ ___/ __ `/ __ \/ __  / __ `__ \/ __ `/// ___/
/ /_/ / /  / /_/ / / / / /_/ / / / / / / /_/ / (__  ) 
\____/_/___\__,_/_/ /_/\__,_/_/ /_/ /_/\__,_/ /____/  
  / ____/ /___  _____/ /__                            
 / /   / / __ \/ ___/ //_/                            
/ /___/ / /_/ / /__/ ,<                               
\____/_/\____/\___/_/|_|                              
```

**Laplateforme software course project**

Grandma's clock is a simple python console alarm clock. It cans display the time in your console and the time update and runs even when you browse menus. 

> [!WARNING]
> Don't watch it run for too long, you will lose your time.

## Dependencies
- **python3**
- **pip**
  - **keyboard**

# Install

## Commands

Clone the repository locally
```bash
git clone https://github.com/samba-gomis/clock.git
```

If you are familiar with python virtual environments you can activate it and avoid global *keyboard* module installation.

**Windows**
```bash
powershell -ExecutionPolicy ByPass -c .venv/Scripts/Activate.ps1
```
**Linux**
```bash
.venv/Scripts/activate
```

Or you can install the pip dependencies on all your system with
```bash
pip install keyboard
```

## Features

- **Set current time**: You can set the time providing the current hour, minute and second.
- **Display time**: You can display time.
- **Set an alarm**: You can set an alarm providing the alarm hour, minute and second. The clock display a "BEEP BEEP" message when the current time reaches the alarm time.
- **Switch 12H - 24H display**: You can display your time in both modes. For example, 13:04:45 in 24H mode will be displayed 01:04:45 PM in 12H mode.
- **Pause time**: You can pause time when displaying it hitting *spacebar*.


## Setup

When you start the clock, it systematically asks you to set the time.

## Quick Start

1. Run clock:

   ```bash
   py main.py
   ```

2. Set the clock

3. Use numbers to browse the menu

   ## Challenges
- Git merge conflicts

   ## Roadmap
- Use Threading
  - Modify the whole architecture to use threading instead of Tic Toc mechanic
- Add a GUI
  - Make a GUI with tkinter
- Add sound
  - The alarm should play a real alarm sound
  - Add the possibility to select the desired alarm

   ## Authors
  - Childebert Bouaichi
  - Samba Diop Gomis
  - Arthur Georget