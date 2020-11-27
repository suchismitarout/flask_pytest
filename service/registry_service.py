from registry import data
import logging


class RegistryService():
    def get_all_data(self):
        """
            to get all students information
        """
        return data.students

    def get_all_data_by_name(self, name):
        """
            to get students by name from registry module
        """
        students = data.students
        logging.info("got all students info:{}".format(students))
        for student in students:
            if student['name'] == name:
                return student

    def get_all_data_by_id(self, id):
        """
            it'll get students by id from registry module
        """
        students = data.students
        logging.info("got all students info:{}".format(students))

        for student in students:
            if student['id'] == int(id):
                return student


