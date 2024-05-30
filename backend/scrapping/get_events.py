from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from csv import DictReader
import csv
import re

def get_events_en(driver: WebDriver):
    with open("scrapping/esportes_en.csv") as f:
        csv_reader = DictReader(f, lineterminator='\n')
        eventos = []
        for linha in csv_reader:
            esporte_en = linha["nome"]
            esporte_url = esporte_en.lower().replace(' ', '-').replace('/', '-')
            print(esporte_url)
            url = f"https://olympics.com/pt/olympic-games/tokyo-2020/results/{esporte_url}"
            driver.get(url)
            h1 = driver.find_element(By.TAG_NAME, "h1")
            texto = h1.get_attribute("innerHTML")
            esporte_pt = texto.split("Resultados ")[-1]
            (ActionChains(driver)
                .scroll_by_amount(0, 400)
                .scroll_by_amount(0, 400)
                .scroll_by_amount(0, 400)
                .scroll_by_amount(0, 400)
                .perform())
            botao = driver.find_element(By.CSS_SELECTOR, 'button[data-cy="event-select"]')
            (ActionChains(driver)
                .scroll_by_amount(0, 400)
                .scroll_by_amount(0, 400)
                .scroll_by_amount(0, 400)
                .scroll_by_amount(0, 400)
                .perform())
            botao.click()
            s = driver.find_element(By.CSS_SELECTOR, 'div[data-cy="inline-wizard-events"]')
            l = s.find_elements(By.CSS_SELECTOR, 'button[data-cy="event-button"]')
            for e in l:
                nome = e.find_element(By.TAG_NAME, 'p')
                eventos.append((nome.get_attribute("innerHTML"), esporte_en, esporte_pt))
        with open("scrapping/eventos.csv", 'w') as f:
            w = csv.writer(f, lineterminator='\n')
            w.writerow(["id", "evento", "esporte_en"])
            for i, (evento, esporte_en, esporte_pt) in enumerate(eventos):
                w.writerow([i, evento, esporte_en])

def get_events_pt(driver: WebDriver):
    with open("scrapping/eventos_en.csv") as f:
        csv_reader = DictReader(f, lineterminator='\n')
        eventos = []
        for linha in csv_reader:
            esporte = linha["esporte"]
            esporte_url = esporte.lower().replace(' ', '-').replace('/', '-')
            evento = linha["evento"]
            match esporte_url:
                case "judo" | "karate" | "taekwondo":
                    evento = evento.replace('-', '')
            evento_url = (evento.lower()
                .replace(' ', '-').replace('/', '-').replace("'", '-').replace(':', '-')
                .replace(',', '').replace('(', '').replace(')', '')
                .replace('+', 'over-').replace('é', 'e'))
            url = f"https://olympics.com/pt/olympic-games/tokyo-2020/results/{esporte_url}/{evento_url}"
            driver.get(url)
            (ActionChains(driver)
                .scroll_by_amount(0, 400)
                .scroll_by_amount(0, 400)
                .scroll_by_amount(0, 400)
                .scroll_by_amount(0, 400)
                .perform())
            spans = (driver
                .find_element(By.CSS_SELECTOR, 'button[data-cy="event-select"]')
                .find_elements(By.TAG_NAME, "span"))
            prox = False
            e = None
            for span in spans:
                if prox:
                    e = span
                    break
                if span.get_attribute("innerHTML").startswith("<s"):
                    prox = True
                else:
                    e = span
                    break
            tupla =(e.get_attribute("innerHTML"), evento_url, esporte_url)
            print(tupla)
            eventos.append(tupla)
        with open("scrapping/eventos_pt.csv", 'w'):
            w = csv.writer(f, lineterminator='\n')
            w.writerow(["evento_pt", "evento_id", "esporte_url"])
            w.writerows(eventos)
            

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.implicitly_wait(1.5)
    driver.get("https://olympics.com")
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    get_events_pt(driver)

    

