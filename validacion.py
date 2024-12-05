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
