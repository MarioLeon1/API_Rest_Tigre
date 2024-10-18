# Animal API

Este proyecto es una API RESTful en Python utilizando Flask y SQLite. La API permite realizar operaciones CRUD sobre animales, con acciones adicionales como rugir, cazar y dormir.

## Requisitos

- Python 3.8 o superior
- Flask
- SQLAlchemy
- GnuPG (para el manejo de claves PGP)
- **SOPS** (para cifrado y descifrado de secretos)

## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone <repo-url>
    cd APIRestTigre
    ```

2. **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Importar la clave PGP para cifrado de secretos:**

    Si has recibido una clave PGP (por ejemplo, `sops_functional_tests_key.asc`), impórtala con el siguiente comando:

    ```bash
    gpg --import sops_functional_tests_key.asc
    ```

    Asegúrate de utilizar el ID correcto de la clave en el siguiente paso (en este caso, `3D16CEE4A27381B4`).

4. **Cifrar o descifrar los secretos (opcional):**

    Si trabajas con datos sensibles, puedes usar **SOPS** para cifrar y descifrar el archivo `secrets.yaml`.

    - **Cifrar el archivo `secrets.yaml`:**
      
      ```bash
      make encrypt-secrets
      ```

    - **Descifrar el archivo `secrets.enc.yaml`:**
      
      ```bash
      make decrypt-secrets
      ```

5. **Ejecutar la aplicación:**

    ```bash
    make run
    ```

6. **Ejecutar las pruebas:**

    ```bash
    make test
    ```

## Cifrado de Secretos con SOPS

El proyecto utiliza **SOPS** para gestionar los secretos de forma segura mediante cifrado PGP. Aquí te dejamos un ejemplo de cómo gestionar el archivo `secrets.yaml`:

1. **Archivo `secrets.yaml` de ejemplo:**

    ```yaml
    user: fake_user
    pass: fake_password
    ```

2. **Cifrar el archivo `secrets.yaml` con SOPS:**

    Este comando cifra el archivo usando la clave PGP importada (ID `3D16CEE4A27381B4`):

    ```bash
    make encrypt-secrets
    ```

3. **Descifrar el archivo `secrets.enc.yaml`:**

    Para obtener el archivo original `secrets.yaml`:

    ```bash
    make decrypt-secrets
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

## Consideraciones de seguridad

- **PGP**: Se utiliza **GPG** para gestionar las claves PGP y cifrar/desencifrar secretos.
- **SOPS**: Automatiza el cifrado de los archivos sensibles usando PGP.
- Asegúrate de que el archivo **`secrets.yaml`** no se suba a GitHub, añadiéndolo a `.gitignore`:

    ```bash
    secrets.yaml
    sops_functional_tests_key.asc
    ```
