"""
This file provides classes for parsing the GEDCOM file
"""
validTags = ['NAME', 'SEX', 'FAMS', ' FAMC', 'MARR', 'BIRT', 'WIFE', 'HUSB', 'CHIL', 'DEAT', 'DIV', 'DATE', 'HEAD','TRLR', 'NOTE',
             'INDI', 'FAM']

# class for every gedcom tag line
class gedcomTagLine(object):

    def __init__(self, line):
        self.level = None
        self.tag = None
        self.arg = None
        self.ref = None

        listLine = line.split(' ',)
        # set level of the object
        self.level = int(listLine[0])

        # for setting tag and argument
        if self.level > 0:
            self.tag = listLine[1]
            self.arg = listLine[2:]

        if self.level == 0:
            if listLine[1] in validTags:
                self.tag = listLine[1]
                self.arg = None
            else:
                self.tag = listLine[2]
                self.ref = listLine[1]


# class for individual persons
class individualPerson(object):

    def __init__(self, uid):
        self.uid = uid  #umoque id of individual person
        self.name = None # name of individual person
        self.birthday = None # Date of birthday of individual person
        self.sex = None # sex of individual person
        self.deathDate = None # Date of death of individual person
        self.alive = True # person alive or dead
        self.famc = [] # family id where individual is a child
        self.fams = [] # family id where individual is parent

# class for families
class familyClass(object):

    def __init__(self, uid):
        self.uid = uid
        self.marriage = None  # marriage event for family
        self.husband = None  # for husband in family
        self.husbandName = None # name of husband
        self.wife = None  # for wife in family
        self.wifeName = None # for name of the wife
        self.children = []  # for child in family
        self.divorce = None  # divorce event in family