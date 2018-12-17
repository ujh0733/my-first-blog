
import xml.etree.ElementTree as etree

f = open('test.xml', 'r')
text = f.read()
f.close()

print ("\n[Python Debug My Text]")
print(text)
print("[Python Debug End of My Text]\n")

root = etree.fromstring(text)
print("--------------------------------")
print('tag : ',root[0].tag, 'attributes: ',root[0].attrib)

print("--------------------------------")
print("id : " + root[0].attrib['id'])
print(root[0].attrib['name'])
print(root[0].attrib['address'])
print(root[0].attrib['lat'])
print(root[0].attrib['lng'])
print(root[0].attrib['type'])
