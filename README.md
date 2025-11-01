# CPU Usage Menu Bar App for macOS

This is a simple macOS menu bar application that displays live CPU usage, updating every second.

## Features
- Shows current CPU usage in the menu bar
- Updates every 1 second
- Lightweight and easy to use

## Requirements
- macOS
- Python 3.8+
- [psutil](https://pypi.org/project/psutil/)
- [rumps](https://pypi.org/project/rumps/)
- [py2app](https://pypi.org/project/py2app/) (for packaging as a .app)

## Installation & Usage

### 1. Run as a Python Script
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   python cpu_tray.py
   ```

### 2. Build as a macOS App (.app)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install py2app
   ```
2. Build the app:
   ```bash
   python setup.py py2app
   ```
3. The `.app` will be in the `dist/` folder. Double-click to run.

## Files
- `cpu_tray.py`: Main application code
- `setup.py`: py2app build script
- `requirements.txt`: Python dependencies
- `dist/`: Output folder for the built .app

## Troubleshooting
- If you see errors about missing libraries (e.g., `libcrypto.3.dylib`), ensure you have the required libraries installed via Homebrew or your system package manager.
- If you encounter permission errors, try running the build command with `sudo` (not generally recommended) or adjust file permissions.

## License
MIT License
