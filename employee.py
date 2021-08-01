class Employee:
    def __init__(self, db_id, first_name, last_name, age, birthday, position, start_date, email):
        self.id = db_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birthday = birthday
        self.position = position
        self.start_date = start_date
        self.email = email

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.id, self.first_name, self.last_name, self.age, self.birthday,
                                                self.position, self.start_date, self.email)

    def __repr__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.id, self.first_name, self.last_name, self.age,
                                                self.birthday, self.position, self.start_date, self.email)
