print(f"el usuario se registro como 03 : {{ usuario }}")

# Variable usuario
usuario1 = {{ usuario }}

print(f"El usuario se registró como: ", usuario1)

if usuario1 == 'ceballos':
	print(f"El usuario {usuario} cumple con la condición. Abriendo página web...")
	# URL de la página que deseas abrir
	url = "https://corpuslux.blogspot.com/2023/06/ga028-el-curso-de-mi-vida-cap-iii-anos.html"
	
	# Comando para abrir la página web en el navegador predeterminado
	if os.name == "nt":  # Windows
	os.system(f"start {url}")
	elif os.name == "posix":  # macOS o Linux
	os.system(f"open {url}")

	
	devengo = pd.DataFrame()
	for f in glob.glob("../interfaz/input_excel/pagoManual/*"): # "../mejorninez/input_excel/pagoManual/*",
		df = pd.read_excel(f, engine='openpyxl', converters={'folio': str, 'Nº CDP': str, 'Monto Total': int})
		print('Procesando  : ', f)
		devengo = pd.concat([devengo, df], ignore_index=True)

	devengo['CodProyecto']  =  devengo['Cod. Proyecto']
	devengo['MesAtencion']  =  devengo['Mes Atención']
	devengo['Estatus']  	=  "Pendiente"
	devengo['Diferencia']  	=  "Pendiente"
	del devengo['observacion']  

	print(devengo)

	metadata = sqlalchemy.MetaData()
	engine = sqlalchemy.create_engine('sqlite:///DBGITHUB.db', echo=False)
	metadata = sqlalchemy.MetaData()

	Asigfe = sqlalchemy.Table(
		'CodProyectos',
		metadata,
		sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
		sqlalchemy.Column('folio', sqlalchemy.String),
		sqlalchemy.Column('Estatus', sqlalchemy.String)
	)

	metadata.create_all(engine)
	devengo.to_sql('CodProyectos', engine, if_exists='replace')
else:
	print("============== NO PUSISTE LA PALABRA CORRECTA ==============")
