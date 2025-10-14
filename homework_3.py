class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation              # приватный атрибут
        self.__higher_education = higher_education  # приватный атрибут

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        edu_text = "есть высшее образование" if self.__higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.__occupation}. У меня {edu_text}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Я учился с Айсулуу в группе {self.group}. У меня {edu_text}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Мое хобби {self.hobby}. У меня {edu_text}.")


# Примеры
cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")

cl1.introduce()
fr1.introduce()
