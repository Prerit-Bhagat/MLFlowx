import pandas as pd
import os
import json
import time

from pycaret.classification import (
    setup as cls_setup,
    compare_models as cls_compare,
    tune_model as cls_tune,
    finalize_model as cls_finalize,
    save_model as cls_save,
    pull as cls_pull
)

from pycaret.regression import (
    setup as reg_setup,
    compare_models as reg_compare,
    tune_model as reg_tune,
    finalize_model as reg_finalize,
    save_model as reg_save,
    pull as reg_pull
)


def detect_problem_type(df, target_column):
    if df[target_column].dtype == "object":
        return "classification"
    return "regression"


def train_model(dataset_path, target_column):

    start_time = time.time()

    df = pd.read_csv(dataset_path)

    problem_type = detect_problem_type(df, target_column)

    model_name = "best_model"

    if problem_type == "classification":

        cls_setup(
            data=df,
            target=target_column,
            session_id=42,
            verbose=False
        )

        best_model = cls_compare()

        tuned_model = cls_tune(best_model)

        final_model = cls_finalize(tuned_model)

        accuracy_table = cls_pull()

        accuracy = float(accuracy_table.iloc[0]['Accuracy'])

        model_path = os.path.join("models", model_name)

        cls_save(final_model, model_path)

    else:

        reg_setup(
            data=df,
            target=target_column,
            session_id=42,
            verbose=False
        )

        best_model = reg_compare()

        tuned_model = reg_tune(best_model)

        final_model = reg_finalize(tuned_model)

        result_table = reg_pull()

        accuracy = float(result_table.iloc[0]['R2'])

        model_path = os.path.join("models", model_name)

        reg_save(final_model, model_path)

    training_time = round(time.time() - start_time, 2)

    metrics = {
        "problem_type": problem_type,
        "accuracy": accuracy,
        "training_time_seconds": training_time,
        "model_path": f"{model_path}.pkl"
    }

    with open("metrics/metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    return metrics