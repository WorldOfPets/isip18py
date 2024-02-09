class User:
    def __init__(self, out_age, out_name):
        self._age = out_age
        self._name = out_name

    @property
    def name(self) -> str:
        return "default"
    
    @property
    def age(self) -> str:
        return self._age
    
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Возраст не может быть меньше нуля")
            self._age = 18


    def say(self):
        if self.age >= 18:
            print(f"Hello my name is {self.name}. My age is {self.age}")
        else:
            print(f"Bye bye {self.name}! You so young!")

user1 = User(180, "isip18")
user1.age = 190
print(user1.age)





def name_function(name, age):
    if age >= 18:
        return f"Hello {name}"
    else:
        return f"Bye bye {name}. You so young!"
    
    

# result = name_function("isip18!", 189)
# print(result.upper())
# name_function("daler!", 15)
# name_function("liza!", 18)