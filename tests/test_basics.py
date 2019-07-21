import unittest

import sys
sys.path.insert(0, '/home/florian/projects/project/src')
#sys.path.insert(0, '/home/florian/projects/project/src/sub1/sub2')
print(sys.path)

class TestMe(unittest.TestCase):
    def test_util(self):
        import util
        assert util.util_string == 'util'
    def test_model1(self):
        from models.model1 import Model1
        model1 = Model1()
        assert model1.model1_string == 'Model1'
    def test_train(self):
        from models.model1 import Trainer
        trainer = Trainer()
        assert trainer.trainer_model1_string == 'Trainer Model1'
    def test_data(self):
        from data import DataLoader
        data_loader = DataLoader()
        assert data_loader.dataloader_string == 'DataLoader'

if __name__ == '__main__':
    unittest.main()
