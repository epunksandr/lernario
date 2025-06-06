make run:
	python app.py

make install:
	pip install -r requirements.txt

make unit-test:
	pytest tests/unit -v

make integration-test:
	pytest tests/integration -v

make test:
	pytest tests/unit -v
	pytest tests/integration -v