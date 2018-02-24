from simulator import Simulator, PeopleTypes
import numpy as np 

data_simulator = Simulator(10,1000,10,"single",0)

types_of_people = [PeopleTypes(50, 0.1, 0.3), PeopleTypes(40, 0.4, 0.6), PeopleTypes(10, 0.6, 0.85)]

data, ground_truths = data_simulator.generate_data(types_of_people)

data_simulator.write_to_csv('crowd.csv', data, mode="value", order_by="question")
data_simulator.write_to_csv('gt.csv', ground_truths, mode="value")
