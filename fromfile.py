import xml.etree.ElementTree as ET

tree = ET.parse('/home/doug/PycharmProjects/XMLParse/rough_data.xml')
root = tree.getroot()

LPN = root.findall('Lpn/LpnDetail')
print('LPN count:', len(LPN))

for item in LPN:
    print('Item', item.find('Item').text)
    print('ActualQuantity', item.find('ActualQuantity').text)
