from flask import Flask,Blueprint,jsonify,render_template
from models.huron import Huron
from models.boa_constrictor import BoaConstrictor
from models.gato import Gato
from models.perro import Perro
from models.animal import Animal

controller_sonido = Blueprint('hacer_sonido',__name__)


dict_animales = {
    "gato" : Gato (nombre="negus",raza="Criollo",edad=8,peso=5.5) ,
    "perro" : Perro(nombre="wollfie",raza="salchica",edad=1,peso=4.8),
    "huron" : Huron(nombre="kiplin",edad= 4, peso= 3.2, pais_origen= "usa", impuestos= 1500.63),
    "boa" : BoaConstrictor(nombre="la serpiente",edad=4,peso=10.0,pais_origen="rusia", impuestos=15.0,contar_ratones=0)
    }


@controller_sonido.route('/api/hacer_sonido/<nombre>', methods =['GET'])
def sonido(nombre):
    name = nombre.lower()
    if name in dict_animales:
        instancia = dict_animales[name]
        sonido = instancia.hacer_sonido()
        return jsonify({"animal":name, "sonido":sonido})
    else:
        return jsonify({"error:No se encotro animal"})

@controller_sonido.route('/hacer_sonido', methods=['GET'])
def vista():
    return render_template('vista_web_sonidos.html',animales = dict_animales)
