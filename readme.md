# Advanced Gmail Account Creation Bot

A Python automation script, modified and enhanced by **Javier Garcia Cubiles**.

This project is based on the original script by [Abdelhakim Khaouiti](https://github.com/khaouitiabdelhakim), but it has been extensively rewritten to include advanced logic, error handling, and adaptability to Google's modern user interface.

---

## Overview

This bot automates the process of creating Gmail accounts using Selenium and ChromeDriver. Unlike simpler scripts, this version incorporates several robust features to handle the complexity and variations of Google's sign-up pages.

### Key Features

- **Random Data Generation:** Creates unique first names, last names, and usernames in each run to simulate real users.
- **Flexible Navigation:** Capable of detecting and handling multiple sign-up flows that Google presents randomly (A/B Testing).
- **Robust Interaction:** Uses a combination of explicit waits (`WebDriverWait`), forced JavaScript clicks, and keyboard navigation to overcome the hurdles of modern web interfaces.
- **Clean Sessions:** Starts the browser in Incognito mode to ensure that previous sessions or cookies do not interfere with the process.

## Prerequisites

- **Python 3.x**
- **Google Chrome Browser** (any recent version).
- **ChromeDriver:** The executable that allows Selenium to control Chrome.
  - You can download it from the official dashboard: **[Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)**
  > **Important:** Ensure that the ChromeDriver version you download **exactly matches** your installed Google Chrome version, otherwise the script will not work.

## Installation and Usage

Follow these steps to get the bot up and running:

1.  **Clone this repository to your computer:**
    ```bash
    git clone [https://github.com/your-username/your-repository.git](https://github.com/your-username/your-repository.git)
    ```
    *(Replace the URL with your own repository's URL)*

2.  **Navigate to the project folder:**
    ```bash
    cd your-repository-name
    ```

3.  **Install the necessary dependencies:**
    It is recommended to create a virtual environment. Once activated, install the required libraries from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download and place ChromeDriver:**
    Download the `chromedriver.exe` file that corresponds to your Chrome version from the link in the "Prerequisites" section and place it in the same folder as the Python script.

5.  **Run the script:**
    Open a terminal in the project folder and run:
    ```bash
    python your_script_name.py
    ```
    *(Replace `your_script_name.py` with the actual name of your file)*

The bot will begin the process and will display the created account's credentials in the terminal upon successful completion.

## Important Notice

Automating account creation may be against Google's Terms of Service. This script is provided for educational purposes and to demonstrate advanced automation techniques. Use it responsibly and at your own risk. The author is not responsible for any misuse of this code.

## Credits

- **Modified and Enhanced Version:** Javier Garcia Cubiles
- **Original Script:** Abdelhakim Khaouiti ([khaouitiabdelhakim on GitHub](https://github.com/khaouitiabdelhakim))
