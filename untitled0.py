# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 15:11:43 2026

@author: svivs
"""
#%% lambda

add1 = lambda num : num+1
# 함수이름 = lambda parameter : return 값
add1(1)
add1(2)

power = lambda base, exp : base**exp
power(2,2)

#%% class
class Dog:
    sex = 'F'
    name = ''
    owner = ''
    hp = 0
    
    # 생성자
    def __init__(self, sex, name, owner):
        self.sex = sex
        self.name = name
        self.owner = owner
    
    # 소멸자
    def __del__(self):
        print("소멸자 호출")
        
    # getter
    def getSex(self):
        return self.sex
    
    def getName(self):
        return self.name
    
    def getOwner(self):
        return self.owner
    
    def getHp(self):
        return self.hp
    
    # setter
    def setSex(self, sex):
        self.sex = sex
    
    def setName(self, name):
        self.name = name
    
    def setOwner(self, owner):
        self.owner = owner
    
    def setHp(self, hp):
        self.hp = hp
    
    # 메소드
    def bark(self):
        print("멍멍")
    
    def hand(self):
        print("손을 준다.")
    
    def poop(self):
        print("똥을 싼다.")
    
    def eat(self, food):
        foods = {
            'meat' : 100,
            'fish' : 70,
            'rice' : 30,
            'juckey' : 10
            }
        self.hp += foods[food]
        print(f"{food}를 먹었다. hp가 {self.hp}이 되었다.")
#%% main

dog = Dog('F', '멍뭉이', '이혜진')
print(dog.getHp())
dog.hand()
dog.eat('meat')
dog.eat('rice')
dog.bark()
dog.setOwner("누군가")
del dog