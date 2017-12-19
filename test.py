import xml.etree.ElementTree as ET

tree = ET.parse('/home/doug/PycharmProjects/XMLParse/countryxml.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
