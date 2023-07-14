import os

class File:

	# Método construtor recebe o caminho e o nome do arquivo:
	def __init__(self, path, name, columns):
		self.file_path = path
		self.file_name = name
		self.columns = columns
		self.check()

	# Verificando se há ou não o arquivo responsável para armazenar os dados:
	def check(self):
		# Concatenando caminho + nome do arquivo:
		file = self.file_path + self.file_name
		
		# Formatando a lista de titulos separadas por ";":
		titles = ";".join(self.columns) + "\n"

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
	
	# Criar linha e armazenar no arquivo:
	def create_line(self, datas):
		# Concatenando caminho + nome do arquivo:
		file = self.file_path + self.file_name
		with open (file, 'a') as document:

			# Percorrendo as linhas procurando a chave de acordo com a lista de colunas:
			for data in  datas:

				# Criando uma lista temporária para armazenar os dados de cada objeto:
				array_temp = list()
				for column in self.columns:
					array_temp.append(data[column])

				# Formatando o array para string separadas por ";" e armazenando no arquivo:
				data_temp = ";".join(array_temp) + "\n"
				document.write(data_temp)

# Testando a classe de arquivos:
file_path = "../datas/"
file_name = "users.csv"
columns = ['name', 'last_name', 'city', 'country', 'email', 'telephone']

datas = [
	{'name':'luis', 'last_name': 'felipe', 'city':'são paulo', 'country': 'Brasil', 'email': 'luis@email.com', 'telephone':'19999999999'},
	{'name':'felipe', 'last_name': 'zeca', 'city':'são paulo', 'country': 'Brasil', 'email': 'felipe@email.com', 'telephone':'19999999999'},
	{'name':'zeca', 'last_name': 'luis', 'city':'são paulo', 'country': 'Brasil', 'email': 'zeca@email.com', 'telephone':'19999999999'},
]

file = File(file_path, file_name, columns)
file.create_line(datas)