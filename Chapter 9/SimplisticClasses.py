class DumbClassifier():
    def __init__(self, state):
        self.state = state
    def probability(self, input):
        data = self.state
        if input in data:
            return data[input]
        else:
            return None
    def predict(self, input):
        return self.probability(input)

class VariantImprovesAndFemaleMoreSoClassifier():
    def probability(self, input):
        data = {
            ('control', '60626', 'female'): 0.60,
            ('variant', '60626', 'female'): 0.65,
            ('control', '60626', 'male'): 0.45,
            ('variant', '60626', 'male'): 0.45,
            ('control', '60602', 'female'): 0.70,
            ('variant', '60602', 'female'): 0.70,
            ('control', '60602', 'male'): 0.50,
            ('variant', '60602', 'male'): 0.45,
        }
        classifier = DumbClassifier(data)
        return classifier.probability(input)

class AllCasesHaveSameProfitRegressionModel():
    def predict(self, input):
        return 12.25

def assign_ad_for(customer, classifier, regression_model, ad_cost=0):
    control_input = ('control',) + customer
    variant_input = ('variant',) + customer
    control_probability_of_order = classifier.probability(control_input)
    variant_probability_of_order = classifier.probability(variant_input)
    control_profit = regression_model.predict(control_input)
    variant_profit = regression_model.predict(variant_input)
    variant_expected_value = variant_probability_of_order * variant_profit - ad_cost
    control_expected_value = control_probability_of_order * control_profit
    if control_expected_value >= variant_expected_value:
        return 'control'
    else:
        return 'variant'
