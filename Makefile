run:
	python app.py

test:
	python -m unittest discover -s tests

lint:
	flake8 .

coverage:
	coverage run -m unittest discover -s tests
	coverage report -m

trivy:
	trivy fs .

encrypt-secrets:
	sops --encrypt --pgp 3D16CEE4A27381B4 secrets.yaml > secrets.enc.yaml

decrypt-secrets:
	sops --decrypt secrets.enc.yaml > secrets.yaml
