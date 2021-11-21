import pandas as pd
from sklearn.model_selection import train_test_split

from mltraining.config import logger
from mltraining.utils.data_util import process_data
from mltraining.utils.model_util import train_model

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
    _, _, encoder, lb = process_data(
        test,
        categorical_features=cat_features,
        label=label,
        training=False,
        encoder=encoder,
        lb=lb,
    )
    # Train and save a model.
    logger.info("Training the model")
    model = train_model(X_train, y_train)

    logger.info("Export artifacts to model folder")
    for obj, name in zip([model, encoder, lb], ["model", "encoder", "label_binarizer"]):
        pd.to_pickle(obj, f"model/{name}.pkl")


if __name__ == "__main__":
    main()
