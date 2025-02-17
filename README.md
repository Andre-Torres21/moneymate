Money Mate - Gerenciador de Finanças Pessoais

Descrição

O Money Mate é uma aplicação web desenvolvida para auxiliar no gerenciamento de finanças pessoais. O sistema permite o controle de despesas, entradas, transações, categorias e metas financeiras, além da geração de relatórios detalhados para uma melhor visualização das finanças do usuário. A aplicação oferece filtros avançados para facilitar a análise financeira e ajudar os usuários a tomarem decisões mais assertivas.

Funcionalidades

✅ Gerenciamento de Despesas – Registre e acompanhe seus gastos com categorização detalhada.
✅ Gerenciamento de Entradas – Controle suas fontes de receita de maneira eficiente.
✅ Gerenciamento de Transações – Visualize todas as movimentações financeiras em um só lugar.
✅ Gerenciamento de Categorias – Classifique despesas e receitas de forma personalizada.
✅ Metas Financeiras – Defina e monitore objetivos financeiros ao longo do tempo.
✅ Relatórios Mensais – Consulte relatórios financeiros com saldo atual, total de despesas e receitas.
✅ Filtragem Avançada – Busque e analise seus dados financeiros com filtros personalizados.

Tecnologias Utilizadas

🔹 Backend: Python, Django, PostgreSQL
🔹 Frontend: HTML, CSS, JavaScript, Bootstrap
🔹 Modelagem: UML (diagramas de caso de uso e de classes)
🔹 Versionamento: Git e GitHub
🔹 Gerenciamento do Projeto: SCRUM no Notion

Instalação e Configuração

1. Clone o Repositório

git clone https://github.com/seuusuario/money-mate.git
cd money-mate

2. Crie e Ative um Ambiente Virtual

python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate      # Para Windows

3. Instale as Dependências

pip install -r requirements.txt

4. Configure o Banco de Dados

Edite o arquivo settings.py e configure as credenciais do PostgreSQL. Em seguida, execute as migrações:

python manage.py migrate

5. Crie um Superusuário

python manage.py createsuperuser

6. Inicie o Servidor

python manage.py runserver

Acesse o sistema em: http://127.0.0.1:8000/

Hospedagem

O sistema pode ser implantado em serviços como Fly.io, Heroku, ou Railway, garantindo acessibilidade remota.

Contribuição

Sinta-se à vontade para contribuir! Faça um fork do repositório, crie uma branch e envie um pull request.

Licença

Este projeto está licenciado sob a MIT License.

💰 Money Mate – Controle suas finanças com segurança e praticidade!
