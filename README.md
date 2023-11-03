# Guia de Instalação e Uso - Seu Projeto Django com API Django Rest Framework

Este guia fornece instruções detalhadas para configurar e executar o seu projeto Django com a API Django Rest Framework. Certifique-se de seguir os passos abaixo para garantir o funcionamento adequado do projeto.

## Requisitos

Este projeto utiliza dependências que podem não ser funcionais em todas as versões do Python. Portanto, recomendamos que você tenha o Python na versão 3.10.0 ou superior. Você pode usar o Pyenv para gerenciar as versões do Python. Para mais informações, siga o nosso tutorial sobre a instalação e uso do Pyenv.

⚠️ **ATENÇÃO**: Nunca remova versões antigas do Python instaladas em seu sistema, pois o seu sistema operacional pode depender delas! ⚠️

### Instalação da Dependência `mysqlclient`

Para instalar a dependência `mysqlclient`, certifique-se de que algumas bibliotecas estejam presentes no seu sistema operacional, dependendo do sistema que você está usando:

#### Debian/Ubuntu
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
```
macOS

```bash
brew install mysql pkg-config
```

### Configurando o Ambiente Virtual

Crie um ambiente virtual:

```bash
python3 -m venv .venv
```
### Ative o ambiente virtual:

```bash
source .venv/bin/activate
```
#### Instale as dependências no ambiente virtual a partir do arquivo dev-requirements.txt:

```bash
python3 -m pip install -r dev-requirements.txt
```
### Executando o Projeto

#### Construa a imagem Docker para o banco de dados:

```bash
docker build -t spotnews-db .
```
#### Execute o contêiner do MySQL:

```bash
docker run -d -p 3306:3306 --name=spotnews-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=spotnews_database spotnews-db
```

### Migrations e Seeding

Aplique as migrações do banco de dados:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runscript seeds
```
### Iniciando o Servidor

Na raiz do projeto, inicie o servidor Django:

```bash
python3 manage.py runserver
```

### Rotas
#### Cadastro e Acesso às Informações

Usuários:
```bash 
localhost:8000/api/users
```
Notícias:
```bash
localhost:8000/api/news
```
Categorias:
```bash
localhost:8000/api/categories
```
Atualização e Exclusão de Dados

Você pode atualizar e excluir dados específicos acessando as seguintes URLs:

Usuários:
```bash
localhost:8000/api/users/id (por exemplo, /api/users/1, /api/users/2)
```
Notícias:
```bash
localhost:8000/api/news/id (por exemplo, /api/news/1, /api/news/2)
```
Categorias:
```bash
localhost:8000/api/categories/id (por exemplo, /api/categories/1, /api/categories/2)
```
