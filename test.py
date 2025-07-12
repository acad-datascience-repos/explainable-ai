import unittest
from assignment import explain_iris_prediction
from lime.explanation import Explanation

class TestLimeExplanation(unittest.TestCase):
    def test_explain_iris_prediction(self):
        explanation = explain_iris_prediction()
        self.assertIsInstance(explanation, Explanation)
        # Check if the explanation has a list of features
        self.assertIsInstance(explanation.as_list(), list)
        self.assertGreater(len(explanation.as_list()), 0)

if __name__ == '__main__':
    unittest.main()
