# 🧮 Multi-platform Python Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-red.svg)](https://flask.palletsprojects.com/)





## 📝 Description

A multi-platform calculator developed in Python, demonstrating various approaches to user interface development. The project includes three different calculator implementations:

1. **Console Calculator** - classic text interface
2. **GUI Calculator** - graphical interface using Tkinter
3. **Web Calculator** - modern interface accessible through a browser

All implementations share the same calculation logic, showing how basic functionality can be adapted for different user interfaces.

## 🛠️ Technologies Used

### Backend
- **Python** - main programming language
- **Flask** - lightweight web framework for Python
- **Tkinter** - standard GUI library in Python

### Frontend (Web version)
- **HTML5** - web interface structure
- **CSS3** - styling and animations
  - Modern CSS techniques: Glass Morphism, animations, gradients
  - Responsive design
- **JavaScript** - client-side logic and interactivity
  - Fetch API for server communication
  - DOM manipulations
  - Events and user input handling

### Architectural Principles
- **Separation of business logic and user interface**
- **Modular structure** - reuse of core calculation logic
- **REST API** - for frontend-backend communication in the web version

## ✨ Features

### Basic Operations
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division

### Advanced Functions
- 🔄 Sign change (+/-)
- 💯 Percentage conversion (%)
- 🧹 Clear current input (C)
- 🗑️ Full calculator reset (AC)

### Web Interface
- 🎨 Multiple color themes (light, dark, standard)
- 📱 Responsive design
- ⌨️ Keyboard shortcuts support
- 💾 Last result storage
- 🔍 Current operation visualization

### GUI Interface
- 🖥️ Native graphical interface
- 🪟 Compact window with fixed size
- 🎯 Intuitive button layout

## 📂 Project Structure

```
.
├── calculator.py          # Base calculation logic and console interface
├── gui_calculator.py      # Tkinter GUI implementation
├── web_calculator.py      # Flask web server
├── requirements.txt       # Project dependencies
└── templates/
    └── calculator.html    # HTML/CSS/JS for the web interface
```

## 🚀 Installation and Launch

### Prerequisites

- Python 3.x
- pip (Python Package Installer)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/python-calculator.git
   cd python-calculator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Different Versions

#### Console Calculator
```bash
python calculator.py
```

#### GUI Calculator
```bash
python gui_calculator.py
```

#### Web Calculator
```bash
python web_calculator.py
```
After starting the web server, open http://127.0.0.1:5000/ in your browser.

## 🖼️ Screenshots

*(Here you can add screenshots of the different calculator interfaces)*

## 📚 Lessons Learned

This project demonstrates:
- How the same logic can be implemented with different interfaces
- Differences between console, GUI, and web applications
- Integration between frontend and backend
- Modern web design techniques
- Effective user experience management

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🤝 Contribution

Contributions to the project are welcome! Please feel free to submit Pull Requests or open Issues.

## 📧 Contact

*(Here you can add your contact information)*

---

Developed with ❤️ and Python 
