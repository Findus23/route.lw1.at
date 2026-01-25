all: extract update compile run


extract:
	pybabel extract -F mapping.ini -o translations/messages.pot templates/*

update:
	pybabel update -i translations/messages.pot -d translations

compile:
	pybabel compile  -d translations --statistics

run:
	python main.py
