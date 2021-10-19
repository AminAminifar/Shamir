import numpy as np
import party
import mediator
import interface

n = 10
k = 9

#  generate secret values
secret_values = 1 - np.random.random_sample(n)
public_vector = 1 - np.random.random_sample(n)


#  generate parties
parties = []
for i in range(n):
    parties.append(party.Party(party_index=i, public_vector=public_vector, secret_value=secret_values[i], k=k))

#  generate mediator
mediator = mediator.Mediator(public_vector, k)

#  generate interface
interface = interface.Interface(parties, mediator)

#  run secure aggregation
aggregation_result = interface.perform_secure_aggregation()

print("Comparison (aggregation_result, np.sum(secret_values))", aggregation_result, np.sum(secret_values))

