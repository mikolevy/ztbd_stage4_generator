__author__ = 'mikolevy'


class Value(object):

    TABLE = "wartosci_atrybutow"
    ID = "wartosc_atrybutu_id"
    ENTITY_ID = "encja_id"
    ATTRIBUTE_ID = "atrybut_id"
    VALUE = "wartosc"


    XML_ATTRIBUTE = "atrybut"
    XML_NAME = "nazwa"
    XML_VALUE = "wartosc"

    def __init__(self, value_id, entity_id, attr_id, value, attribute):
        self.id = value_id
        self.entity_id = entity_id
        self.attr_id = attr_id
        self.value = value
        self.attribute = attribute

    def to_sql(self):
        return "INSERT INTO  {} ({}, {}, {}, {}) VALUES ({}, {}, {}, {});".format(
            self.TABLE, self.ID, self.ENTITY_ID, self.ATTRIBUTE_ID, self.VALUE,
            self.id, self.entity_id, self.attr_id, self.value)

    def to_xml(self):
        return "{}{}{}{}{}{}{}{}".format(
            self.XML_BEGIN(self.XML_ATTRIBUTE),
            self.XML_BEGIN(self.XML_NAME), self.attribute.name, self.XML_END(self.XML_NAME),
            self.XML_BEGIN(self.XML_VALUE), self.value, self.XML_END(self.XML_VALUE),
            self.XML_END(self.XML_ATTRIBUTE)
        )

    def XML_BEGIN(self, string):
        return "<{}>".format(string)

    def XML_END(self, string):
        return "</{}>".format(string)
