from lxml import etree as ET

root = ET.Element('SalesOrder')

level1 = ET.SubElement(root, 'CustomerID')
second1 = ET.SubElement(root, 'ATGOrderNumber')
second1 = ET.SubElement(root, 'SalesChannel')
second1 = ET.SubElement(root, 'Origin')
second1 = ET.SubElement(root, 'Webstore')
second1 = ET.SubElement(root, 'Language')
second1 = ET.SubElement(root, 'SaleCurrency')
second1 = ET.SubElement(root, 'TransferCurrency')
second1 = ET.SubElement(root, 'DistributionCentre')
second1 = ET.SubElement(root, 'OrderTotal')
second1 = ET.SubElement(root, 'DateEntered')
second1 = ET.SubElement(root, 'Source')
second1 = ET.SubElement(root, 'IsStaffOrder')
second1 = ET.SubElement(root, 'IsGift')

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

level1 = ET.SubElement(root, 'ShippingGroups')
level2 = ET.SubElement(level1, 'ShippingGroup')
second1 = ET.SubElement(level2, 'GWSOrderNumber')
second1 = ET.SubElement(level2, 'ATGOrderNumber')
second1 = ET.SubElement(level2, 'ShippingTotal')
second1 = ET.SubElement(level2, 'IsShippingTotalTaxInclusive')
level1 = ET.SubElement(level2, 'ShippingTaxes')
level2 = ET.SubElement(level1, 'ShippingTax')
second1 = ET.SubElement(level2, 'GWSOrderNumber')
second1 = ET.SubElement(level2, 'Type')
second1 = ET.SubElement(level2, 'Rate')
second1 = ET.SubElement(level2, 'Amount')

level1 = ET.SubElement(level1, 'ShippingMethod')

# level3 = ET.SubElement(level2, 'Morph')
# second1 = ET.SubElement(level3, 'Lemma')
# second1.text = 'sdfs'
# second1 = ET.SubElement(level3, 'info')
# second1.text = 'qw'
#
# level4 = ET.SubElement(level3, 'Aff')
# second1 = ET.SubElement(level4, 'Type')
# second1.text = 'sdfs'
# second1 = ET.SubElement(level4, 'Suf')
# second1.text = 'qw'

tree = ET.ElementTree(root)
tree.write('output.xml', pretty_print=True, xml_declaration=True, encoding="utf-8")
