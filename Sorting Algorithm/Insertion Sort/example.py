class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

def insertion_sort(persons):
    for i in range(len(persons)):
        j = i
        while j > 0 and persons[j-1] > persons[j]:
            persons[j-1], persons[j] = persons[j], persons[j-1]
            j = j-1

if __name__ == '__main__':
    per1 = Person("Hrishi", 26)
    per2 = Person("Apurava", 32)
    per3 = Person("Sima", 27)
    per4 = Person("Simada", 89)
    per5 = Person("SimaYWDGIQW", 2)
    persons = [per1,per2,per3,per4,per5]
    insertion_sort(persons)

    for person in persons:
        print(person.name)


