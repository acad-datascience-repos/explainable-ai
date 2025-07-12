import lime
import lime.lime_tabular
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

def explain_iris_prediction():
  """
  Trains a model on the Iris dataset and explains a prediction with LIME.

  Returns:
    A LIME explanation object.
  """
  # Task 1: Load the Iris dataset and train a RandomForestClassifier
  # Hint: Use load_iris() and then model.fit(X, y)
  iris = None
  X, y = (None, None)
  model = None
  # Your code here


  # Task 2: Create a LimeTabularExplainer
  # Hint: You need to pass the training data (X), feature_names, and class_names from the iris object.
  explainer = None
  # Your code here


  # Task 3: Explain a prediction
  # Hint: Use explainer.explain_instance() on the first instance (X[0]).
  explanation = None
  # Your code here


  return explanation