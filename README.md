# Swedish Learning Game 

This project is part of the **Software Engineering and Project Management** course at **Uppsala University**. It focuses on developing the user interface (UI) for a Swedish learning game designed to help users learn Swedish interactively. This repository contains the code related to the Swedish Learning Game application, where users can practice Swedish through various levels and challenges.

## Application Setup and Execution

### Prerequisites
Before setting up the application, ensure you have the relevant packages installed.

### 1. Verify Python installation
To verify if Python is installed, run the following command:

- **MacOS**
```bash
python3 --version
```

- **Linux(Ubuntu)**
```bash
python3 --version
```

- **Windows**
```bash
python --version
```
*or*
```bash
python3 --version
```

If Python is not installed, install it using the following:

- **MacOS**
```bash
brew install python
```

- **Linux(Ubuntu)**
```bash
sudo apt update
sudo apt install python3 -y
 ```

- **Windows**
  *Download and install it from [Python's official website](https://www.python.org/downloads/).*

### 2.  Verify pip Installation
To verify if pip is installed, run the following command:

- **MacOS**
```bash
pip3 --version
```
*or*
```bash
python3 -m pip --version
```

- **Linux(Ubuntu)**
```bash
pip3 --version
```
*or*
```bash
python3 -m pip --version
```

- **Windows**
```bash
pip --version 
```
*or*
```bash
pip3 --version 
```

If pip is not installed, install it using:

- **MacOS**
```bash
python3 -m ensurepip --default-pip
```

- **Linux(Ubuntu)**
```bash
sudo apt update
sudo apt install python3-pip -y
```

- **Windows**
```bash
python -m ensurepip --default-pip
```

### 3. Verify Tkinter Installation
To verify if tkinter is installed, run the following command:

- **MacOS**
```bash
python3 -m tkinter
```

- **Linux(Ubuntu)**
```bash
python3 -m tkinter
```

- **Windows**
```bash
python -m tkinter
```

If not installed, install it using:

- **MacOS**
 ```bash
brew install python-tk
 ```

- **Linux(Ubuntu)**
 ```bash
sudo apt update
sudo apt install python3-tk -y
 ```
- **Windows**
  *For Windows, Tkinter comes pre-installed with standard Python distributions.*

## Run the application

### Clone this repository
```bash
git clone https://github.com/SamuelMoller/sepm-group6.git
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Start the application
```bash
python scripts/interface.py
```

