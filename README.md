## 💾 Install Python and Dependencies on Localhost

1. **Clone Repository Git**
2. **Install Python**: Download from [https://www.python.org/downloads/](https://www.python.org/downloads/). Be sure to select the option to add Python to the PATH during installation.
3. **Validate Python Installation**: Open command prompt and run `python --version`.
4. **Install PIP**: Download the "get-pip.py" file from [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py). Open CMD and run `python get-pip.py`. Validate the installation by running `pip --version` in cmd.
5. **Install Environment**:
    1. In the Windows terminal or VS Code, navigate to the program folder. Example: `cd C:\Users\YourUsername\MyProject`.
    2. Run command `python -m venv venv` (venv is a Python library, and the second venv indicates the name of the environment, let's always use that by default). A venv folder will be created in the repository.
    3. Activate the environment by running `./Venv/Scripts/Activate.ps1`. If activated correctly, the name of the environment will appear in parentheses in the VS Code terminal.
        - If the environment cannot be activated, follow these steps:
            1. Open PowerShell with administrator privileges: Right-click on the Start menu and select "Windows PowerShell (Admin)".
            2. Verify the script execution policy by running `Get-ExecutionPolicy`. If it's wrong, it will show "Restricted".
            3. Change the script execution policy using `Set-ExecutionPolicy RemoteSigned`.
6. **Install Library**:
    1. Inside the repository, there is a file with all the libraries to install (requirements.txt). Run `pip install -r requirements.txt` in the terminal to install all the libraries. This ensures everyone has the same versions of the library.

## ◾Add New Python Library
In the terminal, you can install libraries using pip. Example: `pip install python-multipart`. When installing a library, remember to update the "requirements.txt" file by running `pip freeze > requirements.txt` in the terminal.

## ◾pylint
To run linting rules with pylint, the virtual environment must be running, and navigate to the 'src' folder. From here, you can run pylint on the entire 'src' folder with `pylint *` or on specific folders/files as needed, for example, `pylint services/*` or `pylint services/maizplus.py`.



**📝TASKS LIST**
---

### DOING
- 🔵 Improve path finder when there are so many enemies

### TO DO
- 🟡 Add some decoration on the ground

### DONE
- 🟢 2024-03-14 | Invest path finder algorithms and implements in MapObject class


