import numpy as np


class Mediator:

    def __init__(self, public_vector, k):
        self.public_vector = public_vector
        self.intermediate_results = np.empty(len(self.public_vector))
        self.k = k
        self.known_coefficients = np.empty([len(self.public_vector), k])
        self.update_known_coefficients()

    def update_known_coefficients(self):
        for i in range(len(self.known_coefficients[:,0])):
            for j in range(len(self.known_coefficients[0,:])-1):
                self.known_coefficients[i,j] = self.public_vector[i]**(j+1)
            self.known_coefficients[i,-1] = 1



    def update_intermediate_results(self, intermediate_result, party_index):
        self.intermediate_results[party_index] = intermediate_result

    def solve(self):
        print(">>>", self.known_coefficients, self.intermediate_results)
        result = np.linalg.solve(self.known_coefficients[:self.k,:], self.intermediate_results[:self.k])
        aggregation_result = result[-1]
        return aggregation_result
