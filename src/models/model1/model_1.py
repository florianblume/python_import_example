from models import AbstractModel

class Model1(AbstractModel):

    def __init__(self):
        self.model1_string = 'Model1'
        print(self.model1_string)
        super().__init__()

    def train(self):
        print('train')