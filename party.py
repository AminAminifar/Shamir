import numpy as np


class Party:

    def __init__(self, party_index, public_vector, secret_value, k):
        self.party_index = party_index
        self.public_vector = public_vector
        self.secret_value = secret_value
        self.secret_coefficients = 1 - np.random.random_sample(k-1)
        self.received_results = np.empty(len(self.public_vector))
        self.received_results[self.party_index] = 0
        self.local_results = np.empty(len(self.public_vector))
        self.update_local_results()

    def calculate_result(self, party_index):
        public_value = self.public_vector[party_index]
        result = self.secret_value
        for i in range(len(self.secret_coefficients)):
            result += self.secret_coefficients[i] * (public_value**(i+1))
        return result

    def update_received_results(self, received_result, party_index):
        self.received_results[party_index] = received_result

    def send_local_result(self, party_index):
        return self.local_results[party_index]

    def update_local_results(self):
        for i in range(len(self.public_vector)):
            self.local_results[i] = self.calculate_result(i)

    def calculate_intermediate_result(self):
        result_self = self.local_results[self.party_index]
        intermediate_result = result_self
        intermediate_result += np.sum(self.received_results)
        return intermediate_result
