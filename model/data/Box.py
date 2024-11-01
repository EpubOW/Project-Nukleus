from config import *
from model.data.BaseData import *

class Box(BaseData):
    __tablename__ = 'box'
    
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    x1 = Column(Double, nullable=False) # in percents
    y1 = Column(Double, nullable=False) # in percents
    x2 = Column(Double, nullable=False) # in percents
    y2 = Column(Double, nullable=False) # in percents
    
    def __init__(self, name, description, x1, y1, x2, y2, id=None):
        super().__init__(id)
        
        self.name = name
        self.description = description
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def getInfo(self):
        return [self.name, self.description, self.x1, self.y1, self.x2, self.y2, self.id]
        