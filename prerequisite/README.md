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

## References

- [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)
- [VSCode Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
