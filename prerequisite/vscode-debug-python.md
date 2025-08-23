# Debugging Python Files in VSCode

This guide explains how to debug Python files using Visual Studio Code.

## Prerequisites

- Install [Visual Studio Code](https://code.visualstudio.com/)
- Install the [Python extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Ensure Python is installed on your system

## Steps to Debug a Python File

1. **Open your project folder in VSCode.**

2. **Open the Python file you want to debug.**

3. **Set breakpoints:**
   - Click in the gutter to the left of the line numbers where you want execution to pause.

4. **Start debugging:**
   - Press `F5`, or
   - Click the green "Run and Debug" button in the Run panel, or
   - Select "Run > Start Debugging" from the menu.

5. **Configure the debugger (if prompted):**
   - If this is your first time, VSCode may prompt you to create a `launch.json` file. Choose "Python File" to use the default configuration.

6. **Use the Debug Toolbar:**
   - Step over (`F10`), step into (`F11`), continue (`F5`), or stop debugging as needed.
   - Inspect variables and the call stack in the left sidebar.

## Tips

- You can add variables to the "Watch" panel to monitor their values.
- Use the Debug Console to execute Python commands while paused.

## References

- [VSCode Python Debugging Documentation](https://code.visualstudio.com/docs/python/debugging)
