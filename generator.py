from generator_logic import GeneratorLogic

__author__ = 'mikolevy'


def generate():
    generator = GeneratorLogic()
    generator.sql_to_file()
    generator.xml_to_file()

if __name__ == '__main__':
    generate()
