import os  # Importa el módulo os para interactuar con funcionalidades del sistema operativo
from flask_admin import Admin  # Importa la clase Admin de Flask-Admin para configurar la interfaz de administración
from models import (  # Importa los modelos y la instancia de base de datos desde el módulo models
    db, Users, Personajes, Vehiculos, Planetas,
    Favoritos_personajes, Favoritos_vehiculos, Favoritos_planetas
)
from flask_admin.contrib.sqla import ModelView  # Importa ModelView para crear vistas de modelo en Flask-Admin

def setup_admin(app):
    """
    Configura la interfaz de administración de Flask-Admin para la aplicación Flask.

    Args:
        app (Flask): Instancia de la aplicación Flask.
    """
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')  # Configura la clave secreta de la aplicación Flask
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'  # Configura el tema de la interfaz de administración

    # Crea una instancia de Admin para la aplicación con nombre y modo de plantilla especificados
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    # Agrega vistas de modelo para cada modelo a la interfaz de administración
    admin.add_view(ModelView(Users, db.session))
    admin.add_view(ModelView(Personajes, db.session))
    admin.add_view(ModelView(Vehiculos, db.session))
    admin.add_view(ModelView(Planetas, db.session))
    admin.add_view(ModelView(Favoritos_personajes, db.session))
    admin.add_view(ModelView(Favoritos_vehiculos, db.session))
    admin.add_view(ModelView(Favoritos_planetas, db.session))

    # Puedes duplicar esta línea para agregar más modelos a la interfaz de administración
    # admin.add_view(ModelView(YourModelName, db.session))
