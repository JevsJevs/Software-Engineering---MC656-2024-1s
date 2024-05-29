from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from csv import DictReader

driver = webdriver.Firefox()
driver.implicitly_wait(2)
driver.get("https://olympics.com")
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
with open("scrapping/esportes_en.csv") as f:
    csv_reader = DictReader(f, lineterminator='\n')
    eventos = []
    for linha in csv_reader:
        nomes = []
        esporte = linha["nome"]
        esporte_url = esporte.lower().replace(' ', '-').replace('/', '-')
        print(esporte_url)
        url = f"https://olympics.com/pt/olympic-games/tokyo-2020/results/{esporte_url}"
        driver.get(url)
        (ActionChains(driver)
            .scroll_by_amount(0, 400)
            .scroll_by_amount(0, 400)
            .scroll_by_amount(0, 400)
            .scroll_by_amount(0, 400)
            .perform())
        botao = driver.find_element(By.CSS_SELECTOR, 'button[data-cy="event-select"]')
        botao.click()
        s = driver.find_element(By.CSS_SELECTOR, 'div[data-cy="inline-wizard-events"]')
        l = s.find_elements(By.CSS_SELECTOR, 'button[data-cy="event-button"]')
        for e in l:
            nome = e.find_element(By.TAG_NAME, 'p')
            eventos.append((nome.get_attribute("innerHTML"), esporte))
    with open("scrapping/eventos.csv", 'w') as f:
        f.write("id,evento,esporte\n")
        for i, (evento, esporte) in enumerate(eventos):
            f.write(f"{i},{evento},{esporte}")

