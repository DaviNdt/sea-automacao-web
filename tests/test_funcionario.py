import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#valido no final se o funcionário realmente foi criado
import requests

#para a conversão da data que gerei com o faker
import time

def data_br(data):
    return data.strftime("%d%m%Y")

#para a criação de dados mock
from faker import Faker
fake = Faker()

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    

    driver.set_page_load_timeout(30)

    yield driver

    driver.quit()

def test_adicionar_funcionario (driver):
<<<<<<< HEAD
    driver.get("")
=======
    driver.get("11")
>>>>>>> cee5f33 (Update URL in test_adicionar_funcionario)
    botao_adicionar_funcionarios = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[contains(., '+ Adicionar Funcionário')]")
        )
    )
    botao_adicionar_funcionarios.click()

    seletor_dispo = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[2]/button/span")
        )
    )

    seletor_dispo.click()


    campo_nome = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[3]/div/div[1]/input")
        )
    )
    nome = fake.name()
    campo_nome.send_keys(nome)

    campo_cpf = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[3]/div/div[3]/input")
        )
    )
    cpf = fake.random_number(digits= 11)
    campo_cpf.send_keys(cpf)

    campo_rg = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[3]/div/div[5]/input")
        )
    )
    rg = fake.random_number(digits= 7)
    campo_rg.send_keys(rg)

    seletor_sexo_fem = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[3]/div/div[2]/div/label[2]/span[2]")
        )
    )
    seletor_sexo_fem.click()

    seletor_sexo_masc = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[3]/div/div[2]/div/label[1]/span[2]")
        )
    )
    seletor_sexo_masc.click()

    data_nasc = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[3]/div/div[4]/input")
        )
    )
    data = fake.date_of_birth()
    data_nasc_faker = data_br(data)
    data_nasc.send_keys(data_nasc_faker)

    seletor_cargo = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[3]/div/div[6]/div/div/span[2]")
        )
    )
    seletor_cargo.click()

    cargo3 = WebDriverWait(driver, 10).until(
        lambda d: next(
            (
                e for e in d.find_elements(
                    By.CSS_SELECTOR,
                    ".ant-select-item-option-content"
                )
                if e.text.strip() == "Cargo 03"
            ),
            False
        )
    )
    cargo3.click()

    booleano_epi = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[4]/div/label/span[2]")
        )
    )

    booleano_epi.click()
    time.sleep(2)
    booleano_epi.click()

    seletor_atividade = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[4]/div/div/div[1]/div/div/span[2]")
        )
    )
    seletor_atividade.click()

    ativid03 = WebDriverWait(driver, 10).until(
        lambda d: next(
            (
                e for e in d.find_elements(
                    By.CSS_SELECTOR,
                    ".ant-select-item-option-content"
                )
                if e.text.strip() == "Ativid 03"
            ),
            False
        )
    )
    ativid03.click()

    seletor_epi = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[4]/div/div/div[2]/div/div[1]/div/div/span[2]")
        )
    )
    seletor_epi.click()

    epi = WebDriverWait(driver, 10).until(
        lambda d: next(
            (
                e for e in d.find_elements(
                    By.CSS_SELECTOR,
                    ".ant-select-item-option-content"
                )
                if e.text.strip() == "Calçado de Segurança"
            ),
            False
        )
    )
    epi.click()

    campo_ca = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[4]/div/div/div[2]/div/div[2]/input")
        )
    )
    campo_ca.click()

    ca = fake.random_number(digits= 10)
    campo_ca.send_keys(ca)

    botao_salvar = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/button")
        )
    )
    botao_salvar.click()

    # valida se o funcionario foi realmente criado via API

    # função
    def buscar_funcionario(cpf, timeout=50):
        inicio = time.time()

        while time.time() - inicio < timeout:
            try:
                response = requests.get(
                    "https://analista-teste.seatecnologia.com.br/employees",
                    timeout=10
                )

                if response.status_code in (502, 503, 504):
                    print(
                        f"API retornou {response.status_code}. "
                        "Tentando novamente..."
                    )
                    time.sleep(0.5)
                    continue

                response.raise_for_status()

                funcionarios = response.json()

                for funcionario in funcionarios:
                    employee = funcionario.get("state", {}).get("employee", {})

                    if employee.get("cpf") == str(cpf):
                        print("Funcionário encontrado na API!")
                        return funcionario
                    
            except requests.exceptions.RequestException as erro:
                print(f"Erro ao consultar API: {erro}")
                time.sleep(1)

        return None

    # busca
    funcionario = buscar_funcionario(cpf, timeout=60)
    assert funcionario is not None, f"Funcionário com CPF {cpf} não foi encontrado"
    employee = funcionario["state"]["employee"]
    assert employee is not None
    assert employee ["name"] == nome
    assert employee ["rg"] == str(rg)

    # print para demonstração
    print(funcionario)
