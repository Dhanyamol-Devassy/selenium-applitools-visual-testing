Selenium + Applitools Visual Testing

This project demonstrates AI-powered visual testing using Selenium WebDriver and Applitools Eyes to validate UI changes effectively.

📌 Features

✅ Automates UI validation with Applitools Visual AI✅ Detects pixel-perfect UI changes without false positives✅ Works across browsers and screen sizes

🐂 Repository Structure

selenium-applitools-visual-testing/
│── tests/
│   ├── test_homepage_visual.py  # Test script for homepage UI validation
│   ├── test_banner_visual.py    # Test script for banner UI validation
│── requirements.txt  # Required dependencies
│── .gitignore  # Ignore unnecessary files
│── README.md  # Documentation

🚀 Setup & Installation

1️⃣ Install Dependencies

Ensure you have Python, Selenium, and Applitools SDK installed:

pip install selenium
pip install eyes-selenium
pip install webdriver-manager

2️⃣ Get Your Applitools API Key

Sign up at Applitools

Navigate to Account Settings → Copy your API Key

Replace YOUR_APPLITOOLS_API_KEY in test scripts

3️⃣ Run the Tests

python tests/test_homepage_visual.py
python tests/test_banner_visual.py

This will launch the browser, capture UI snapshots, and compare them to the baseline in the Applitools Dashboard.

📊 View Results in Applitools Dashboard

Go to Applitools Dashboard

Review detected UI changes

Approve or reject updates to update the baseline

![image](https://github.com/user-attachments/assets/ba2dfc94-b03d-4c1c-a2c7-09a08a94dc81)

💡 Why Use AI-Powered Visual Testing?

✅ Eliminates flaky tests caused by CSS changes✅ Detects meaningful UI differences (not just pixel shifts)✅ Cross-browser & responsive testing support
