print("------CLASS and OBJECT----------")
name=input("Enter the name:")
marks=int(input("Enter the marks:"))

class student:
    def get(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self,name,marks):
        return self.name,self.marks
        
obj=student()
obj.get(name,marks)
result=obj.display(name,marks)
print("Student name and mark:",(result))

------CLASS and OBJECT----------
Enter the name:df
Enter the marks:8
Student name and mark: ('df', 8)
---------------------

