.PHONY: install VD-games build package-install

install:
	uv sync

VD-games:
	uv run vd-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

VD-bank:
	uv run VD-bank
