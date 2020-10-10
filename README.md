# Django Project Password Generate

## Como usar

Clonar no repositório: <https://github.com/hevertongomes/django-generate-password.git>

Configure o ambiente do projeto com [virtualenv](https://virtualenv.pypa.io) e [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r requeriments.txt

# Para rodar o projeto.
$ cd django-generate-password/
$ python manage.py migrate
$ python manage.py runserver

##  Sobre o projeto

* Um projeto básico usando Django 3. Utilizando o conceito de rotas e o padrão de templates
* para criar um app que gerar senhar aleatórios para seu usuário 