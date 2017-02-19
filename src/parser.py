from datetime import date
from datetime import datetime
from .classModels import gedcomTagLine, individualPerson, familyClass

# Function to Parse the GEDCOM file
def GEDCOMParser(filename):
    individual = []
    family = []
    gedlist = []

    # read each line from file and strip \n from the last
    lines = [line.rstrip('\n\r') for line in open(filename)]

    # Create objects and add it to the list
    for line in lines:
        current_gedcom = gedcomTagLine(line)
        gedlist.append(current_gedcom)

    # Iterate every tag
    for index, gedcomline in enumerate(gedlist):
        #for saving Individual person
        if gedcomline.tag == 'INDI':

            date_type = None
            # Create blank object for the person
            indiObject = individualPerson(gedcomline.ref)

            # set the values of the object UNTIL next level 0
            for gedline in gedlist[index + 1:]:
                if gedline.level == 0:
                    break
                if gedline.tag == "NAME":
                    indiObject.name = gedline.arg
                if gedline.tag == "SEX":
                    indiObject.sex = gedline.arg[0]
                if gedline.tag == "BIRT":
                    date_type = "BIRT"
                if gedline.tag == "DEAT":
                    date_type = "DEAT"
                if gedline.tag == "FAMC":
                    indiObject.famc.append(gedline.arg[0])
                if gedline.tag == "FAMS":
                    indiObject.fams.append(gedline.arg[0])

                # check if date is birth or date
                if gedline.tag == 'DATE':
                    if date_type == 'BIRT':
                        indiObject.birthday = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        date_type = None
                    elif date_type == 'DEAT':
                        indiObject.deathDate = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        indiObject.alive = False
                        date_type = None

            # add object into the individual list
            individual.append(indiObject)

        # For family list
        if gedcomline.tag == 'FAM':

            date_type = None

            # create blank object
            familyObject = familyClass(gedcomline.ref)

            # ste values until next level 0
            for gedline in gedlist[index + 1:]:
                if gedline.level == 0:
                    break
                if gedline.tag == "MARR":
                    date_type = "MARR"
                if gedline.tag == "DIV":
                    date_type = "DIV"
                if gedline.tag == "HUSB":
                    familyObject.husband = gedline.arg[0]
                    for persons in individual:
                        if persons.uid == gedline.arg[0]:
                            familyObject.husbandName = persons.name
                if gedline.tag == "WIFE":
                    familyObject.wife = gedline.arg[0]
                    for persons in individual:
                        if persons.uid == gedline.arg[0]:
                            familyObject.wifeName = persons.name
                if gedline.tag == "CHIL":
                    familyObject.children.append(gedline.arg[0])

                # check if marriage date or divorce date
                if gedline.tag == "DATE":
                    if date_type == "MARR":

                        familyObject.marriage = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        date_type = None

                    elif date_type == "DIV":

                        familyObject.divorce = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        date_type = None
            # append object into the family list
            family.append(familyObject)

    return individual, family