# Projeto pessoal: site integrado com ferramentas de gerenciamento de leads e banco de dados relacional.

Chamei este projeto Python+Django Framework de "rocketsystem", acesse o projeto pela url:
- http://rocketsystem.tech/

### Fiz as seguintes integrações:
1) Webhook do Pipedrive (CRM - funil de vendas);
2) API do Pipedrive (CRM - funil de vendas);
3) Banco de Dados Mysql;

### Eventos (webhook):
1) Um evento é disparado pelo webhook trafegando dados de PERSON em json possibilitando utilizar os dados em diversos aplicativos e automações;
2) Um evento é disparado pelo webhook trafegando dados de DEAL em json possibilitando utilizar os dados em diversos aplicativos e automações;
3) Os dados dos eventos são tratados e armazenados em um banco de dados relacional;

### Eventos (api):
1) O usuário pode alterar dados de PERSON e DEAL pelo front-end através da API oficial do Pipedrive;
2) O usuário pode criar novo PERSON e DEAL pelo front-end através da API oficial do Pipedrive;

<br>

# RUN PROJECT
### Para rodar este projeto siga as instruções:

1) crie o arquivo "config_app.py" no diretório do projeto "pjt_pipedrive", este arquivo deve estar na mesma hierarquia que os apps:

-- pjt_pipedrive<br>
--- > ./app_webhook<br>
---> ./app...<br>
---> ./app...<br>
--- > ./pjt_pipedrive<br>
--- > config_app.py

### Aplique as configurações a seguir:
<pre>
SECRET_KEY = 'django-insecure-....crie uma chave segura'
DEBUG = True ou False
ALLOWED_HOSTS = ["hosts_permitidos ex: http://127.0.0.1/"]
CSRF_TRUSTED_ORIGINS = ["hosts_permitidos ex: http://127.0.0.1/"]
STATIC_ROOT = "seu diretório de arquivos estáticos..ex: C:/Users/.../pipedrive/app_webhook/static/"

CONN_REMOTE_DATABASE = True ou False
# -> TRUE  para host externo
# -> FALSE para db.sqlite3

DB_HOST = "host_database"
DB_USER = "nome_usuario_db"
DB_PASSWORD = "senha_usuario_db"
DB_NAME = "nome_banco_dados"
DB_PORT = "ex: 3306"
DB_ENGINE = "django.db.backends.mysql" # exemplo de banco de dados
# para outros tipos de banco de dados acesse:
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

COMPANY_DOMAIN = 'nome do company_domain do pipedrive...ex: rocket_system_app'
API_TOKEN = 'token_api da sua conta Pipedrive'

</pre>