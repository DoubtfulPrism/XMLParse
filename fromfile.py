import xml.etree.ElementTree as ET

tree = ET.parse('/home/doug/PycharmProjects/XMLParse/rough_data.xml')
root = tree.getroot()

LPN = root.findall('Lpn/LpnDetail')
print('LPN count:', len(LPN))

for LPN in root.iter('Lpn'):
    print('ReceivedDate', LPN.find('ReceivedDate').text)
    print('FacilityAliasID', LPN.find('FacilityAliasID').text)

for LpnDetail in root.iter('LpnDetail'):
    print('Item', LpnDetail.find('Item').text)
    print('ActualQuantity', LpnDetail.find('ActualQuantity').text)
