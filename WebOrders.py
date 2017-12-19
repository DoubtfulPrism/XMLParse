import xml.etree.ElementTree as ET

tree = ET.parse('/home/doug/PycharmProjects/XMLParse/WebOrder.xml')
root = tree.getroot()

# LPN = root.findall('Lpn/LpnDetail')
# print('LPN count:', len(LPN))

for WO in root.iter('SalesOrder'):
    for Address in root.iter('Address'):
        print('ATGOrderNumber', WO.find('ATGOrderNumber').text)
        print('SalesChannel', WO.find('SalesChannel').text)
        print('Webstore', WO.find('Webstore').text)
        print('DateEntered', WO.find('DateEntered').text)
        print('ATGOrderNumber', Address.find('ATGOrderNumber').text)
        print('ShipToStoreID', Address.find('ShipToStoreID').text)
