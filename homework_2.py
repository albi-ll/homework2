class Person(object):
    def __init__(self, name, brith_date, occupation, higher_education):
        self.first_name = name
        self.brith_date = brith_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет! Меня зовут {self.first_name}, моя профессия — {self.occupation}, и у меня {education}.")


class Classmate(Person):
    def __init__(self, name, brith_date, occupation, higher_education, group_name):
        super().__init__(name, brith_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, Меня зовут {self.first_name}," f" Я друг {self.group_name} "
              f"Я родилась {self.brith_date}. " f"работаю {self.occupation}, "
              f"у меня {self.higher_education}")


class Friend(Person):
    def __init__(self, name, brith_date, occupation, higher_education, hobby):
        super().__init__(name, brith_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, Меня зовут {self.first_name}, я родился{self.brith_date}"
              f"Я работаю {self.occupation}" f" мое хобби  {self.hobby}")


classmate1 = Classmate("Айдай", "5.12.2010", "программист", True, "Байеля")
classmate2 = Classmate("Айдана", "8.03.2001", "дизайнер", True, "Азата   ")

friend1 = Friend("Алмаз", "10.10.1999", "инженер", True, "футбол")
friend2 = Friend("Бектур", "12.04.2005", "врач", True, "чтение книг")
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()

