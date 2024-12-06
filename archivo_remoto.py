from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SisValidacion80Bis:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        self.driver = None

    def iniciar_sesion(self):
        print(f"Iniciando sesión con nombre: {self.nombre} y contraseña: {self.contraseña}")
        self.driver = webdriver.Chrome()  # Inicializar ChromeDriver
        self.driver.get("https://www.example.com/login")  # URL de ejemplo
        
        # Localizar y llenar campos de usuario y contraseña
        self.driver.find_element(By.ID, "username").send_keys(self.nombre)
        self.driver.find_element(By.ID, "password").send_keys(self.contraseña)
        
        # Enviar formulario
        self.driver.find_element(By.ID, "loginButton").click()
        time.sleep(5)  # Esperar para observar el resultado

    def cerrar(self):
        if self.driver:
            self.driver.quit()
