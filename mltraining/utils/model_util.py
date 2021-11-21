from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import fbeta_score, precision_score, recall_score
from sklearn.model_selection import RandomizedSearchCV

from mltraining.config import logger


# Optional: implement hyperparameter tuning.
def train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """
    rf = RandomForestClassifier()
    rf_params = {
        "n_estimators": [50, 100, 150, 200],
        "max_features": ["auto", "sqrt", "log2", None],
        "criterion" : ["gini", "entropy"]
    }
    logger.info("Start randomized search")
    clf = RandomizedSearchCV(rf, rf_params)
    clf.fit(X_train, y_train)
    model_score, best_params, best_score = (
        clf.best_estimator_,
        clf.best_params_,
        clf.best_score_,
    )
    logger.info("Export result to model_info.txt")
    with open(f"model/model_info.txt", "w") as f:
        f.write(f"Model: {model_score}\nScore: {best_score}\nParams: {best_params}")

    return clf.best_estimator_


def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def inference(model, X):
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : ???
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    return model.predict(X)
