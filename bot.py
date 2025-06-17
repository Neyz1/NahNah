from selenium import webdriver
# Permet d'utiliser des touches du clavier tels que RETURN, F1, F2 etc ...
from selenium.webdriver.common.keys import Keys
# Permet de récuperer des informations dans un docs
from selenium.webdriver.common.by import By
import time
import random


# Création du Web driver pour CHROME
driver = webdriver.Chrome()

# Permet de charger la page que l'on veut. Pour que le sript commence, il faut que la page soit entièrement chargée.
driver.get("http://192.168.1.12")
print(driver.title)


# Génère les adresses mails et mots de passes

for i in range(1,150):  
    emails = f"user{i}@gmail.com"  
    passwords = f"Admin{i}"



# Remplit le champ email
    driver.find_element(By.NAME, 'email').clear()
    driver.find_element(By.NAME, 'email').send_keys(emails)


# Remplit le champ mot de passe
    driver.find_element(By.NAME, 'password').clear()
    driver.find_element(By.NAME, 'password').send_keys(passwords)

# Valide le formulaire
    continue_button = driver.find_element(By.CLASS_NAME, 'next-button')
    continue_button.click()

# Recharge la page.
    driver.get("http://192.168.1.12")


# Marque "No results found" si aucun résultat n'a été trouvé
assert "No results found." not in driver.page_source


driver.close()