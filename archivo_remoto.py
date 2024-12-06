from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SisValidacion80Bis:
	def __init__(self, nombre, contraseña):
		self.nombre = nombre
		self.contraseña = contraseña
		self.driver = None

		print("		chrome_options = webdriver.ChromeOptions()=================")

		# Ruta al archivo chromedriver
		chromedriver_path = '/Users/hector/Documents/Documents/desarrollo/convenios_y_transferencias/webdriver/chromedriver'

		# Configuración de opciones de Chrome
		chrome_options = webdriver.ChromeOptions()
		prefs = {
			'download.default_directory': '/Users/hector/Documents/Documents/desarrollo/convenios_y_transferencias/input_excel/resolucionesUrgencia/pdfs',
			"download.prompt_for_download": False,
			"download.directory_upgrade": True,
			"safebrowsing_for_trusted_sources_enabled": False,
			"safebrowsing.enabled": False
		}
		chrome_options.add_experimental_option('prefs', prefs)
		chrome_options.add_argument('--ignore-certificate-errors')
		chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
		chrome_options.binary_location = '/Users/hector/Documents/Documents/desarrollo/convenios_y_transferencias/webdriver/chrome-mac/Chromium.app/Contents/MacOS/Chromium'  # Ruta a la versión de Chromium 114.0.5735.90

		# Configuración del servicio de ChromeDriver
		service = Service(executable_path=chromedriver_path)

		# Inicializar el driver de Chrome
		driver = webdriver.Chrome(service=service, options=chrome_options)
		driver.maximize_window()

		# Navegar a la URL deseada
		driver.get('https://www.sis.mejorninez.cl/')
