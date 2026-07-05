class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name=None, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls,name=None, hours=None, rest_days=None, email=None):
        if hours is None:
            return cls(name=name, hours=(7 - rest_days)*8, rest_days=rest_days, email=email)
        else:
            return cls(name=name, hours=hours, rest_days=rest_days, email=email)

    @classmethod
    def get_email(cls,name=None, hours=None, rest_days=None, email=None):
        if not email:
            return cls(name=name, hours=hours, rest_days=rest_days, email=f'{name}@email.com')
        else:
            return cls(name=name, hours=hours, rest_days=rest_days, email=email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hourly_payment * self.hours
