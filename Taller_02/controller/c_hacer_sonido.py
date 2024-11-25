from flask import Blueprint, render_template, jsonify
from models.huron import Huron
from models.boa_constrictor import BoaConstrictor
from models.gato import Gato
from models.perro import Perro
from models.animal import Animal

controller_sonido = Blueprint('hacer_sonido',__name__)

dict_animales = {
    "gato" :Gato,
    "perro" : Perro,
    "huron" : Huron,
    "boa" : BoaConstrictor
}


@controller_sonido.route('/api/hacer_sonido/<nombre>', methods =['GET'])
def sonido(nombre):
    name = nombre.lower()
    if name in dict_animales:
        instancia = dict_animales[name]()
        sonido = instancia.hacer_sonido()
        return jsonify({"animal":name, "sonido":sonido})
    else:
        return jsonify({"error:No se encotro animal"})


