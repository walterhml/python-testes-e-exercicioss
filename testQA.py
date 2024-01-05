from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.example.com"

driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_name("name").send_keys("John Doe")
driver.find_element_by_name("email").send_keys("johndoe@example.com")
driver.find_element_by_name("message").send_keys("Hello, World!")
driver.find_element_by_css_selector("input[type='submit']").click()

assert "Mensagem enviada com sucesso!" in driver.page_source

driver.quit()

print("Testes concluídos com sucesso!")