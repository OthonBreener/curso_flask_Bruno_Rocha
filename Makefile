# arquivo para instalar vários pacotes de uma vez

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .['dev'] --upgrade --no-cache

install:
	pip install -e .['dev']

test:
	FLASK_ENV= test pytest tests/ -v --cov=apilanches

run:
	FLASK_APP=apilanches/app.py FLASK_ENV=development flask run

format:
	isort **/*.py
	black -l 79 **/*.py

