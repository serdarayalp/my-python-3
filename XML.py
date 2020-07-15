import xml.etree.ElementTree as etree

myXML = '''
<current>
    <temperature value="289.731" min="289.731" max="289.731" unit="kelvin"/>
</current>
'''

tree = etree.fromstring(myXML)

temperatureInfo = tree.find('temperature')
degrees = temperatureInfo.attrib['value']

print(degrees)
