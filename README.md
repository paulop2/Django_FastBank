FastBank - Aplicação Django
Banco de Dados
Esta aplicação utiliza o Laragon como ambiente de desenvolvimento e requer a criação de um banco de dados. Siga os passos abaixo para configurar o ambiente:

Instale o Laragon em seu sistema.

Crie um banco de dados utilizando o Laragon.

Crie um arquivo chamado ".env" e preencha-o com as configurações necessárias, utilizando o arquivo de exemplo ".env_exemplo" como referência.

Mantenha o Laragon rodando enquanto estiver utilizando a aplicação para garantir o funcionamento adequado.

Como Rodar o Programa
Siga as instruções abaixo para executar a aplicação:

bash
Copy code
git clone https://github.com/LauraPigosso/Django_FastBank.git
python -m venv venv 
.\venv\Scripts\activate
pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
Certifique-se de ter o Git e o Python instalados em seu ambiente antes de iniciar. Esses comandos garantirão que a aplicação seja configurada corretamente e pronta para ser executada.

Lembre-se de verificar regularmente as atualizações e as dependências do projeto para garantir um ambiente de desenvolvimento estável.