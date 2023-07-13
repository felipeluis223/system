import os

class File:

	# Método construtor recebe o caminho e o nome do arquivo:
	def __init__(self, path, name):
		self.file_path = path
		self.file_name = name

	# Verificando se há ou não o arquivo responsável para armazenar os dados:
	def check(self, columns):
		# Concatenando caminho + nome do arquivo:
		file = self.file_path + self.file_name
		
		# Formatando a lista de titulos separadas por ";":
		titles = ";".join(columns)

		# Caso exista o arquivo:
		if (os.path.isfile(file)):
			# Lendo a primeira linha do arquivo:
			with open(file, 'r') as document:
			    first_line = document.readline().strip()
			    
			# Compara a primeira linha com a variável de titulos:
			if (first_line == titles): 
				print('Arquivo verificado com sucesso!')
			else: 
				print('Ops! Titulos diferentes.')

		# Caso não exista o arquivo:
		elif not (os.path.isfile(file)):
			# Criando a primeira linha - titulos:
			with open(file, "w") as document:
				# Armazenando no arquivo ".csv":
				document.write(titles)
		


# Testando a classe de arquivos:
file_path = "../datas/"
file_name = "users.csv"
columns = ['name', 'last_name', 'city', 'country', 'email', 'telephone']

file = File(file_path, file_name)
file.check(columns)
