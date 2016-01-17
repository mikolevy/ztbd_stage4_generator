from random import randrange
from attribute import Attribute
from config import Config
from entity import Entity
from value import Value

__author__ = 'mikolevy'


class GeneratorLogic(object):

    def __init__(self):
        self.entities = self.generate_enitites()
        self.attributes = self.generate_attributes()
        self.values = self.generate_values()


    def generate_enitites(self):
        entities = []
        for entity_index in range(Config.ENTITIES_NUM):
            entities.append(Entity(entity_index + 1))
        return entities

    def generate_attributes(self):
        attributes = []
        for attr_index in range(Config.ATTRIBUTES_NUM):
            attributes.append(Attribute(attr_index + 1))
        return attributes

    def generate_values(self):
        values = []
        value_index = 1
        for entity in self.entities:
            value_per_entity = randrange(Config.MIN_VAL_PER_ENTITY, Config.MAX_VAL_PER_ENTITY)
            used_attributes = []
            for value_number in range(value_per_entity):
                attribute_index = randrange(0, Config.ATTRIBUTES_NUM)
                while attribute_index in used_attributes:
                    attribute_index += 1
                    if attribute_index == Config.ATTRIBUTES_NUM:
                        attribute_index = 0
                attribute = self.attributes[attribute_index]
                used_attributes.append(attribute_index)
                value_val = randrange(Config.MIN_VAL, Config.MAX_VAL)
                value = Value(value_index, entity.id, attribute.id, value_val, attribute)
                values.append(value)
                entity.values.append(value)
                value_index += 1
        return values

    def sql_to_file(self):
        lines = []
        for entity in self.entities:
            lines.append(entity.to_sql())
            lines.append(Config.NEW_LINE)
        for attribute in self.attributes:
            lines.append(attribute.to_sql())
            lines.append(Config.NEW_LINE)
        for value in self.values:
            lines.append(value.to_sql())
            lines.append(Config.NEW_LINE)

        sql_file = open(Config.SQL_FILE_PATH, "w")
        sql_file.writelines(lines)
        sql_file.close()

    def xml_to_file(self):
        lines = []
        for entity in self.entities:
            lines.append(entity.to_xml())
            lines.append(Config.NEW_LINE)

        sql_file = open(Config.XML_FILE_PATH, "w")
        sql_file.writelines(lines)
        sql_file.close()