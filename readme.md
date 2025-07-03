# Advanced Gmail Account Creation Bot

A Python automation script, modified and enhanced by **Javier Garcia Cubiles**.

This project is based on the original script by [Abdelhakim Khaouiti](https://github.com/khaouitiabdelhakim), but it has been extensively rewritten to include advanced logic, error handling, and adaptability to Google's modern user interface.

---

## Overview

This bot automates the process of creating Gmail accounts using Selenium and ChromeDriver. Unlike simpler scripts, this version incorporates several robust features to handle the complexity and variations of Google's sign-up pages.

### Key Features

-   **Random Data Generation:** Creates unique first names, last names, and usernames in each run to simulate real users.
-   **Flexible Navigation:** Capable of detecting and handling multiple sign-up flows that Google presents randomly (A/B Testing).
-   **Robust Interaction:** Uses a combination of explicit waits (`WebDriverWait`), forced JavaScript clicks, and keyboard navigation to overcome the hurdles of modern web interfaces.
-   **Clean Sessions:** Starts the browser in Incognito mode to ensure that previous sessions or cookies do not interfere with the process.

---

## ⚠️ IMPORTANT: Antivirus False Positive Warning! ⚠️

It is **VERY LIKELY** that your antivirus software (such as Windows Defender, Avast, AVG, etc.) will detect the downloaded ZIP file from this repository or the running script as a **"virus" or "unwanted software"**.

**Please do not worry!** This is a **FALSE POSITIVE** and is an expected behavior for this type of automation tool.

### Why does this happen?

This script utilizes [Selenium](https://www.selenium.dev/) and `chromedriver.exe` to **automate and control the Google Chrome browser**. The ability of a program to programmatically interact with the browser and simulate user actions (like typing text, clicking, etc.) is a characteristic also used by certain types of malicious software (bots, spamware, etc.).

Due to this functional similarity, heuristic engines in antivirus software, especially for new or less common software, tend to flag such scripts as potentially dangerous, even when the intent is entirely legitimate and the code is safe. Your code does not contain any actual viruses or malicious software.

### What to do if your antivirus flags it?

1.  **Check on VirusTotal:** If you have any doubts, you can upload the downloaded ZIP file (or the `chromedriver.exe` file if downloaded separately) to [VirusTotal](https://www.virustotal.com/gui/home/upload). This online tool will scan the file with dozens of different antivirus engines. If only a few engines detect it (especially less-known ones) and most major ones deem it clean, this confirms it's a false positive.
2.  **Add an Exception:** If you are confident in the legitimacy of this script (as you downloaded it from my official repository), you can add an exception or exclusion for the project folder or specific files (`.py` and `chromedriver.exe`) in your antivirus software's settings. This will instruct your antivirus to trust these files and not block or delete them in the future. (Refer to your antivirus's documentation on how to add "Exclusions," "Trusted Items," or to the "Whitelist.")

---

## Prerequisites

-   **Python 3.x**
-   **Google Chrome Browser** (any recent version).
-   **ChromeDriver:** The executable that allows Selenium to control Chrome.
    -   You can download it from the official dashboard: **[Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)**
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
    Simply run the provided installation script for your operating system:
    -   **For Windows:** Double-click `install_dependencies.bat`
    -   **For Linux/macOS:** Open a terminal, navigate to the project folder, and run:
        ```bash
        chmod +x install_dependencies.sh # Make the script executable
        ./install_dependencies.sh
        ```
    This will create a virtual environment and install all required Python libraries.

4.  **Download and place ChromeDriver:**
    Download the `chromedriver.exe` file that corresponds to your Chrome version from the link in the "Prerequisites" section and place it in the same folder as the Python script.

5.  **Run the script:**
    Open a terminal in the project folder and run:
    ```bash
    # For Windows:
    .\venv\Scripts\python.exe your_script_name.py

    # For Linux/macOS:
    ./venv/bin/python your_script_name.py
    ```
    *(Replace `your_script_name.py` with the actual name of your file, e.g., `gmail_automation.py`)*

The bot will begin the process and will display the created account's credentials in the terminal upon successful completion.

## Important Notice

Automating account creation may be against Google's Terms of Service. This script is provided for educational purposes and to demonstrate advanced automation techniques. Use it responsibly and at your own risk. The author is not responsible for any misuse of this code.

## Credits

-   **Modified and Enhanced Version:** Javier Garcia Cubiles
-   **Original Script:** Abdelhakim Khaouiti ([khaouitiabdelhakim on GitHub](https://github.com/khaouitiabdelhakim))
