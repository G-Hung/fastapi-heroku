import numpy as np
import pandas as pd
import pytest
from sklearn.dummy import DummyClassifier

from mltraining.train_model import cat_features
from mltraining.utils.data_util import process_data
from mltraining.utils.model_util import compute_model_metrics, inference


@pytest.fixture(scope="module")
def data():
    df = pd.read_csv("data/cleaned_full_census.csv")
    X, y, _, _ = process_data(
        df, categorical_features=cat_features, label="salary", training=True
    )
    return X, y


@pytest.fixture(scope="module")
def model(data):
    X, y = data
    dummy = DummyClassifier(strategy="uniform")
    dummy.fit(X, y)
    return dummy


def test_inference_shape(data, model):
    X, _ = data
    preds = inference(model, X)
    assert len(preds) == len(X)
    assert isinstance(preds, np.ndarray)


def test_inference_vals(data, model):
    X, _ = data
    preds = inference(model, X)
    assert set(preds) and set([0, 1]) == set([0, 1])


def test_compute_model_metrics_shape(data, model):
    X, y = data
    preds = inference(model, X)
    output = compute_model_metrics(y, preds)
    assert len(output) == 3


def test_compute_model_metrics_vals(data, model):
    X, y = data
    preds = inference(model, X)
    output = compute_model_metrics(y, preds)
    assert all(0 <= metric <= 1 for metric in output)
