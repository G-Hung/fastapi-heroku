# Environment Set up
* Download and install conda if you don’t have it already.
```
conda create -n fastapi_heroku "python=3.8" scikit-learn dvc pandas numpy pytest jupyter jupyterlab fastapi uvicorn -c conda-forge pip

pip install -r requirements.txt
```

## Introduction

repo: https://github.com/G-Hung/fastapi-heroku

In the project, the interesting try is to use DVC and set S3 as remote location to store trained model and data. The advantage of this is we have lighter repo and we don't need to develop extra logic to download the data. `dvc pull` will follow the configurations in dvc files and pull them even the repo is deployed to another environment [and they need to have corresponding credentials for sure]

## GitHub Actions

GitHub Actions is used for the unit testing and style check in this repo, for more details, they are under `.github`

## Data & Model

Data is not the key part of this project, just the census data from UCI repo
 <a href="https://archive.ics.uci.edu/ml/datasets/census+income" target="_blank">here</a>.

Model is also not the key for this, although we can try more, the key is to have the complete workflow to deploy the api with trained model

## API Creation

We use FastAPI to deploy REST API for the project, for details, please see `api` folder

## API Deployment
The API is deployed to heroku, note that it may take some times to warmup if it is not used recently

https://udacity-fastapi-ghung.herokuapp.com/
