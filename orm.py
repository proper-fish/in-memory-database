# the class that represents ORM containing all the necessary methods

from employee import Employee
from database import db
from datetime import date


class ORM:
    n = 1

    def save(first_name, last_name, age, birthday, position, start_date, email):
        employee = Employee(ORM.n, first_name, last_name, age, birthday, position, start_date, email)
        db.append(employee)
        ORM.n += 1

    def update(db_id, first_name, last_name, age, birthday, position, start_date, email):
        index = 0
        for employee in db:
            if employee.id == db_id:
                del db[index]
                employee = Employee(db_id, first_name, last_name, age, birthday, position, start_date, email)
                db.append(employee)
            index += 1

    def delete(db_id):
        index = 0
        for employee in db:
            if employee.id == db_id:
                del db[index]
            index += 1

    def find_by_id(db_id):
        for employee in db:
            if employee.id == db_id:
                return employee

    def list_by_position(position):
        return [employee for employee in db if employee.position == position]

    @staticmethod
    def turn_to_lists():
        listoflists = []
        for employee in db:
            sublist = [employee.id, employee.first_name, employee.last_name, employee.age, employee.birthday,
                       employee.position, employee.start_date, employee.email]
            listoflists.append(sublist)
        return listoflists

    @staticmethod
    def list_all_sort_by_age():
        return sorted(ORM.turn_to_lists(), key=lambda x: x[3])

    def find_born_after(birth_date):
        return [employee for employee in db if date.fromisoformat(employee.birthday) > date.fromisoformat(birth_date)]

    def find_by_full_name(full_name):
        first_name = full_name.split()[0]
        last_name = full_name.split()[1]
        for employee in db:
            if employee.last_name == last_name and employee.first_name == first_name:
                return employee

    @staticmethod
    def list_start_date_this_year():
        return [employee for employee in db if date.fromisoformat(employee.start_date).year >= date.today().year]
