# POS

A simple parts-of-speech API using [spacy](https://spacy.io). Based on [Microsoft's FastAPI spacy template](https://github.com/microsoft/cookiecutter-spacy-fastapi).

---
## Run locally
To run this project locally, it is first necessary to install the dependencies. It is recommended to use virtualenv to do this.

```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements/base.txt
python3 main.py
```

Visit [localhost:8080](http://localhost:8080) to verify that it is running.

## Run with Docker
This project can also be run in a docker container. Run the following to build the container.
```
docker build -t <container_name> .
```

Run the project locally through docker with:
```
docker run -dp 8080:8080 pos-test  
```

Visit [localhost:8080](http://localhost:8080) to verify that it is running.