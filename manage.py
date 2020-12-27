import os
import socket

from flask_script import Manager
#from flask_script import Server, Manager

from app.main import create_app
from app import blueprint

listen_port = 8000

print("hostname", socket.gethostname())
print("fqdn", socket.getfqdn())


app = create_app('dev')

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)



@manager.command
def run():
    app.run(debug=True, host='0.0.0.0', port=listen_port)
    #app.run(debug=False, host='0.0.0.0', port=listen_port)

if __name__ == '__main__':
    manager.run()
