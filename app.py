from flask import Flask
from api.route.tipo_route import tipo_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(tipo_api, url_prefix='/api')
    
    app.config['JSON_SORT_KEYS'] = False
    
    return app
    
if __name__ == '__main__': 
    app = create_app()
    app.run()