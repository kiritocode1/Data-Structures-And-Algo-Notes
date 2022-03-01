import pandas as pd
import numpy as np

class databass:
    count = 0
    def __init__(self,name="dafault",age=99,std="class-01"):
        self.name = name 
        self.age = age 
        self.std  = std
        self.count+=1
        self.markys = []
        self.subjects = ("math","english","social","music")
    @property
    def email(self):
        ask = input('enter the email preferance --->gmail/hotmail/ just type it :    ')
        return f"{self.name}{self.std}@{ask}.com"
    @email.setter
    def email(self,other_email):
        self.email = other_email
    def marks(self):
        for _ in range(5):
            self.markys.append(int(input(f"enter the marks of {self.subjects[_]}")))
        print("thank you for ur time")


def final_database(f):
    all_students = f(input("enter the no of students --> "))
    
    pass








def fuck(numps)->dict:
    students = {}
    for _ in range(numps):
        print('/'*_)
        student = databass(input("enter the name -->"),int(input("enter the age -->")),input("enter the std--->"))
        students[f"{_}"] = student
    return students