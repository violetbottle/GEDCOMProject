from unittest import TestCase
import os
from .parser import GEDCOMParser
from .userStoriesValidation import birth_before_marriage

cur_path = os.path.dirname(__file__)
FAIL_DIR = "gedcom_files/fail/"
PASS_DIR = "gedcom_files/pass/"
acceptfile = "Family.ged"
fail_file = os.path.relpath("..\\" + FAIL_DIR + acceptfile, cur_path)
pass_file = os.path.relpath("..\\" + PASS_DIR + acceptfile, cur_path)

class test_birth_before_marriage(TestCase):
    def test_birth_before_marriage(self):

        if os.path.exists(fail_file) and os.path.exists(pass_file):
            individuals, families = GEDCOMParser(pass_file)
            self.assertTrue(birth_before_marriage(individuals, families))
            individuals, families = GEDCOMParser(fail_file)
            self.assertFalse(birth_before_marriage(individuals, families))
        else:
            print("!!test_marriage_before_death acceptance file not found")

    def test_birth_before_date(self):
        individuals, families = GEDCOMParser(pass_file)
        for family in families:
            if family.marriage:
                husband = None
                wife = None
                for indiv in individuals:
                    if indiv.uid == family.husband:
                        husband = indiv
                    if indiv.uid == family.wife:
                        wife = indiv
                self.assertNotEquals(husband.birthday, wife.birthday)

