from app.config.env import Config
from manager import init
import os

config_name = os.getenv('FLASK_CONFIG', 'default')


def create_app():
    app = init(config_name)

    # manage = Manager(app)
    # manage.add_command('runserver', Server(host='localhost', port=9000))

    # manage.add_command('db', MigrateCommand)

    app.run(port=Config.Server_Port)
    # manage.run()


if __name__ == '__main__':
    create_app()
