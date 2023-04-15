from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os


async def get_eco_status():
    """
    Returns the player count, day, time information and meteor impact time.
    """

    # Set up the Chrome driver
    s = Service('path/to/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(service=s, options=options)

    # Load the webpage
    url = os.getenv("ECO_WEBSITE_IP")
    try:
        driver.get(url)
    except:
        return None

    # Find all the span elements with class name 'text-highlight'
    text_highlight_spans = driver.find_elements(By.CLASS_NAME, 'text-highlight')

    # Extract the player count and time information from the first two spans
    player_count_span = text_highlight_spans[0]
    time_span = text_highlight_spans[1]

    # Extract the text content of the player count span
    player_count = player_count_span.text

    # Extract the text content of the time span and split it by comma
    time_text = time_span.text

    # Extract the day and time from the time text
    day, time = time_text.split(',')[0].split()[-1], time_text.split(',')[1].strip()

    # Find the Meteor Impact element and extract the remaining time information
    meteor_impact_li = driver.find_element(By.XPATH, '//li[contains(.,"Meteor Impact")]')
    meteor_impact_time = meteor_impact_li.find_element(By.CLASS_NAME, 'text-highlight').text

    # Close the browser
    driver.quit()

    # Return the player count, day, time information and meteor impact time
    return player_count, day, time, meteor_impact_time