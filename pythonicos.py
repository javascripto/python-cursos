#!/usr/bin/python
# coding: utf-8
# python inline: python -c "print('ola'); input()"

def pythonicos05():
  ip = raw_input('Digite um endereço IP: ')
  print "O endereço %s é um endereço válido" %ip
  print "O endereço %s tem %d caracteres" %(ip, len(ip))
  # print "O numero %f é um número do tipo float" %3.141592653589793
  # print "O numero %.2f é um número do tipo float" %3.141592653589793

def atribuicao_multipla():
  # list()
  dados =  ['yuri', 'alves', 24, 'trancoso' ]
  nome, sobrenome, idade, cidade = dados 
  print nome
  print sobrenome
  print idade
  print cidade

def metodos_lista():
  # Listas são como arrays de outras linguagens, porem arrays com indices numéricos
  a = [1,2,3]
  b = [4,5,6]
  c = a + b   # concatenando em terceira variavel

  d = a       # atribuição de endereço
  d = a[:]    # clonagem de valores
  d.extend(b) # concatenando com efeito colateral na variavel
  a.index(2)  # retorna valor correspondente ao indice 
  a.append(4) # acrescenta valor em nova posição no fim da lista
  posicao = 4
  a.insert(posicao, "texto") # insere valor em determinada posição. Não substitui valor existente, cria um novo
  a.insert(posicao+1, "texto2")
  a.remove("texto")         # remove primeira ocorrência de um valor
  a.pop()                   # remove ultimo elemento da lista, ou elemento correspondente ao indice passado como argumento
  # del a[0]                  # del não é método, é função e utiliza o indice
  a.sort()                  # ordenação com efeito colatera
  a.reverse()               # inverte lista com efeito colateral
  # a[::-1]                   # reversao sem efeito colateral. gera copia da lista ao contrario
  a.count(1)                # count() retorna numero de vezes um item se repete.
  # Diferente da função len que conta a quantidade de elementos de uma lista ou caracteres em uma string

def tuplas():
  # Parece com lista mas é tupla. valores imutaveis. tuple()
  t = (1,2,3,4,5,6,7,8,9)
  tupla_de_um_item = ("Item",) # pecisa da virgula se não faz um split da string

def dicionarios():
  # dicionarios são como listas e tuplas. Se parecem com arrays associativos com uma chave e valor. dict()
  var1 = {'nome': 'yuri', 'idade': 24}
  var2 = {'idade': 24, 'nome': 'yuri'}
  print var1 == var2 # True - mesmo que em ordem diferente

  # Métodos:
  var1.keys()   # retorna indices do dicionario
  var1.values() # retorna valores do dicionario
  var1.items()    # retorna tuplas para cada item contendo a chave e o valor

  # iterando com for
  for k,v in var1.items():
    print k,': ',v

  for i in var1:
    print i,': ', var1[i]

  # Verificar se chave existe no dicionario
  if 'nome' in var1:
    print var1['nome']

  print var1.get('nome', 'Indice não encontrado') # mesmo que console.log(var1['nome'] || 'Indice não encontrado') no javascript 

  # metodo setdefault('cahve', 'valordefault')

def trabalhando_strings():
  string1 =   'It\'s a dog\nIsso é um cachorro\n' # no python2 sem unicode no windows
  string2 =  u'It\'s a dog\nIsso é um cachorro\n' # unicode
  string3 =  r'It\'s a dog\nIsso é um cachorro\n' # raw
  string4 = ur'It\'s a dog\nIsso é um cachorro\n' # unicode e raw

  print string1, string2, string3, string4

  'Ola Mundo'.istitle() # verifica se a primeira letra de cada plavra está em caixa alta

  # split
  nome = "Yuri Alves de Almeida"
  palavras = nome.split(' ') # para o caractere espaço não é necessario nem passar como parametro. ex "yuri alves".split()
  nomeSplit = list(nome) # mesmo que nome.split("") em outras linguagens

# Aula 15 - Funções
var = 'minha variavel'

def funcao_com_retorno_multiplo():
  return 1, 2

def usando_var_global():
  global var
  print var

def conta(x):
  try:
      print 10/x
  except Exception as e:
    print 'Error: ', str(e)

def aula15():
  # teste funcao_com_retorno_multiplo
  var1, var2 = funcao_com_retorno_multiplo()
  print var1
  print var2
  # teste usando_var_global
  var = 2
  usando_var_global()
  # teste exception
  conta(2) # 5
  conta(0) # Erro:  integer division or modulo by zero

# from time import *
# Para importar arquivos em subdiretorios coloque um arquivo '__init__.py' dentro dos subdiretorios e importe assim:
# from pasta.subdir.arquivo import funcao_x

def moduloOS():
  import os
  from time import sleep
  # from time import sleep, timezone
  
  sleep(1)

  files = ['arquivo.txt', 'package.json', 'main.js', 'musica.mp3']

  for file in files:
    print os.path.join(os.getcwd(), file)


  oldpath = os.getcwd() # current working directory
  os.chdir('../')       # cd
  print os.getcwd()
  os.chdir(oldpath)
  print os.getcwd()

  # Criando, renomeando, movendo, removendo diretorios
  os.makedirs('Nova Pasta')
  os.mkdir('Nova Pasta 2')
  # sleep(1)
  os.rename('Nova Pasta 2', 'Nova Pasta\\Nova 2') # Movendo e renomeando
  # sleep(1)
  os.rename('Nova Pasta\\Nova 2', 'Nova Pasta 2') # Movendo denovo
  # sleep(1)
  os.rmdir('Nova Pasta')
  os.rmdir('Nova Pasta 2')

  # Listando diretorios
  for item in os.listdir(os.getcwd()):
    print item

  # path absoluto
  print os.path.abspath('teste') # C:\\Users\\Yuri\\teste
  # path relativo
  print os.path.relpath(os.path.abspath('C:\\Program Files'), os.getcwd())


  print os.path.dirname('/usr/bin/sh') # /usr/bin
  print os.path.basename('/usr/bin/sh') # sh

  os.path.isdir(os.getcwd())
  os.path.isfile(os.getcwd())

def arquivos():
  file = '../../Desktop/arquivo.txt'

  f = open(file)
  print type(f)
  print f

  # iterando linhas
  for line in f:
    print line.strip() # strip deve remover as quebras de linhas, porem o comando print inclui quebras a cada iteração

  # Apos esta iteração, é necessario abrir o arquivo novamente para que o cursor de iteração volte ao inicio
  f = open(file)
  raw_string =  f.read() # uma vez executado este método percorrendo as linhas do arquivo, o cursor nao volta ao inicio
  raw_string # no terminal iterativo é impresso a string crua
  print raw_string # com print a string é impressa já formatada com quebras de linhas
  for char in raw_string: # iterando sobre cada caractere do arquivo
    print char


  f = open(file)
  lines = f.readlines() # retorna uma lista com as linhas
  print ''.join(lines)

  for line in lines:
    print line 

  for line in lines:
    print line.strip()


def escrevendo_arquivos():
  # w - write()
  # a - add/append
  # r - read - opção default, não é necessario declarar
  # b - binary
 
  # Escrevendo
  f = open('teste.txt', 'w')
  f.write('Olá, mundo\n')
  f.write('linha 2\n')
  f.close()

  # Adicionando
  f = open('teste.txt', 'a')
  f.write('Com a opção \'a\', o texto não é sobrescrito cada vez que o arquivo é aberto\n')
  f.close()

  # Salvando binário
  import requests
  url = 'http://downloads.sourceforge.net/gnuwin32/wget-1.11.4-1-setup.exe'
  r = requests.get(url)
  f = open('wget.exe', 'ab')
  f.write(r.content)
  f.close()

def copiando_arquivos_e_pastas():
  import shutil # Shell Util
  import os

  os.listdir()
  shutil.copy('arquivo.txt', 'arquivo-copia.txt')
  shutil.move('arquivo.txt', './nova-pasta/arquivo-movido.txt')
  os.unlink('arquivo.txt') # Apagar arquivo
  os.rmdir('./nova-pasta') # Apagar pasta vazia
  shutil.rmtree('./nova-pasta-2') # Apagar pastas com seus arquivos e subpastas   

def simulando_ls(): # ls -R com generator os.walk()
  import os
  for pasta, subpastas, arquivos in os.walk('./linux'):
    print 'Pasta atual %s' %pasta
    for subpasta in subpastas:
      print '%s/%s' %(pasta, subpasta)
    for arquivo in arquivos:
      print '%s/%s' %(pasta, arquivo)


def endLinePython2():
  for i in range(0, 10):
    print i, ' - '

  print 10,

  
def alternativaPrint():
  import sys
  sys.stdout.write(" ".join(sys.argv) + '\n')


def arquivosZipados():
  import zipfile
  zipado = zipfile.ZipFile('backup2018.zip')
  zipado.namelist()

  for file in zipado.namelist():
    print file

  info = zipado.getinfo('arquivo.txt')
  print dir(info) # Ver atributos do objeto

  print info.file_size
  print info.compress_size

  zipado.extractall()
  zipado.extract('arquivo.txt')
  zipado.extract('arquivo.txt', '/var/www/html/destino')

  zipado.close()

def arquivosZipados2():
  # Criar arquivo zipado e adicionar conteudo
  import zipfile
  zipbkp = zipfile.ZipFile('backup.zip', 'w')
  zipbkp.write('arquivo1.txt')
  zipbkp.close()


def _subprocess():
  import subprocess

  # subprocess.call('ls')
  # subprocess.call('ls -alt', shell=True)
  # subprocess.call(['ls', '-alt'])

  # subprocess.check_call(['false'])

  objPopen = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  # print dir(objPopen)
  retorno = objPopen.communicate() # tupla com result e erro
  print retorno[0]


# socket() - Módulo onde é possível criar servidores TCP e UDP, e mais algumas coisas interessantes
def servidorTCP():
  # import socket
  # ip = socket.gethostbyname('facebook.com')   # nome para IP
  # host = socket.gethostbyaddr(ip)             # IP para nome
  # print(ip, host)
  # print(socket.gethostname())                 # retorna nome do pc local 
  # print(socket.getservbyport(80))             # retorna nome do serviço (http)
  # print(socket.getservbyname('domain'))       # retorna porta do serviço (53)

  import socket

  ip = '127.0.0.1'
  porta = 2222

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria socket
  s.bind((ip, porta)) # Define porta que vai ser aberta
  s.listen(5) # Armazenando em uma fila antes de receber o accept()

  while True:
    conn, addr = s.accept() # Aceita uma conexão removendo da lista do listen()
    conn.send('Bem vindo ao seu primeiro servidor TCP\n')
    print('Conexão de %s:%d' %(addr[0], addr[1]))
    conn.send('>>>')
    msg = conn.recv(1024)
    print('Mensagem Recebida: %s' %msg)
    conn.close()
    break

  s.close()
  
  # Testado no linux com netcat:
  # nc 127.0.0.1 2222
  # >>>olá

