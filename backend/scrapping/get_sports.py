from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(7)
driver.get("https://olympics.com/pt/olympic-games/tokyo-2020/results")
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
(ActionChains(driver)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .perform())

# e = driver.find_element(By.ID, "olympic-games-disciplines")
e = driver.find_element(By.CSS_SELECTOR, 'section[data-cy="disciplines-list"]')
l = e.find_elements(By.CSS_SELECTOR, 'a[data-cy="disciplines-item"]')
esportes = []
for esporte in l:
    esportes.append(esporte.find_element(By.TAG_NAME, 'p').get_attribute("innerHTML"))
with open("scrapping/esportes.csv", "w") as f:
    f.write("id,nome\n")
    for i, esporte in enumerate(esportes):
        f.write(f"{i},{esporte}\n")

driver.get("https://olympics.com/en/olympic-games/tokyo-2020/results")
driver.implicitly_wait(7)
(ActionChains(driver)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .scroll_by_amount(0, 400)
    .perform())
# e = driver.find_element(By.ID, "olympic-games-disciplines")
e = driver.find_element(By.CSS_SELECTOR, 'section[data-cy="disciplines-list"]')
l = e.find_elements(By.CSS_SELECTOR, 'a[data-cy="disciplines-item"]')
esportes = []
for esporte in l:
    esportes.append(esporte.find_element(By.TAG_NAME, 'p').get_attribute("innerHTML"))
with open("scrapping/esportes_en.csv", "w") as f:
    f.write("id,nome\n")
    for i, esporte in enumerate(esportes):
        f.write(f"{i},{esporte}\n")
    