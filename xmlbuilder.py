from lxml import etree as ET

root = ET.Element('SalesOrder')

level1 = ET.SubElement(root, 'CustomerID')
second = ET.SubElement(root, 'ATGOrderNumber')
second = ET.SubElement(root, 'SalesChannel')
second = ET.SubElement(root, 'Origin')
second = ET.SubElement(root, 'Webstore')
second = ET.SubElement(root, 'Language')
second = ET.SubElement(root, 'SaleCurrency')
second = ET.SubElement(root, 'TransferCurrency')
second = ET.SubElement(root, 'DistributionCentre')
second = ET.SubElement(root, 'OrderTotal')
second = ET.SubElement(root, 'DateEntered')
second = ET.SubElement(root, 'Source')
second = ET.SubElement(root, 'IsStaffOrder')
second = ET.SubElement(root, 'IsGift')

level1 = ET.SubElement(root, 'Addresses')
level2 = ET.SubElement(level1, 'Address')
second1 = ET.SubElement(level2, 'ATGOrderNumber')
second1 = ET.SubElement(level2, 'Type')
second1 = ET.SubElement(level2, 'ShipToStoreID')
second1 = ET.SubElement(level2, 'FirstName')
second1 = ET.SubElement(level2, 'LastName')
second1 = ET.SubElement(level2, 'Address1')
second1 = ET.SubElement(level2, 'Address2')
second1 = ET.SubElement(level2, 'City')
second1 = ET.SubElement(level2, 'StateProvince')
second1 = ET.SubElement(level2, 'PostalCode')
second1 = ET.SubElement(level2, 'Country')
second1 = ET.SubElement(level2, 'ContactPhone')
second1 = ET.SubElement(level2, 'ContactEmail')

level1 = ET.SubElement(root,'ShippingGroups')
level2 = ET.SubElement(level1, 'ShippingGroup')
second2 = ET.SubElement(level2, 'GWSOrderNumber')
second2 = ET.SubElement(level2, 'ATGOrderNumber')
second2 = ET.SubElement(level2, 'ShippingTotal')
second2 = ET.SubElement(level2, 'IsShippingTotalTaxInclusive')
level1 = ET.SubElement(level2, 'ShippingTaxes')
level2 = ET.SubElement(level1, 'ShippingTax')
second3 = ET.SubElement(level2, 'GWSOrderNumber')
second3 = ET.SubElement(level2, 'Type')
second3 = ET.SubElement(level2, 'Rate')
second3 = ET.SubElement(level2, 'Amount')

level1 = ET.SubElement(root, 'ShippingMethod')


tree = ET.ElementTree(root)
tree.write('output.xml', pretty_print=True, xml_declaration=True, encoding="utf-8")


# with open("output.xml", 'w') as xml:
#     print(tree, file=xml)