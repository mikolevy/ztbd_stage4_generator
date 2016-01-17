__author__ = 'mikolevy'


class Entity(object):

    TABLE = "encje"
    ID = "encja_id"
    NAME = "nazwa"
    NAME_VAL_TEMPLATE = "Produkt"
    
    XML_TABLE = "encja_xml"
    XML_ID = "kod"
    XML_NAME = "nazwa"
    XML_ATTR = "opis"

    XML_ATTRIBUTES = "atrybuty"

    def __init__(self, entity_id):
        self.id = entity_id
        self.name = self.NAME_VAL_TEMPLATE + str(self.id)
        self.values = []

    def to_sql(self):
        return "INSERT INTO  {} ({}, {}) VALUES ({}, '{}');".format(
            self.TABLE, self.ID, self.NAME, self.id, self.name)

    def to_xml(self):
        values_xml = ""
        values_xml += self.XML_BEGIN(self.XML_ATTRIBUTES)
        for value in self.values:
            values_xml += value.to_xml()
        values_xml += self.XML_END(self.XML_ATTRIBUTES)

        return "INSERT INTO {} ({}, {}, {}) VALUES({}, '{}', XMLType('{}'))".format(
            self.XML_TABLE, self.XML_ID, self.XML_NAME, self.XML_ATTR, self.id, self.name, values_xml
        )

    def XML_BEGIN(self, string):
        return "<{}>".format(string)

    def XML_END(self, string):
        return "</{}>".format(string)
