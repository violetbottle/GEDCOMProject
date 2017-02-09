"""
This file provides classes for parsing the GEDCOM file
"""

# class for individual persons
class individualPerson(object):

    def __init__(self, uid):
        self.uid = uid  #umoque id of individual person
        self.name = None # name of individual person
        self.birthday = None # Date of birthday of individual person
        self.sex = None # sex of individual person
        self.death = None # Date of death of individual person
        self.famc = [] # family id where individual is a child
        self.fams = [] # family id where individual is parent

# class for families
class family(object):

    def __instancecheck__(self, uid):
        self.uid = uid
        self.marriage = None  # marriage event for family
        self.husband = None  # for husband in family
        self.wife = None  # for wife in family
        self.children = []  # for child in family
        self.divorce = None  # divorce event in family