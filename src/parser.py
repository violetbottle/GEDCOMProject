from datetime import datetime
from .classModels import gedcomTagLine, individualPerson, familyClass

# Function to Parse the GEDCOM file
def GEDCOMParser(filename):
    individual = []
    family = []
    gedlist = []

    lines = [line.rstrip('\n') for line in open(filename)]

    for line in lines:

        current_gedcom = gedcomTagLine(line)
        gedlist.append(current_gedcom)


    for index, gedcomline in enumerate(gedlist):

        if gedcomline.tag == 'INDI':

            date_type = None
            indiObject = individualPerson(gedcomline.ref)

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

                if gedline.tag == 'DATE':
                    if date_type == 'BIRT':
                        indiObject.birthday = datetime(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        date_type = None
                    elif date_type == 'DEAT':
                        indiObject.deathDate = datetime(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        date_type = None
            individual.append(indiObject)

        if gedcomline.tag == 'FAM':

            date_type = None
            familyObject = familyClass(gedcomline.ref)

            for gedline in gedlist[index + 1:]:
                if gedline.level == 0:
                    break
                if gedline.tag == "MARR":
                    date_type = "MARR"
                if gedline.tag == "DIV":
                    date_type = "DIV"
                if gedline.tag == "HUSB":
                    familyObject.husband = gedline.arg[0]
                if gedline.tag == "WIFE":
                    familyObject.wife = gedline.arg[0]
                if gedline.tag == "CHIL":
                    familyObject.children.append(gedline.arg[0])


                if gedline.tag == "DATE":
                    if date_type == "MARR":

                        familyObject.marriage = datetime(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        date_type = None

                    elif date_type == "DIV":

                        familyObject.divorce = datetime(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        date_type = None
            family.append(familyObject)

    return individual, family