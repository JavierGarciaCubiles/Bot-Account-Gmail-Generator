# Gmail Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)
# -- MODIFIED SCRIPT by Javier Garcia Cubiles --

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random
import time
from unidecode import unidecode

# Chrome options
chrome_options = ChromeOptions()
chrome_options.add_argument("--disable-infobars")

# WebDriver service
service = ChromeService('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

french_first_names = [
    "Amélie", "Antoine", "Aurélie", "Benoît", "Camille", "Charles", "Chloé", "Claire", "Clément", "Dominique",
    "Élodie", "Émilie", "Étienne", "Fabien", "François", "Gabriel", "Hélène", "Henri", "Isabelle", "Jules",
    "Juliette", "Laurent", "Léa", "Léon", "Louise", "Lucas", "Madeleine", "Marc", "Margaux", "Marie",
    "Mathieu", "Nathalie", "Nicolas", "Noémie", "Olivier", "Pascal", "Philippe", "Pierre", "Raphaël", "René",
    "Sophie", "Stéphane", "Suzanne", "Théo", "Thomas", "Valentin", "Valérie", "Victor", "Vincent", "Yves",
    "Zoé", "Adèle", "Adrien", "Alexandre", "Alice", "Alix", "Anatole", "André", "Angèle", "Anne",
    "Baptiste", "Basile", "Bernard", "Brigitte", "Céleste", "Céline", "Christophe", "Cyril", "Denis", "Diane",
    "Édouard", "Éléonore", "Émile", "Félix", "Florence", "Georges", "Gérard", "Guillaume", "Hugo", "Inès",
    "Jacques", "Jean", "Jeanne", "Joséphine", "Julien", "Laure", "Lucie", "Maëlle", "Marcel", "Martine",
    "Maxime", "Michel", "Nina", "Océane", "Paul", "Perrine", "Quentin", "Romain", "Solène", "Thérèse"
]

french_last_names = [
    "Leroy", "Moreau", "Bernard", "Dubois", "Durand", "Lefebvre", "Mercier", "Dupont", "Fournier", "Lambert",
    "Fontaine", "Rousseau", "Vincent", "Muller", "Lefèvre", "Faure", "André", "Gauthier", "Garcia", "Perrin",
    "Robin", "Clement", "Morin", "Nicolas", "Henry", "Roussel", "Mathieu", "Garnier", "Chevalier", "François",
    "Legrand", "Gérard", "Boyer", "Gautier", "Roche", "Roy", "Noel", "Meyer", "Lucas", "Gomez",
    "Martinez", "Caron", "Da Silva", "Lemoine", "Philippe", "Bourgeois", "Pierre", "Renard", "Girard", "Brun",
    "Gaillard", "Barbier", "Arnaud", "Martins", "Rodriguez", "Picard", "Roger", "Schmitt", "Colin", "Vidal",
    "Dupuis", "Pires", "Renaud", "Renault", "Klein", "Coulon", "Grondin", "Leclerc", "Pires", "Marchand",
    "Dufour", "Blanchard", "Gillet", "Chevallier", "Fernandez", "David", "Bouquet", "Gilles", "Fischer", "Roy",
    "Besson", "Lemoine", "Delorme", "Carpentier", "Dumas", "Marin", "Gosselin", "Mallet", "Blondel", "Adam",
    "Durant", "Laporte", "Boutin", "Lacombe", "Navarro", "Langlois", "Deschamps", "Schneider", "Pasquier", "Renaud"
]

# Randomly select a first name and a last name
your_first_name = random.choice(french_first_names)
your_last_name = random.choice(french_last_names)

# Generate a random number
random_number = random.randint(1000, 9999)

# Retirer les accents des prénoms et nom de famille
your_first_name_normalized = unidecode(your_first_name).lower()
your_last_name_normalized = unidecode(your_last_name).lower()

your_username = f"{your_first_name_normalized}.{your_last_name_normalized}{random_number}"

your_birthday = "02 3 1989" #dd m YYYY exp : 24 11 2003
your_gender = "1" # 1:F 2:M 3:Not say 4:Custom
your_password = "x,nscldsj123...FDKZ"

def fill_form(driver):
    try:
        driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        wait = WebDriverWait(driver, 20)

        # --- Paso 1 y 2 (Sin cambios) ---
        first_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        first_name_field.send_keys(your_first_name)
        last_name_field = driver.find_element(By.NAME, "lastName")
        last_name_field.send_keys(your_last_name)
        try:
            next_button_fn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Siguiente')]")))
            next_button_fn.click()
        except: pass
        print("full name fields filled successfully")

        day_field = wait.until(EC.visibility_of_element_located((By.ID, "day")))
        year_field = driver.find_element(By.ID, "year")
        birthday_elements = your_birthday.split()
        day_field.send_keys(birthday_elements[0])
        year_field.send_keys(birthday_elements[2])
        month_dropdown = driver.find_element(By.ID, "month")
        month_dropdown.click()
        month_xpath = f"//ul[@aria-label='Mes']/li[@data-value='{birthday_elements[1]}']"
        wait.until(EC.element_to_be_clickable((By.XPATH, month_xpath))).click()
        gender_dropdown = driver.find_element(By.ID, "gender")
        gender_dropdown.click()
        gender_xpath = f"//ul[@aria-label='Género']/li[@data-value='{your_gender}']"
        wait.until(EC.element_to_be_clickable((By.XPATH, gender_xpath))).click()
        next_button_bd = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Siguiente')]")))
        next_button_bd.click()
        print("Birthday and Gender filled successfully")
        time.sleep(2)

        # --- Paso 3: Lógica flexible para la PRIMERA pantalla de elección ---
        try:
            print("[DEBUG] Comprobando si estamos en la Pantalla A ('Elige cómo iniciarás sesión')...")
            create_choice_selector = "div[jsname='CeL6Qc']"
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, create_choice_selector)))
            
            print("[INFO] Pantalla A detectada. Seleccionando opción y continuando...")
            create_own_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, create_choice_selector)))
            driver.execute_script("arguments[0].click();", create_own_option)
            
            next_button_A = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Siguiente')]")))
            next_button_A.click()
        except:
            print("[INFO] Pantalla A no detectada. Continuando...")
            pass
        
        # --- NUEVO PASO 3.5: Lógica para la SEGUNDA pantalla de elección ("Elige tu dirección") ---
        try:
            print("[DEBUG] Comprobando si estamos en la Pantalla B ('Elige tu dirección de Gmail')...")
            # Espera a que aparezca la opción "Crear dirección de Gmail personalizada"
            custom_address_xpath = "//div[contains(text(), 'Crear dirección de Gmail personalizada')]"
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, custom_address_xpath)))

            print("[INFO] Pantalla B detectada. Seleccionando la opción 'Crear dirección de Gmail personalizada'...")
            custom_address_option = wait.until(EC.element_to_be_clickable((By.XPATH, custom_address_xpath)))
            driver.execute_script("arguments[0].click();", custom_address_option)
            # Después de este clic, el campo de texto aparece en la misma página.
        except:
            print("[INFO] Pantalla B no detectada. Continuando...")
            pass

        # --- Paso 4: Creación del Username ---
        print("[DEBUG] Esperando a que aparezca el campo para el username...")
        username_input_xpath = "//input[@name='Username' and @type='text']"
        username_field = wait.until(EC.element_to_be_clickable((By.XPATH, username_input_xpath)))
        username_field.clear()
        username_field.send_keys(your_username)
        print(f"[DEBUG] Username '{your_username}' introducido.")
        
        next_button_user = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Siguiente')]")))
        driver.execute_script("arguments[0].click();", next_button_user)
        print("[DEBUG] Pasando a la sección de la contraseña.")

        # --- Paso 5: Contraseña y Final ---
        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        password_field.clear()
        password_field.send_keys(your_password)
        confirm_passwd_div = driver.find_element(By.ID, "confirm-passwd")
        password_confirmation_field = confirm_passwd_div.find_element(By.NAME, "PasswdAgain")
        password_confirmation_field.clear()
        password_confirmation_field.send_keys(your_password)
        
        next_button_final = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Siguiente')]")))
        driver.execute_script("arguments[0].click();", next_button_final)

        print(f"\n[SUCCESS] Gmail creado con éxito:\n{{\ngmail: {your_username}@gmail.com\npassword: {your_password}\n}}")
        

    except Exception as e:
        print("Falló la creación de tu Gmail, lo siento.")
        print(e)

# Execute the function to fill out the form
try:
    fill_form(driver)
finally:
    ### --- 5. AÑADIMOS driver.quit() AQUÍ --- ###
    # El navegador se cerrará al final de todo el proceso,
    # después de ambos registros, incluso si hay un error.
    print("\n[INFO] Proceso de automatización finalizado. Cerrando el navegador.")
    time.sleep(10) # Espera 10 segundos para ver el resultado final
    driver.quit()