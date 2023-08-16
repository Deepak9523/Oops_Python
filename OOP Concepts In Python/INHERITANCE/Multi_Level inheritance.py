# what is Multi Level Inheritance:-
# in this inheritance we have one parent class and multiple child class 
#synt:- class parent:
       # properties
       # class child(parent):
       # properties
       #class child1(child):
       # properties
# ********************* Multi level inheritance Coding *******************************

class father:
    surname="Singh"

class son(father):
    def show(self):
        print("Deepak",self.surname)

class Gson(son):
    def disp(self):
        print("Mahi",self.surname)

s=son()
s.show()

Gs=Gson()
Gs.disp() 
Gs.show()

# ***************** Multiple inheritance ************************
# what is multiple inheritance
# inheritance which contain more parent classes and only one child class is called multiple inheritance
# syntax:-class parent1:
#          properties
#        class parent1:
#          properties

#         class parent2:
#          properties 
#       
#        class parent3:
#          properties

#        class child(parent1,parent2,parent3):
#          properties

# *************** Coding***************

class Vivek:
    Back=("MySql DB,Python")
    def Backend(self):
        print("Suessfully:",self.Back)

class Priyanshu:
    Front=("Tkinter")
    def Frontend(self):
        print("Sucessfully:",self.Front)

class TeamLead(Vivek,Priyanshu):
    def show(self):
        print("Dyanmic Website created.....")
    
T=TeamLead()
T.Backend()
T.Frontend()
T.show()

# ************************* Hierarchical inheritance ***********************
# What is Hierarchical inheritance
# inheritance which contain only one parent class and multiple child class but each child class can acess parent class propertoes
# Syntex:-class parent:
# properties
# class child1(parent):
# properties
#class child2(parent):
# properties

# ************************** Coding *****************

class father:
    surname="Rajput"
    def show(self):
        print("My Surname is:",self.surname)

class son1(father):
    def disp(self):
        print("My name is Deepak",self.surname)

class son2(father):
    def out(self):
        print("My name is Trisha",self.surname)

s1=son1()
s2=son2()

s1.disp()
s1.show()
s2.out()
s2.show()