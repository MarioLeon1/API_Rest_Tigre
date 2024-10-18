import os
from flask import Flask, jsonify, request, redirect, url_for, render_template_string
from dotenv import load_dotenv
from models import Animal
from database import init_db, db_session

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configuraciones de la aplicación usando variables de entorno
app.config['ENV'] = os.getenv('FLASK_ENV', 'development')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'mysecretkey')

# Inicializar la base de datos y crear un tigre si no existe
def initialize_default_data():
    # Verificar si el tigre ya existe
    tiger = Animal.query.get(1)
    if not tiger:
        # Crear el tigre por defecto con ID 1
        new_tiger = Animal(id=1, name='Tigre', action='rugir')
        db_session.add(new_tiger)
        db_session.commit()
        print('Tigre inicializado en la base de datos.')

# Inicializar la base de datos
init_db()
initialize_default_data()

# Página principal con botones para las acciones del tigre
@app.route('/')
def index():
    html_content = '''
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 18px;
                color: #666;
            }
            button {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 10px;
                cursor: pointer;
                border-radius: 8px;
                transition-duration: 0.4s;
            }
            button:hover {
                background-color: #45a049;
            }
            a {
                text-decoration: none;
                color: #4CAF50;
                font-size: 16px;
            }
            a:hover {
                color: #333;
            }
            .container {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bienvenido a la API de Animales</h1>
            <p>Elige una acción para el tigre:</p>
            <form action="/animals/1/rugir" method="POST">
                <button type="submit">Rugir</button>
            </form>
            <form action="/animals/1/cazar" method="POST">
                <button type="submit">Cazar</button>
            </form>
            <form action="/animals/1/dormir" method="POST">
                <button type="submit">Dormir</button>
            </form>
            <p><a href="/animals">Ver todos los animales</a></p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

@app.route('/animals', methods=['GET'])
def get_animals():
    animals = Animal.query.all()
    return jsonify([animal.to_dict() for animal in animals])

@app.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    animal = Animal.query.get(id)
    if not animal:
        return jsonify({'error': 'Animal not found'}), 404
    return jsonify(animal.to_dict())

@app.route('/animals', methods=['POST'])
def create_animal():
    data = request.get_json()
    new_animal = Animal(name=data['name'], action=data['action'])
    db_session.add(new_animal)
    db_session.commit()
    return jsonify(new_animal.to_dict()), 201

@app.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    animal = Animal.query.get(id)
    if not animal:
        return jsonify({'error': 'Animal not found'}), 404
    data = request.get_json()
    animal.name = data.get('name', animal.name)
    animal.action = data.get('action', animal.action)
    db_session.commit()
    return jsonify(animal.to_dict())

@app.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    animal = Animal.query.get(id)
    if not animal:
        return jsonify({'error': 'Animal not found'}), 404
    db_session.delete(animal)
    db_session.commit()
    return jsonify({'message': 'Animal deleted'}), 200

@app.route('/animals/<int:id>/rugir', methods=['POST'])
def animal_rugir(id):
    animal = Animal.query.get(id)
    if not animal:
        return jsonify({'error': 'Animal not found'}), 404
    return render_template_string('<h2>{} está rugiendo!</h2><a href="/">Volver</a>'.format(animal.name))

@app.route('/animals/<int:id>/cazar', methods=['POST'])
def animal_cazar(id):
    animal = Animal.query.get(id)
    if not animal:
        return jsonify({'error': 'Animal not found'}), 404
    return render_template_string('<h2>{} está cazando!</h2><a href="/">Volver</a>'.format(animal.name))

@app.route('/animals/<int:id>/dormir', methods=['POST'])
def animal_dormir(id):
    animal = Animal.query.get(id)
    if not animal:
        return jsonify({'error': 'Animal not found'}), 404
    return render_template_string('<h2>{} está durmiendo!</h2><a href="/">Volver</a>'.format(animal.name))

if __name__ == '__main__':
    app.run(debug=True)
