{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   │   ├── testing
    │   │   └── training
    │   └── raw            <- The original, immutable data dump.
    │
    ├── devops             <- Scripts for devOps
    │   ├── infra          <- Scripts for creating infrastructure
    │   │   ├── aws
    │   │   ├── gcp
    │   │   └── README.md
    │   └── Jenkinsfile    <- Jenkins file
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── mlops              <- Scripts for MLOps
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── config         <- Scripts for project configurations
    │   │   └── config.yaml
    │   │
    │   ├── dags           <- Scripts for Airflow dags
    │   │
    │   └── docker         <- Docker files
    │       ├── docker-compose.yml
    │       └── Dockerfile
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   ├── main.py        <- Main file to run the project (includes flow, etc.)
    │   ├── README.md
    │   ├── VERSION
    │   │
    │   ├── api            <- Scripts for API (realtime models)
    │   │   └── __init__.py
    │   │
    │   ├── config         <- Scripts for configurations
    │   │   ├── __init__.py
    │   │   ├── config.py
    │   │   └── config.yaml
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   ├── __init__.py
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   ├── __init__.py
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make predictions
    │   │   ├── __init__.py
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── tests          <- Scripts for tests
    │   │   ├── __init__.py
    │   │   ├── conftest.py
    │   │   └── README.md
    │   │
    │   ├── utils          <- Scripts for utility fucntions
    │   │   ├── __init__.py
    │   │   └── utils.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       ├── __init__.py
    │       └── visualize.py
    │
    ├── .env
    ├── .gitignore
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── pylintrc
    ├── pyptoject.toml
    ├── pytest.ini
    ├── README.md
    ├── requirements.txt
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── test_environments.py
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

