class Distance():
    UNIT_CONVERSION = {
        'cm': 0.1,
        'm':1,
        'km':1000
    }
    def __init__(self, value ,unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"
    @staticmethod
    def to_meters(value, unit):
        if unit not in Distance.UNIT_CONVERSION:
            raise ValueError(f"Не известная единица измерения: {unit}")
        return value * Distance.UNIT_CONVERSION[unit]
    @staticmethod
    def from_meters(value_in_meters,target_unit):
        if target_unit not in Distance.UNIT_CONVERSION:
            raise ValueError(f"Не известная единица измерения: {target_unit}")
        return value_in_meters / Distance.UNIT_CONVERSION[target_unit]

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_meters = self.to_meters(self.value, self.unit) + self.to_meters(other.value, other.unit)
        return Distance(self.from_meters(total_meters, self.unit), self.unit)
    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        diff_meters = self.to_meters(self.value , self.unit) - self.to_meters(other.value , other.unit)
        if diff_meters < 0:
            raise ValueError('результат вычитание не может быть отрицательным')
        return Distance(self.from_meters(diff_meters, self.unit), self.unit)
    def __eq__(self, other):
        return self.to_meters(self.value , self.unit) == self.to_meters(other.value , other.unit)
    def __lt__(self, other):
        return self.to_meters(self.value , self.unit) < self.to_meters(other.value , other.unit)
    def __le__(self, other):
        return self.to_meters(self.value , self.unit) <= self.to_meters(other.value , other.unit)
    def __gt__(self, other):
        return self.to_meters(self.value , self.unit) > self.to_meters(other.value , other.unit)
    def __ge__(self, other):
        return self.to_meters(self.value , self.unit) >= self.to_meters(other.value , other.unit)

d1 = Distance(500, 'cm')
d2 = Distance(2, 'm')
d3 = Distance(1, 'km')

print(d1)
print(d2)
print(d3)


print(d1 + d2)
print(d2 + d3)


print(d3 - d2)
print(d1 < d2)
print(d1 == Distance(5, 'm'))
print(d3 > d2)





