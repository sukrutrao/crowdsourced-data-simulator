# Crowd-sourced Data Simulator

[![Build Status](https://travis-ci.com/GoodDeeds/crowdsourced-data-simulator.svg?branch=master)](https://travis-ci.com/GoodDeeds/crowdsourced-data-simulator)

A program that simulates crowd annotations to a set of multiple choice questions

## Description
* The program generates simulated answers to a specified number of multiple choice questions by a specified number of people of varying abilities. It also generates correct answers (randomly) to the simulated questions.
* The multiple choices questions can have either one or more correct answer, which is specified in the input.
* A simulated answerer is characterized by the ability to answer a given question correctly. Simulated answerers are grouped together using `PeopleTypes` objects.
* In a `PeopleTypes` object, the number of people out of hundred in the population belonging to that type, and the range of probabilities of getting an answer correct which characterizes people belonging to that type, are specified. A person belonging to a type has a probability of answering a question correctly as a value uniformly chosen from that type.
* When simulating, a set of `PeopleTypes` objects is specified, in a way that the entire population's ability is described.
* The simulator accepts as inputs the number of questions, the number of options per question, the number of people in the population answering the questions, and whether the questions have a single or multiple answers correct. It is assumed that every person answers every question.
* For a given question, a person answers it correctly with the probability corresponding to that person's ability.
* For multiple answer correct questions, answers are simulated by treating each option as a binary yes/no question.
* Outputs can be displayed in two formats - either as a list of selected options, or as a one-hot encoding.

## Setup 

### Prerequisites
* Python 2.7 or 3.4-3.6
* pip

### Setting up dependencies
All other dependencies can be installed using pip, as
```
$ pip install -r requirements.txt
```

## Example
Run
```
$ python example.py
```

## License
This code is provided under the [MIT License](LICENSE).

## Author
[Sukrut Rao](https://github.com/GoodDeeds/)

For any issues, queries, or suggestions, please [open an issue](https://github.com/GoodDeeds/crowdsourced-data-simulator/issues/new).
