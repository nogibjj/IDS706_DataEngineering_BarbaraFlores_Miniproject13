install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=app --cov= test_*.py

format:	
	black app/*.py run.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py app/*.py run.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy
