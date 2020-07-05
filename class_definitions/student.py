"""
Program name: student.py
Author: Rachel Li
Last date modified: 07/05/2020

The purpose of this program is to print student information in a string
and conduct validation with issuperset for characters
"""
class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        '''
        :param lname: this represents student last name
        :param fname:  this represents student first name
        :param major:  this represents student major
        :param gpa: this represents student gpa, takes value
        :keyError: raise ValueError if not character
        '''
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    @property
    def last_name(self):
        '''
        use reST style
        :return: last name
        '''
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        '''
        use reST style
        :return: sets the last name to a value
        :keyError: raises ValueError
        '''
        if isinstance(value, str):
            self._last_name = value
        else:
            raise ValueError

    @property
    def first_name(self):
        '''
        use reST style
        :return: returns first name
        '''
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        '''
        use reST style
        :return: returns first name in a value
        :keyError: raises ValueError if not string
        '''
        if isinstance(value, str):
            self._first_name = value
        else:
            raise ValueError

    @property
    def major(self):
        '''
        use reST style
        :return: returns major
        '''
        return self._major

    @major.setter
    def major(self, value):
        '''
        use reST style
        :return: returns major in a value
        :keyError: raises ValueError if not string
        '''
        if isinstance(value, str):
            self._major = value
        else:
            raise ValueError

    @property
    def gpa(self):
        '''
        use reST style
        :return: returns gpa
        '''
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        '''
        use reST style
        :return: returns gpa in float value
        :keyError: raises ValueError if not float and not in range
        '''
        if isinstance(value, float):
            if value <= 4.0 and value >=0.0:
                self._gpa = value
            else:
                raise ValueError
        else:
            raise ValueError


    def __str__(self):
        '''
        use reST style
        :return: returns information in a string
        '''
        return self.last_name + ', ' + self.first_name + " has major " + self.major + " with GPA: " + str(self.gpa)

    def __repr__(self):
        '''
        use reST style
        :return: return string in program format
        '''
        return self.__str__()

    def display(self):
        '''
        use reST style
        :return: display information in a string
        '''
        return self.last_name + ', ' + self.first_name + " has major " + self.major + " with GPA: " + str(self.gpa)

if __name__ == '__main__':
    s = Student('Wayne', 'Bruce', 'Crimonology', 4.0)
    print(s.display)
