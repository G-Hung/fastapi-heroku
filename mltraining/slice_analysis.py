import pandas as pd
from config import logger
from train_model import cat_features, label
from utils.data_util import process_data
from utils.model_util import compute_model_metrics, inference


def performance_by_feature_slice(df, slice_feature, model, encoder, lb):
    logger.info(f"Start slice performance analysis on {slice_feature} feature")
    with open(f"model/{slice_feature}_perf_output.txt", "w") as f:
        f.write(f"Performance for {slice_feature} feature\n")
        f.write(f"---------------------------------------\n")
        for slice in df[slice_feature].unique():
            logger.info(f"{slice} in {slice_feature} feature")
            slice_df = df.loc[df[slice_feature] == slice]
            X, y, _, _ = process_data(
                X=slice_df,
                categorical_features=cat_features,
                label=label,
                training=False,
                encoder=encoder,
                lb=lb,
            )
            y_pred = inference(model, X)
            precision, recall, fbeta = compute_model_metrics(y, y_pred)
            f.write(f"---------------------------------------\n")
            f.write(f"{slice}:")
            f.write("\n")
            f.write(f"precision:  {precision}")
            f.write("\n")
            f.write(f"recall:     {recall}")
            f.write("\n")
            f.write(f"fbeta:      {fbeta}")
            f.write("\n")


if __name__ == "__main__":
    DATA = pd.read_csv("data/cleaned_full_census.csv")
    MODEL = pd.read_pickle("model/model.pkl")
    ENCODER = pd.read_pickle("model/encoder.pkl")
    LABEL_BINARIZER = pd.read_pickle("model/label_binarizer.pkl")
    LABEL = label

    FEATURES = ["race"]
    for feature in FEATURES:
        performance_by_feature_slice(DATA, feature, MODEL, ENCODER, LABEL_BINARIZER)
