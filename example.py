from simulator import Simulator, PeopleTypes
import numpy as np 

# 8 people answering 1000 questions, each with 10 options, where exactly one is correct
data_simulator = Simulator(8,1000,10,"single",0)

# 50% of people answer correctly with probability [0.1,0.3)
# 40% of people answer correctly with probability [0.4,0.6)
# 10% of people answer correctly with probability [0.6,0.85)
types_of_people = [PeopleTypes(50, 0.1, 0.3), PeopleTypes(40, 0.4, 0.6), PeopleTypes(10, 0.6, 0.85)]

# generate the data and the ground truths
data, ground_truths = data_simulator.generate_data(types_of_people)

# write generated data to CSVs
# simulated data is stored question-wise, with a comma-separated set of correct options
data_simulator.write_to_csv('crowd.csv', data, mode="value", order_by="question")
data_simulator.write_to_csv('gt.csv', ground_truths, mode="value")
