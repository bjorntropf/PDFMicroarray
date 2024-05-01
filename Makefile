.PHONY: clean build install lint publish test update upgrade

clean:
	@rm -rf dist/
	@rm -rf .pytest_cache/
	@rm -rf pdf_microarray/__pycache__/
	@rm -rf tests/__pycache__/

build:
	@rm -rf dist
	@poetry build
	@pipx uninstall pdf-microarray
	@pipx install dist/pdf_microarray-*-py3-none-any.whl

install:
	@poetry install

lint:
	@poetry run flake8 pdf_microarray/
	@poetry run black --check pdf_microarray/

publish:
	@poetry build
	@poetry publish

test:
	@poetry run pytest

update:
	@poetry update

upgrade:
	@poetry show --outdated | grep -o "^[a-z\-]*" | xargs -I {} poetry add {}@latest

