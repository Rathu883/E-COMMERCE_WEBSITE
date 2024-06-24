from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.common.action_chains import ActionChains # type: ignore
import time

# Path to your WebDriver
driver_path = ''
driver = webdriver.Chrome(executable_path=driver_path)

try:
    # Open the HTML file
    driver.get('file:///path/to/index.html')

    # Maximize the window
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load

    # Example of adding an item to the cart
    # Assuming there are buttons or links to add items to the cart
    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, 'add-to-cart')
    for button in add_to_cart_buttons[:2]:  # Adding first two items
        button.click()
        time.sleep(1)  # Wait for the item to be added

    # Navigate to the cart
    cart_button = driver.find_element(By.CLASS_NAME, 'cart')
    cart_button.click()
    time.sleep(2)  # Wait for the cart page to load

    # Proceed to checkout
    checkout_button = driver.find_element(By.CLASS_NAME, 'checkout')
    checkout_button.click()
    time.sleep(2)  # Wait for the checkout page to load

    # Fill in checkout details
    # Example fields: name, email, address, payment method
    name_field = driver.find_element(By.NAME, 'name')
    email_field = driver.find_element(By.NAME, 'email')
    address_field = driver.find_element(By.NAME, 'address')
    payment_field = driver.find_element(By.NAME, 'payment')

    name_field.send_keys('John Doe')
    email_field.send_keys('john.doe@example.com')
    address_field.send_keys('123 Main St, Anytown, USA')
    payment_field.send_keys('4111111111111111')

    # Submit the order
    submit_button = driver.find_element(By.NAME, 'submit')
    submit_button.click()

    # Wait for the confirmation page to load
    time.sleep(5)

    # Optionally, you can capture the confirmation message
    confirmation_message = driver.find_element(By.CLASS_NAME, 'confirmation')
    print(confirmation_message.text)

finally:
    # Close the browser
    driver.quit()
