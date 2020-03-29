# Django Celery, REST Framework & SocketIO template

API Gateway del proyecto encargado de distrubuir la información recopilada/generada a los diferentes servicios y microservicios.

## Especificaciones: técnicas

Las siguientes tecnolgias son implementadas en este proyecto:

- Integración de API's RESTful con Django REST Framework
- Integración Websockets con Python-SocketIO
- Tareas periodicas con Celery

La carpeta `apigateway` representa la configuración pricipal del proyecto donde se encuentra los siguientes archivos:
- En `settings.py` configuración principal y variables del proyecto.
- En `celery_app.py` configuración de celery para integrarse con Django.
- En `socket_app.py` eventos que se escuchan en el socket asi como los diferentes canales.
- Finalmente, `wsgi.py` configurado para ejecutar SocketIO con Django.

El proyecto consta de una app principal llamada `main` y que lleva el mismo nombre la carpeta.
Dentro de main podemos encontrar multiples archivos como una app de Django, los cuales serán mencionados brevemente los más importantes:

- En `models.py` se encuentran los modelos de base de datos que emplea el proyecto.
- En `serializers.py` se encuentran los serializadores de los modelos.
- En `tasks.py` se encuentran las tareas que Celery debe ejecutar en demanda o de manera periodica.
- En `utils.py` se encuentran utilerias y funciones que pueden reciclarse en el proyecto
- Finalmente, en `views.py` se encuentran las rutas que nuestro proyecto mapea ya sea como vistas o API's REST.

## Configuración

## Requisitos
- Tener instalado GIT.
- Python versión 3.6,>.
- Un entorno virtual listo para usar.

### Instalación

Al descargar el proyecto encontraremos un archivo llamado "requirements.txt" el cual contiene todas las dependencias Python para ejecutar el proyecto. 

Ejecutamos lo siguiente: 

    $ pip install -r requirements.txt

### Ejecución del proyecto
Para correr el servidor de scrapy y poder consumir los spiders, ejecutamos:

    $ python manage.py runserver

En otra terminal tenemos que activar el entorno virtual para correr

### Contenedores
Se proporciona el archivo `Dockerfile` y `docker-compose.yml` para ejecución del servicio desde contenedores de Docker.

`web`: servidor de django con integracion de socket.io

`worker`: servicio de celery para ejecutar tareas programadas

#### Ejecución

    $ docker-compose up

# Powered by Open Source Projects. 

Agradecemos enormemente el esfuerzo de las comunidades que mantienen el desarrollo de los siguientes proyectos.

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Python SocketIO](https://python-socketio.readthedocs.io/en/latest/)
- [Celery](http://www.celeryproject.org/)
- [Gunicorn](https://gunicorn.org/)
- [RabbitMQ](https://www.rabbitmq.com/)

# Despligue en Heroku
Para el despligue en la plataforma [Heroku]() se proporciona un archivo llamado `Procfile` con el comando de automatización de despligue del proyecto. Los comandos para cada servicio son los correspondientes para ejecutar en producción.

`Procfile`
```
web: gunicorn -k eventlet -w 1 --threads=5 apigateway.wsgi:application --log-level=debug
worker: celery worker -A apigateway -B --loglevel=INFO
```
`web`: servidor de django con integracion de socket.io

`worker`: servicio de celery para ejecutar tareas programadas

Make with love by [@RaulNovelo](https://github.com/RaulNovelo).
