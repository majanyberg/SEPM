# Clock Game Setup Instructions

To ensure the Clock Game runs correctly on **any computer**, follow these setup steps.

---

## **✅ 1. System Requirements**
Before running the game, ensure the system has the following:

### **🖥️ Check Python Installation**
The game requires **Python 3.8 or later**.
Check if Python is installed by running:
```sh
python3 --version
```
If missing, download and install Python from [python.org](https://www.python.org/downloads/).

### **🖥️ Check for pip3 (Python Package Manager)**
Check if `pip3` is installed:
```sh
pip3 --version
```
If missing, install it:
```sh
sudo apt install python3-pip -y  # Ubuntu/Debian
brew install python3              # macOS
```

### **🖥️ Check for Tkinter (GUI Toolkit)**
Check if Tkinter is installed:
```sh
python3 -m tkinter
```
- If a **window opens**, Tkinter is installed.
- If missing, install it:

#### **Linux (Ubuntu/Debian)**
```sh
sudo apt install python3-tk -y
```
#### **Fedora**
```sh
sudo dnf install python3-tkinter -y
```
#### **macOS**
```sh
brew install python-tk
```

---

## **✅ 2. Install Required Python Libraries**
To install all dependencies, use the provided **requirements file**.

### **📥 Install Dependencies**
```sh
pip3 install -r requirements.txt
```

---

## **✅ 3. Install Required Fonts**
The game uses **Work Sans** font. If it's not installed, UI elements may not display correctly.

### **🖥️ Linux (Ubuntu/Debian)**
```sh
sudo apt install fonts-google -y  # Includes "Work Sans"
```

### **🖥️ macOS**
```sh
brew tap homebrew/cask-fonts
brew install --cask font-work-sans
```

### **🖥️ Windows**
1. Download **Work Sans** from [Google Fonts](https://fonts.google.com/specimen/Work+Sans).
2. Install the font manually.

---

## **✅ 4. Ensure the `assets` Directory Exists**
The game requires the `assets` folder containing:
- `assets/UU-logo`
- `assets/progress.json`
- `assets/WorkSans-Italic-VariableFont_wght.ttf`

If `progress.json` is missing, create it:
```sh
echo '{"scores": {}, "leaderboard": []}' > assets/progress.json
```

---

## **✅ 5. Running the Game**
Once everything is set up, **run the game**:
```sh
python3 ui.py
```

If running from the **Main Menu**, use:
```sh
python3 main.py
```

---

## **📌 Summary of Installation Steps**
### **System Dependencies**
✔ Python 3.8+  
✔ pip3  
✔ Tkinter (`python3-tk`)  

### **Python Libraries**
✔ Pillow (`pip3 install pillow`)  
✔ Tk (`pip3 install tk`)  

### **Fonts**
✔ "Work Sans" font installed  

### **Assets**
✔ Ensure `assets/UU-logo`, `assets/progress.json` and `assets/WorkSans-Italic-VariableFont_wght.ttf` exist  


