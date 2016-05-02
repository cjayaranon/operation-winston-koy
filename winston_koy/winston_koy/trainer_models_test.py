import unittest

from models import trainer


class TrainersTestCase(unittest.TestCase):
    
    """Test for trainer models"""

    def setUp (self):
        pass

    def test_is_trainer_created(self):

        """Is trainer confirmed to be created unto the database?"""

        self.assertTrue(Trainers.objects.all())
        
if __name__ == '__main__':
    unittest.main()
