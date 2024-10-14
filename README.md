# Animal API

Este proyecto es una API RESTful en Python utilizando Flask y SQLite. La API permite realizar operaciones CRUD sobre animales, con acciones adicionales como rugir, cazar y dormir.

## Requisitos

- Python 3.8 o superior
- Flask
- SQLAlchemy

## Instalación

1. Clonar el repositorio
    ```bash
    git clone <repo-url>
    cd APIRestTigre
    ```

2. Instalar dependencias
    ```bash
    pip install -r requirements.txt
    ```

3. Ejecutar la aplicación
    ```bash
    make run
    ```

4. Ejecutar pruebas
    ```bash
    make test
    ```

## Endpoints

- `GET /animals` - Obtiene todos los animales.
- `POST /animals` - Crea un nuevo animal.
- `GET /animals/<id>` - Obtiene un animal por ID.
- `PUT /animals/<id>` - Actualiza un animal.
- `DELETE /animals/<id>` - Elimina un animal.
- `POST /animals/<id>/rugir` - El animal ruge.
- `POST /animals/<id>/cazar` - El animal caza.
- `POST /animals/<id>/dormir` - El animal duerme.

