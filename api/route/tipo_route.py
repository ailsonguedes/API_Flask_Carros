from flask import Blueprint, make_response, jsonify, request
import sys
sys.path.append("..")
from db import Carros

tipo_api = Blueprint('api', __name__)

# get -- retorna todos os carros da lista
@tipo_api.route('/carros', methods=['GET'])
def get_carros():
    # perguntar o porque quando eu uso o Blueprint o make_response e o jsonify não parecem ser necessários para chamar o endpoint com a estrutura correta.
    return make_response( 
        jsonify(
            message='Lista de carros.',
            data=Carros      
                )
    )

@tipo_api.route('/carros', methods=['POST'])    
def create_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            message='Carro cadastrado com sucesso!',
            data=carro
            )                        
    ) 

@tipo_api.route('carros/<int:carro_id>', methods=['DELETE'])  
def delete_carro(carro_id):
    carro = next((carro for carro in Carros if carro['id'] == carro_id), None)
    
    if carro is None:
        return make_response(
            jsonify(
                {"status": "Esse carro não existe"}
            ), 400
        )
    else:
        Carros.remove(carro)
        return make_response(
            jsonify(
                {"status": f"Carro {carro_id} deletado com sucesso"},
                {"Data": f"Carro: {carro['marca']} {carro['modelo']}, Ano: {carro['ano']}"}
            ), 200                      
        ) 