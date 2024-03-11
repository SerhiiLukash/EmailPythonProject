import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

PROXY_SERVER = "200.69.243.137:80"
# useragentarray = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
# ]

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    #options.add_argument(f"--proxy-server={PROXY_SERVER}")
    #options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--lang=en-GB")
    service = Service(ChromeDriverManager(driver_version="121.0.6167.161").install())
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.maximize_window()
    # for i in range (len(useragentarray)):
    #     driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[i]})
    yield driver
    #driver.quit()
