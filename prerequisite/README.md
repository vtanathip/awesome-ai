# Using Pipenv for Python Project Management

This guide explains what **Pipenv** is, how to install it, and how to use it to manage Python dependencies and virtual environments. It also covers how to configure **VSCode** to work with Pipenv.

## What is Pipenv?

[Pipenv](https://pipenv.pypa.io/en/latest/) is a tool that simplifies dependency management and virtual environments for Python projects. It combines the features of `pip` and `virtualenv` into a single workflow, making it easier to manage project-specific packages and environments.

## 1. How to Install Pipenv

First, ensure you have Python (3.6 or newer) installed on your system.

To install Pipenv globally, run:

```sh
pip install pipenv
```

You can verify the installation with:

```sh
pipenv --version
```

## 2. Creating and Using a Pipenv Environment

Navigate to your project directory in your terminal.

To create a new Pipenv-managed environment and a `Pipfile`, run:

```sh
pipenv install --dev
```

- This will create a virtual environment and a `Pipfile` for dependency tracking.
- The `--dev` flag adds development dependencies.

To activate the Pipenv environment:

```sh
pipenv shell
```

This command spawns a new shell with the virtual environment activated.

## 3. Installing and Managing Dependencies

To install all dependencies listed in the `Pipfile`:

```sh
pipenv install
```

To add a new package to your project:

```sh
pipenv install <package-name>
```

To add a development-only package:

```sh
pipenv install --dev <package-name>
```

All packages are installed inside the Pipenv-managed virtual environment, keeping your global Python installation clean.

## 4. Running Python Scripts with Pipenv

You can run Python scripts inside the Pipenv environment without activating the shell:

```sh
pipenv run python your_script.py
```

## 5. Checking Installed Packages

To see a dependency graph of installed packages:

```sh
pipenv graph
```

## 6. Deactivating the Environment

To exit the Pipenv shell, simply type:

```sh
exit
```

## 7. Configuring VSCode to Use Pipenv

1. Open your project folder in VSCode.
2. Press `Ctrl+Shift+P` and select **Python: Select Interpreter**.
3. Choose the interpreter that points to your Pipenv environment. It may appear as:
   - `pipenv (project-name)`
   - Or as a path like `.venv\Scripts\python.exe`
4. If you don't see it, find the environment path with:

   ```sh
   pipenv --venv
   ```

   Then select the Python executable inside that folder.

## 8. Summary of Useful Pipenv Commands

- **Install Pipenv:** `pip install pipenv`
- **Create environment:** `pipenv install`
- **Activate environment:** `pipenv shell`
- **Install package:** `pipenv install <package>`
- **Install dev package:** `pipenv install --dev <package>`
- **Run script:** `pipenv run python your_script.py`
- **Show dependencies:** `pipenv graph`
- **Exit environment:** `exit`

## References

- [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)
- [VSCode Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
