import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def wait_and_click(browser, selector):
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    element.click()


opts = Options()
opts.add_argument("--no-sandbox")
opts.add_argument('--disable-dev-shm-usage')
browser = Chrome(service=Service(
    ChromeDriverManager().install()), options=opts)
browser.implicitly_wait(10)

browser.get('https://dev.digital.etu.ru/trajectories-test/auth')

# Close modal
browser.find_element(By.ID, "devServerModalId___BV_modal_content_")
time.sleep(1)
closeModal = browser.find_element(
    By.CSS_SELECTOR, "#devServerModalId___BV_modal_footer_ > button")
closeModal.click()

# Login through etu id
browser.find_element(
    By.CSS_SELECTOR, '.card-text > div > button:first-child').click()

# Send login form creds and wait
browser.find_element(By.CSS_SELECTOR, "input[type=email]").send_keys(
    "lolovishka@mail.ru")
browser.find_element(
    By.CSS_SELECTOR, "input[type=password]").send_keys("Ugngbnm19")
browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
time.sleep(1)

# Authorize btn click
browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

# Remove cookies notification
browser.find_element(By.CSS_SELECTOR, ".btn.mb-1.btn-outline-primary").click()

# Click on open sidebar menu
wait_and_click(browser, "button.mr-2")

# Click btn "authorize as other user"
wait_and_click(browser, "a[href=\"/trajectories-test/admin/fake\"]")

# Open popup filter by id
browser.find_element(
    By.CSS_SELECTOR, "span.ag-header-icon.ag-header-cell-menu-button:first-of-type").click()

# Enter id 1305 in input
browser.find_element(
    By.CSS_SELECTOR, "div.ag-popup-child input").send_keys("1305")

# Double-click on user row
userRow = browser.find_element(
    By.CSS_SELECTOR, "div[ref=\"eCenterContainer\"] > div")
action = ActionChains(browser)
action.double_click(on_element=userRow)
action.perform()

# Wait for main page to load
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src="/trajectories-test/logo-leti.png"]')))

# === CREATING OPOP ===

# Open sidebar menu by btn click
wait_and_click(browser, "button.btn.mr-2.btn-primary.rounded-pill.collapsed")

# Click opop btn
wait_and_click(browser, "a[href=\"/trajectories-test/documents/opop-list\"]")

# Click add opop btn
wait_and_click(browser, ".btn.mx-1:first-of-type")

# Select speciality name
browser.find_element(
    By.CSS_SELECTOR, ".form-group.valid.required.field-multiselect:nth-of-type(1) > div > div").click()
browser.find_element(
    By.CSS_SELECTOR, ".multiselect__element:first-of-type").click()
time.sleep(1)

# Select speciality plan
browser.find_element(
    By.CSS_SELECTOR, ".form-group.valid.required.field-multiselect:nth-of-type(2) > div > div").click()
browser.find_element(
    By.CSS_SELECTOR, ".multiselect__element:nth-of-type(6)").click()
time.sleep(1)

# Click on add btn
browser.find_element(
    By.CSS_SELECTOR, "#creationModalId___BV_modal_content_ .btn.btn-primary").click()

# Wait for blank to load
WebDriverWait(browser, 10).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, ".mx-1.status-text")))

# === / CREATING OPOP ===

# === GIVING RIGHTS ===

# go to rights tab
browser.find_element(By.CSS_SELECTOR, 'a[aria-posinset="13"]').click()
time.sleep(1)

# click on add btn
browser.find_element(By.CSS_SELECTOR, '.btn.float-right.btn-primary').click()
time.sleep(1)

# select first user
browser.find_element(
    By.CSS_SELECTOR, '.ag-center-cols-container > div:first-of-type').click()
time.sleep(1)

# click checkbox first option
browser.find_element(
    By.CSS_SELECTOR, '.custom-control.custom-control-inline.custom-checkbox:first-of-type').click()
time.sleep(1)

# click on give rights btn
browser.find_element(
    By.CSS_SELECTOR, '#addRightsModal___BV_modal_footer_ > button:first-of-type').click()
time.sleep(1)

# === / GIVING RIGHTS ===

# === CHECKING HISTORY ===

browser.find_element(By.CSS_SELECTOR, 'a[aria-postinset="15"]').click()
time.sleep(1)

# === / CHECKING HISTORY ===
