import os
import sys

import pandas as pd

sys.path.append(os.getcwd())
from sklearn.model_selection import train_test_split

from mltraining.config import logger
from mltraining.utils.data_util import process_data
from mltraining.utils.model_util import compute_model_metrics, train_model

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

label = "salary"


def main():
    logger.info("START: training script")

    logger.info("Import csv data from data folder")
    data = pd.read_csv("data/cleaned_full_census.csv")

    logger.info("Train test split")
    train, test = train_test_split(data, test_size=0.20)

    logger.info("Process training data")
    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label=label, training=True
    )

    # Proces the test data with the process_data function.
    logger.info("Process testing data")
    X_test, y_test, encoder, lb = process_data(
        test,
        categorical_features=cat_features,
        label=label,
        training=False,
        encoder=encoder,
        lb=lb,
    )
    # Train the model.
    logger.info("Training the model")
    model, best_params, _ = train_model(X_train, y_train)

    # Evaluate on test set
    precision, recall, fbeta = compute_model_metrics(y_test, model.predict(X_test))
    logger.info("Export result to model_info.txt")
    with open(f"model/model_info.txt", "w") as f:
        f.write(
            f"""Model: {model}
        precision: {precision}; recall: {recall}; fbeta: {fbeta}
        Params: {best_params}"""
        )

    # export the artifacts
    logger.info("Export artifacts to model folder")
    for obj, name in zip([model, encoder, lb], ["model", "encoder", "label_binarizer"]):
        pd.to_pickle(obj, f"model/{name}.pkl")


if __name__ == "__main__":
    main()
