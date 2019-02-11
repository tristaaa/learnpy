#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 
from MITPersonTrial import MITPerson

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)


# Professor usage example

faculty = Professor('Doctor Arrogant', 'six')

print()
print('---Professor usage example---')
print(faculty.speak('hi there')) # shows Arrogant says: In course six we say hi there
print(faculty.lecture('hi there')) # shows Arrogant says: In course six we say it is obvious that hi there