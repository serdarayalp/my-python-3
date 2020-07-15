import xml.etree.ElementTree as ET

namespaces = {'ns': 'urn:jboss:domain:10.0'}

tree = ET.parse("standalone-rcutil-at-dev.xml")
root = tree.getroot()


deployments = root.find("ns:deployments", namespaces)

root.remove(deployments)
tree = ET.ElementTree(root)

tree.write("standalone-rcutil-at-dev-5.xml")
