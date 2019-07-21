from models.model1 import Model1
from models import AbstractTrainer

class Trainer(AbstractTrainer):

    def __init__(self):
        self.trainer_model1_string = 'Trainer Model1'
        print(self.trainer_model1_string)
        model = Model1()
        model.train()
