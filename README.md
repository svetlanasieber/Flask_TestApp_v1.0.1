# 🧮 Multi-platform Python Calculator [IN DEVELOPMENT]

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-red.svg)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)](https://www.mysql.com/)
[![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)]()

> **Note:** This project is currently under active development. Some features may not be fully implemented or might contain bugs.

## 📝 Description

A multi-platform calculator developed in Python, demonstrating various approaches to user interface development. The project includes three different calculator implementations:

1. **Console Calculator** - classic text interface
2. **GUI Calculator** - graphical interface using Tkinter
3. **Web Calculator** - modern interface accessible through a browser with user profiles and settings

All implementations share the same calculation logic, showing how basic functionality can be adapted for different user interfaces.

## 🛠️ Technologies Used

### Backend
- **Python** - main programming language
- **Flask** - lightweight web framework for Python
- **Flask-Login** - user authentication and session management
- **SQLAlchemy** - ORM for database operations
- **MySQL** - database for user profiles and settings
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
- **MVC pattern** - Model-View-Controller architecture
- **Database persistence** - for user data and settings

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
- 👤 User profiles with personalized settings
- 📊 Calculation history
- ⚙️ Customizable preferences (decimal places, scientific notation)

### GUI Interface
- 🖥️ Native graphical interface
- 🪟 Compact window with fixed size
- 🎯 Intuitive button layout

## 📂 Project Structure

```
.
├── calculator.py          # Base calculation logic and console interface
├── gui_calculator.py      # Tkinter GUI implementation
├── web_calculator.py      # Flask web server with MySQL integration
├── models.py              # Database models for user profiles
├── requirements.txt       # Project dependencies
└── templates/
    ├── calculator.html    # HTML/CSS/JS for the web interface
    ├── register.html      # User registration page
    ├── login.html         # Login page
    ├── settings.html      # User settings page
    └── history.html       # Calculation history page
```

## 🚀 Installation and Launch

### Prerequisites

- Python 3.x
- pip (Python Package Installer)
- MySQL Server (for web version with user profiles)

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

3. MySQL setup (for web version with user profiles):
   - Ensure MySQL server is running
   - Update the MySQL connection parameters in `web_calculator.py` if needed

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

## 🚧 Current Development Status

The project is currently in active development with the following features being worked on:

- **User Authentication System**: Registration, login, and session management
- **MySQL Database Integration**: Storing user profiles, settings, and calculation history
- **Personalized Settings**: Theme preferences, decimal place settings, scientific notation
- **Calculation History**: Saving and viewing past calculations

## 🔧 Known Issues

- MySQL connection may require additional configuration depending on your setup
- Some error handling in the calculation logic needs improvement
- Registration and login system still in testing phase



## 📚 Lessons Learned

This project demonstrates:
- How the same logic can be implemented with different interfaces
- Differences between console, GUI, and web applications
- Integration between frontend and backend
- Modern web design techniques
- Effective user experience management
- Database integration and user authentication
- State management and personalization

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🤝 Contribution

Contributions to the project are welcome! Please feel free to submit Pull Requests or open Issues.



---

Developed with ❤️ and Python 
