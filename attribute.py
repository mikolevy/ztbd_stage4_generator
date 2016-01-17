__author__ = 'mikolevy'


class Attribute(object):

    TABLE = "atrybuty"
    ID = "atrybut_id"
    NAME = "nazwa"
    NAME_VAL_TEMPLATE = "Atrybut"

    def __init__(self, attr_id):
        self.id = attr_id
        self.name = self.NAME_VAL_TEMPLATE + str(self.id)

    def to_sql(self):
        return "INSERT INTO  {} ({}, {}) VALUES ({}, '{}');".format(
            self.TABLE, self.ID, self.NAME, self.id, self.name)