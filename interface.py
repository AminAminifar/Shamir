import numpy as np


class Interface:

    def __init__(self, parties, mediator):
        self.parties = parties
        self.mediator = mediator
        self.intermediate_result = np.empty(len(self.parties))

    def perform_secure_aggregation(self):
        #  all parties share local results
        for i in range(len(self.parties)):
            for j in range(len(self.parties)):
                if i != j:
                    # local result Party_i for received result of Party_j
                    # self.parties[j].received_results[i] = self.parties[i].local_results[j]
                    self.parties[j].update_received_results(received_result=self.parties[i].send_local_result(j),
                                                            party_index=i)

        #  all parties calculate and return intermediate result
        for i in range(len(self.parties)):
            self.intermediate_result[i] = self.parties[i].calculate_intermediate_result()

        #  update intermediate results on the mediator and solve the system of equations
        for i in range(len(self.parties)):
            self.mediator.update_intermediate_results(intermediate_result=self.intermediate_result[i], party_index=i)

        aggregation_result = self.mediator.solve()

        return aggregation_result
