from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from applitools.selenium import Eyes
from webdriver_manager.chrome import ChromeDriverManager

def test_banner_visual():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    eyes = Eyes()
    eyes.api_key = "YOUR_API_KEY" #Replace with the applitools api key 
    
    try:
        eyes.open(driver, "Automation Exercise", "Banner Test", {"width": 1200, "height": 800})
        driver.get("https://automationexercise.com")  # Target website
        banner = driver.find_element(By.CLASS_NAME, "carousel-inner")
        eyes.check_region(banner, "Banner Snapshot")
        eyes.close()
    finally:
        driver.quit()
        eyes.abort()

if __name__ == "__main__":
    test_banner_visual()