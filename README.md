## Instagram Follower Automation Bot

This project automates the process of discovering and following users from the followers list of a specified Instagram account.

Using Selenium WebDriver, the script logs into Instagram, navigates to a target profile, opens the followers dialog, scrolls through dynamically loaded users, and programmatically follows selected accounts.

The goal of this project is to understand how browser automation interacts with complex modern web interfaces such as modal dialogs and dynamically rendered elements.

This project was developed as part of the #90DaysOfCode challenge to practice advanced browser automation workflows using Python.

---

## Technologies Used

Python  
Selenium WebDriver  
ChromeDriver  
WebDriverWait  
Expected Conditions  
JavaScript DOM interaction

---

## Key Concepts Demonstrated

Browser automation using Selenium WebDriver

Handling dynamically loaded UI elements

Explicit waits for reliable element interaction

Scrolling inside modal dialogs using JavaScript execution

Handling intercepted clicks and automation exceptions

Structuring automation workflows using Python classes

---

## Automation Workflow

1. Launch a Chrome browser session
2. Navigate to the Instagram login page
3. Authenticate using username and password
4. Dismiss prompts such as saving login information and notifications
5. Navigate to the target Instagram profile
6. Open the followers dialog
7. Scroll the followers container to load additional users
8. Identify Follow buttons inside the modal dialog
9. Automatically follow selected users

---

## Installation

Install the required dependency

```
pip install selenium
```

Ensure ChromeDriver is installed and compatible with your Chrome browser version.

ChromeDriver should also be accessible through your system PATH.

---

## Run

```
python main.py
```

---

## Configuration

Update these variables before running the script

```
USERNAME = "YOUR_IG_USERNAME"
PASSWORD = "YOUR_IG_PASSWORD"
SIMILAR_ACC = "target_account"
```

---

## Why This Project Matters

Modern social media platforms rely heavily on JavaScript-driven interfaces and dynamic content loading.

This project demonstrates how browser automation can

Automate repetitive workflows

Interact with modal dialogs and dynamically loaded UI components

Handle asynchronous page updates using explicit waits

Build practical automation scripts that interact with real-world web platforms

---

## Disclaimer

This project is intended for educational and learning purposes only.  
Automating actions on social platforms may violate their terms of service if misused.

---

## Author

Faiz Hasan  
Python Automation & Backend Developer
