# Django Project Password Generate

## Como usar?

Configure o ambiente do projeto com [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r requeriments.txt

# You may want to change the name `projectname`.
$ cd projectname/
$ python manage.py migrate
$ python manage.py runserver

##  Sobre o projeto

* Um projeto básico usando Django 3. Utilizando o conceito de rotas e o padrão de templates
* para criar um app que gerar senhar aleatórios para seu usuário 