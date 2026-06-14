class employee:
    department = "Finance"
    name = "Jordan"

    def greeting(self):
        print("Hello! I am an employee")

    def info(self):
        print("My name is", self.name)
        print("I work in the", self.department, "department")

obj = employee()
obj.greeting()
obj.info()