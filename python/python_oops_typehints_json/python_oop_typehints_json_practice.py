# ===== UNUSED IMPORTS =====
# These imports are currently not used in the program.
# from idna import valid_contextj
# from langchain_text_splitters import ExperimentalMarkdownSyntaxTextSplitter
# from pymupdf import f
# from curses.ascii import EM
# from regex import D


# ===== MOCK EMBEDDING FUNCTION =====
# This function returns a fake embedding/vector for given text.
def get_embedding(text):
    return [0.12, 0.55, 0.91]


vector = get_embedding("Insurance policy")
print(vector)


# ===== LOOP THROUGH MODEL NAMES =====
models = ["gpt 4.0", "claud sonet 4.0", "Gemini"]

for model in models:
    print(model)


# ===== DICTIONARY EXAMPLE =====
employee = {"name": "Your Name", "experience": 14, "target_salary": 100000}


# ===== FUNCTION USING DICTIONARY =====
def print_profile(employee):
    print(f"Name : {employee['name']}")
    print(f"Experience : {employee['experience']}")
    print(f"Target Salary : {employee['target_salary']}")


print_profile(employee)


# ===== ACCESS DICTIONARY VALUE =====
employee = {"name": "Kiran", "experience": 17}
print(employee["name"])


# ===== CLASS AND OBJECT =====
class AIModels:
    def __init__(self, model_name):
        self.model_name = model_name

    def ask(self, question):
        print(f"Using    : {self.model_name}")
        print(f"Question : {question}")


claude = AIModels("Claude Sonnet")
claude.ask("What is RAG?")


# ===== ENCAPSULATION WITH PROPERTY =====
class AIEngineeer:
    def __init__(self, name, experience, target_salary):
        self._name = name
        self._experience = experience
        self._target_salary = target_salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value

    def get_name(self):
        return f"Name : {self._name}"

    def get_experience(self):
        return f"Experience : {self._experience}"

    def get_target_salary(self):
        return f"Target Salary : {self._target_salary}"


personal_details = AIEngineeer("Kiran", 14, 100000)
print(personal_details.get_name())
print(personal_details.get_experience())
print(personal_details.get_target_salary())


# ===== PROPERTY SETTER VALIDATION =====
class Calculator:
    def __init__(self, number):
        self.number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if isinstance(value, int) and value > 0:
            print("Valid positive number")
            self.__number = value * 2
        else:
            raise ValueError("Invalid number")


calc = Calculator(5)
print(calc.number)


# ===== INHERITANCE =====
class Employee:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def display(self):
        print(f"Name : {self.name}")
        print(f"Experience : {self.experience}")


class AIEngineer(Employee):
    def build_agent(self):
        print(f"{self.name} is building an AI Agent")


engineer = AIEngineer("Kiran", 15)
engineer.display()
engineer.build_agent()


# ===== COMPOSITION EXAMPLE =====
class VectorStore:
    def search(self):
        print("Vector Search")


class RAGSystem:
    def __init__(self):
        self.vector_store = VectorStore()

    def ask(self):
        self.vector_store.search()


rag = RAGSystem()
rag.ask()


# ===== COMPOSITION WITH AI MODEL =====
class AIModell:
    def generate(self):
        print("Generating AI Response")


class AIAgent:
    def __init__(self):
        self.model = AIModell()

    def execute(self):
        self.model.generate()


agent = AIAgent()
agent.execute()


# ===== ABSTRACT CLASS =====
from abc import ABC, abstractmethod


class AIModel(ABC):
    @abstractmethod
    def generate(self):
        pass


class ClaudeModel(AIModel):
    def generate(self):
        print("Claude Response")


class GPTModel(AIModel):
    def generate(self):
        print("GPT Response")


class GeminiModel(AIModel):
    def generate(self):
        print("Gemini Response")


models = [ClaudeModel(), GPTModel(), GeminiModel()]

for model in models:
    model.generate()


# ===== STATIC METHOD =====
class MyClass:
    @staticmethod
    def greet(name):
        print("Welcome", name)


MyClass.greet("kiran")


# ===== STATIC METHOD AND INSTANCE METHOD =====
class Demo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def multiply(x, y):
        return x * y

    def diff(self):
        return self.a - self.b


print(Demo.multiply(10, 5))
calc = Demo(10, 5)
print(calc.diff())


# ===== DATACLASS EXAMPLE =====
from dataclasses import dataclass, field


@dataclass
class Rectangle:
    width: float
    height: float

    @staticmethod
    def area(width: float, height: float) -> float:
        return width * height


rect = Rectangle(10, 5)
print(rect)
print(Rectangle.area(10, 5))


# ===== DATACLASS FOR CHAT REQUEST =====
@dataclass
class ChatRequest:
    question: str
    temperature: float


request = ChatRequest("Explain RAG", 0.2)
print(request)


# ===== TYPE HINT FUNCTION =====
def generate_embedding1(text: str) -> list[float]:
    return [0.1, 0.2, 0.3]


vector = generate_embedding1("What is RAG?")
print(vector)


# ===== DUNDER METHOD __str__ =====
@dataclass
class Student:
    name: str
    marks: int

    def __str__(self):
        return f"Student {self.name} has {self.marks} marks"


print(Student("Kiran", 82))


# ===== DATACLASS EQUALITY CHECK =====
@dataclass
class Employeee:
    id: int
    name: str
    role: str
    salary: float


emp1 = Employeee(id=101, name="Kiran", role="SDET Trainer", salary=75000)
emp2 = Employeee(id=101, name="Kiran", role="SDET Trainer", salary=75000)
print(emp1 == emp2)


# ===== DATACLASS DEFAULT VALUE =====
@dataclass
class StudentWithGrade:
    name: str
    grade: str = "Not Assigned"


s1 = StudentWithGrade("Arun")
print(s1)


# ===== FROZEN DATACLASS =====
@dataclass(frozen=True)
class Config1:
    id: int
    data: list[int] = field(default_factory=list)


c = Config1(id=1)
c.data.append(10)
# c.data = [20]  # Error: frozen prevents reassignment.


# ===== EXCEPTION HANDLING =====
try:
    number = int(input("Enter a number: "))
    if number < 0:
        raise ValueError
    result = 100 / number
except ZeroDivisionError:
    print("Error! Cannot divide by zero")
except ValueError:
    print("Error: Invalid input, please enter a number.")
else:
    print(result)
finally:
    print("continue")


# ===== JSON PARSING =====
import json

employee = {"name": "Kiran", "experience": 17}
print(employee)
print(type(employee))
print(employee.get("name"))

employee_json = json.dumps(employee)
print(type(employee_json))


# ===== JSON STRING TO PYTHON DICTIONARY =====
employee_json = '{"name": "Kiran", "experience": 17}'
employee = json.loads(employee_json)

print(employee)
print(type(employee))
print(employee.get("name"))


# ===== LIST COMPREHENSION =====
numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number * number)

print(squares)
