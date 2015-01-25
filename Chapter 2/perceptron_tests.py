import perceptron

def no_training_data_supplied_test():
  the_perceptron = perceptron.Perceptron()
  result = the_perceptron.predict()
  assert result is None, 'Should have no result with no training data.'

def simplest_training_set_and_prediction_test():
  the_perceptron = perceptron.Perceptron()
  the_perceptron.train([([0], 0)])
  result = the_perceptron.predict([0])
  assert result is 0, 'Should return the only result it learned.'

def predict_what_weve_seen_in_the_past_test():
  the_perceptron = perceptron.Perceptron()
  the_perceptron.train([([0], 0),([1], 1)])
  result = the_perceptron.predict([0])
  assert result == 0

  result = the_perceptron.predict([1])
  assert result == 1

def seperate_one_dimensional_data_that_generalizes_to_unseen_data_test():
  the_perceptron = perceptron.Perceptron()
  the_perceptron.train([([0], 0),([-1], 0),([1], 1),([2], 1)])
  print the_perceptron._weights
  result = the_perceptron.predict([-2])
  assert result == 0

  result = the_perceptron.predict([3])
  assert result == 1