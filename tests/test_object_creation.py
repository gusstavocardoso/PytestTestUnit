from src.object_creation import Person

def test_person_greet():
    person = Person("Alice", 30)
    assert person.greet() == "Hello, my name is Alice and I am 30 years old"

def test_person_creation():
    person1 = Person("Bob", 25)
    assert person1.name == "Bob"
    assert person1.age == 25

    person2 = Person("Charlie", 40)
    assert person2.name == "Charlie"
    assert person2.age == 40

def test_person_greet_empty_name():
    person = Person("", 30)
    assert person.greet() == "Hello, my name is  and I am 30 years old"

def test_person_greet_negative_age():
    person = Person("David", -20)
    assert person.greet() == "Hello, my name is David and I am -20 years old"

def test_person_creation_empty_name():
    person = Person("", 25)
    assert person.name == ""
    assert person.age == 25

def test_person_creation_negative_age():
    person = Person("Eve", -25)
    assert person.name == "Eve"
    assert person.age == -25