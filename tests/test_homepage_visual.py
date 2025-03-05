from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from applitools.selenium import Eyes
from webdriver_manager.chrome import ChromeDriverManager

def test_homepage_visual():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    eyes = Eyes()
    eyes.api_key = "YOUR_API_KEY" ##Replace with the applitools api key 
    
    try:
        eyes.open(driver, "Automation Exercise", "Home Page Test", {"width": 1200, "height": 800})
        driver.get("https://automationexercise.com")  # Target website
        eyes.check_window("Homepage Snapshot")
        eyes.close()
    finally:
        driver.quit()
        eyes.abort()

if __name__ == "__main__":
    test_homepage_visual()