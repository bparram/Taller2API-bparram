from flask import Flask
from controller.c_hacer_sonido import controller_sonido

app = Flask(__name__,template_folder ="views")


app.register_blueprint(controller_sonido)




if __name__ == '__main__':
    app.run(debug=True)