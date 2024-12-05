import sqlalchemy
import pandas as pd
import glob
from lib.fuente import Fuente
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlalchemy
from datetime import datetime

class Database(object):
	def __init__(self):
		
		self.parse_Excel()
		
	def parse_Excel(self):
		devengo = pd.DataFrame()
		for f in glob.glob("../interfaz/input_excel/pagoManual/*"): # "../mejorninez/input_excel/pagoManual/*",
			df = pd.read_excel(f, converters={ 'folio': str, 'Nº CDP': str, 'Monto Total': int } )
			print('Procesando  : ', f)
			devengo = pd.concat([devengo, df], ignore_index=True)

		devengo['CodProyecto']  =  devengo['Cod. Proyecto']
		devengo['MesAtencion']  =  devengo['Mes Atención']
		devengo['Estatus']  	=  "Pendiente"
		devengo['Diferencia']  	=  "Pendiente"
		del devengo['observacion']  

		print(devengo)

