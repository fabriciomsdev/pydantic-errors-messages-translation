setup-environment:
	python3 -m venv venv
	. ./venv/bin/activate
	PIP_CONFIG_FILE=./pip.conf pip install -r requirements.txt
	PIP_CONFIG_FILE=./pip.conf pip install -r requirements-dev.txt

up-version:
	. ./venv/bin/activate && bumpversion minor --new-version $1 setup.py ./pydantic_errors_messages_translations/__init__.py

release:
	make up-version
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*