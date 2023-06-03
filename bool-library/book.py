import random
from pydantic import BaseModel

class book(BaseModel):
    bookID:int
    title:str
    author:str
    year:int
    # def __init__(self, titleNew, authorNew, yearNew):
    #     bookID = int(random.random())
    #     title = titleNew
    #     auther = authorNew
    #     year = yearNew
    # def __repr__(self):
    #     return str("Title: ",title, ". Author: ",author," Year: ", year, " ID: ",bookID)
    def getID(self):
        return id