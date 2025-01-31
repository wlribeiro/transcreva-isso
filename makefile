dev:
	uvicorn transcript.main:app --reload
install:
	pip install -r requirements.txt