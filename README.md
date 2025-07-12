# Explainable AI with LIME Assignment

## Problem Description

In this assignment, you will use the LIME (Local Interpretable Model-agnostic Explanations) library to explain a prediction from a simple machine learning model trained on the Iris dataset.

## Instructions

1.  Open the `assignment.py` file.
2.  You will find a function definition: `explain_iris_prediction()`.
3.  Your tasks are to:
    *   Load the Iris dataset from `sklearn.datasets`.
    *   Train a `RandomForestClassifier` on the entire dataset.
    *   Create a `LimeTabularExplainer`.
    *   Generate and return a LIME explanation for the first instance in the dataset (`X[0]`).

## Hints

*   The Iris dataset is a classic. `load_iris()` returns an object with `data`, `target`, `feature_names`, and `class_names`.
*   When creating the `LimeTabularExplainer`, you need to pass the training data (`X`), `feature_names`, and `class_names`.
*   The `explainer.explain_instance()` method needs the instance to explain (`X[0]`), the model's prediction function (`model.predict_proba`), and the number of features to show in the explanation.

## Further Exploration (Optional)

*   The explanation object has a method called `as_pyplot_figure()`. Try calling it to visualize the explanation.
*   Look into the SHAP (SHapley Additive exPlanations) library. It's another popular library for model explainability. How does it compare to LIME?
*   How would you use LIME to explain a regression model (a model that predicts a continuous number instead of a class)?
