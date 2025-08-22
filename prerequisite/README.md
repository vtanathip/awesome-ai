# Prerequisites Setup

This guide explains how to set up a Python development environment using **Pipenv** and configure **VSCode** for development.

## 1. Install Pipenv

Make sure you have Python installed. Then install Pipenv:

```sh
pip install pipenv
```

## 2. Create and Activate Virtual Environment

Navigate to your project directory and run:

```sh
pipenv install --dev
```

This will create a `Pipfile` and a virtual environment.

To activate the virtual environment:

```sh
pipenv shell
```

## 3. Install Project Dependencies

To install dependencies listed in `Pipfile`:

```sh
pipenv install
```

All dependencies will be installed **only inside the Pipenv-managed virtual environment**, keeping your global Python installation clean.

To install a new package:

```sh
pipenv install <package-name>
```

## 4. Configure VSCode to Use Pipenv

1. Open the project folder in VSCode.
2. Press `Ctrl+Shift+P` and select **Python: Select Interpreter**.
3. Choose the interpreter that points to your Pipenv environment. It usually appears as:

   ```sh
   .venv\Scripts\python.exe
   ```

   or

   ```sh
   pipenv (project-name)
   ```

4. If it does not appear, you can find the path by running:

   ```sh
   pipenv --venv
   ```

   Then select the Python executable inside that folder.

## 5. Useful Pipenv Commands

- Check installed packages:

  ```sh
  pipenv graph
  ```

- Run a script inside the environment:

  ```sh
  pipenv run python your_script.py
  ```

- Deactivate the environment:

  ```sh
  exit
  ```

## Setting Up the Python Environment

This project uses a `Pipfile` for dependency management. To activate and use the environment:

1. Install pipenv if you haven't already:

   ```sh
   pip install pipenv
   ```

2. Activate the environment:

   ```sh
   pipenv shell
   ```

3. Install all dependencies:

   ```sh
   pipenv install
   ```

   > **Note:** All dependencies are installed only in the Pipenv virtual environment, not globally.

## References

- [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)
- [VSCode Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
