import unittest
from class_definitions import student as s

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.lname = 'Chan'
        self.fname = 'Jackie'
        self.major = 'Physics'
        self.gpa = 0.0
        self.student = s.Student('Chan', 'Jackie', 'Biology')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        #test constructor values set to only require attributes for acceptable values
        self.assertEqual(self.student.last_name, 'Chan')
        self.assertEqual(self.student.first_name, 'Jackie')
        self.assertEqual(self.student.major,'Biology')

    def test_object_created_all_attributes(self):
        #test constructor values set to all attributes for acceptable values
        student = s.Student('Chan', 'Jackie', 'Biology', 3.9) #this is not self.student from setUp, but local
        assert student.last_name == 'Chan'
        assert student.first_name == 'Jackie'
        assert student.major == 'Biology'
        assert student.gpa == 3.9


    def test_student_str(self):
        #test str() method
        pass

if __name__ == '__main__':
    unittest.main()
