# Name: Ali Hassan
# Roll no : F23BSEEN1E02030
# Assignment of Oop

class ConfigurationTemplate:
    def __init__(self, name, settings):
        self.name = name
        self.settings = settings

    def __str__(self):
        return "Template: " + self.name + ", Settings: " + str(self.settings)

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.template = None

    def assign_template(self, template):
        self.template = template

    def __str__(self):
        if self.template:
            return "Employee: " + self.name + ", Position: " + self.position + ", Template: " + self.template.name
        else:
            return "Employee: " + self.name + ", Position: " + self.position + ", Template: None"


template1 = ConfigurationTemplate("Basic", {"theme": "light", "font_size": 12})
template2 = ConfigurationTemplate("Advanced", {"theme": "dark", "font_size": 14})


employee1 = Employee("Ali", "Software Developer")
employee2 = Employee("Zain", "Web Developer")
employee1.assign_template(template1)
employee2.assign_template(template2)
print(employee1)
print(employee2)