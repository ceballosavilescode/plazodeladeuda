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
		archivo = filedialog.askopenfilename(
			title="Selecciona un archivo Excel",
			filetypes=(("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*"))
		)
		print("archivo:::::", archivo)
		devengo = pd.DataFrame()
		for f in glob.glob(archivo): # "../mejorninez/input_excel/pagoManual/*",
			df = pd.read_excel(f, converters={ 'folio': str, 'Nº CDP': str, 'Monto Total': int } )
			print('Procesando  : ', f)
			devengo = pd.concat([devengo, df], ignore_index=True)

		devengo['CodProyecto']  =  devengo['Cod. Proyecto']
		devengo['MesAtencion']  =  devengo['Mes Atención']
		devengo['Estatus']  	=  "Pendiente"
		devengo['Diferencia']  	=  "Pendiente"
		del devengo['observacion']  

		print(devengo)

		self.crear_database(devengo)

	def crear_database(self, devengo):
		metadata = sqlalchemy.MetaData()
		engine = sqlalchemy.create_engine('sqlite:///proyectos.db', echo=False)
		metadata = sqlalchemy.MetaData()

		Asigfe = sqlalchemy.Table(
			'CodProyectos',
			metadata,
			sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
			sqlalchemy.Column('folio', sqlalchemy.String),
			sqlalchemy.Column('Estatus', sqlalchemy.String)
		)

		metadata.create_all(engine)

		self.insertar_Datos(devengo, engine)

	def insertar_Datos(self, devengo, engine):
		devengo.to_sql('CodProyectos', engine, if_exists='replace')
