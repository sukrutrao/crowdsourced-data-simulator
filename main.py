from simulator import Simulator, PeopleTypes
import numpy as np 

data_simulator = Simulator(10,6,4,"multiple",0)

types_of_people = [PeopleTypes(20, 0.4, 0.6), PeopleTypes(60, 0.66, 0.75), PeopleTypes(20, 0.8, 0.95)]

data, ground_truths = data_simulator.generate_data(types_of_people)

data_simulator.write_to_csv('data.csv', data, mode="vector", order_by="person")
data_simulator.write_to_csv('gt.csv', ground_truths, mode="vector")