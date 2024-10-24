# Ejecutar la aplicación
run:
	poetry run python app.py

# Ejecutar pruebas
test:
	poetry run pytest

# Linter con flake8
lint:
	poetry run flake8 .

# Medir la cobertura
coverage:
	poetry run coverage run -m pytest
	poetry run coverage report -m

# Cifrar secretos
encrypt-secrets:
	poetry run sops --encrypt --pgp 3D16CEE4A27381B4 secrets.yaml > secrets.enc.yaml

# Descifrar secretos
decrypt-secrets:
	poetry run sops --decrypt secrets.enc.yaml > secrets.yaml
