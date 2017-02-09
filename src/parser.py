import sys

def GEDCOMParser():
    with open('gedcom_files/Family.ged') as i:
        for line in i:
            print(line.rstrip())
            list = line.split()
            try:
                if list[0] == 'NOTE':
                    continue
                else: print("Level: ",list[0])
                if list[1] in ('NAME', 'SEX', 'FAMS', ' FAMC', 'MARR', 'BIRT', 'WIFE', 'HUSB', 'CHIL', 'DEAT', 'DIV', 'DATE', 'HEAD','TRLR', 'NOTE'):
                    print("Tag: ",list[1])
                elif list[2] in ('INDI', 'FAM'):
                    print("Tag: ",list[2])
                else: print('Tag: Invalid Tag')
            except IndexError:
                print('Tag: Invalid Tag')


if __name__=='__main__':
    sys.stdout = open("OutputFile.txt","w")
    GEDCOMParser()
    sys.__stdout__.close()