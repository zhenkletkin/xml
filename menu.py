
'''
    this program will create in the current directory a simple XML file and then immediately read it, giving us some information.
'''

#creating xml file to system from python

import xml.etree.ElementTree as et

menu_str = '''
<?xml version="1.0"?>
<menu>
	<breakfast hours="7-11">
		<item price="$6.00">burritos</item>
		<item price="$4.00">pancakes</item>
	</breakfast>
	<lunch hours="11-3">
		<item price="$5.00">hamburger</item>
	</lunch>
	<dinner hours="3-10">
		<item price="8.00">spaghetti</item>
	</dinner>
</menu>
'''[1:]

menu_xml = et.XML(menu_str)
tree = et.ElementTree(menu_xml)
tree.write('menu.xml')

#reading xml file in python
#we can read xml by et.ElementTree(file=...) and et.parse(...) methods

tree2 = et.ElementTree(file='menu.xml')
root = tree2.getroot()
print('')
print('root tag:', root.tag)
print('')
for child in root:
    print('for {} ({}) we have:'.format(child.tag, child.attrib['hours']))
    for grandchild in child:
        print('  {}\t{}'.format(grandchild.text, grandchild.attrib['price']))
print('')

#another way of reading( et.parse )
#I won't iterate through menu children but print only root tag

from xml.etree.ElementTree import parse

tree3 = et.parse('menu.xml')
root2 = tree3.getroot()
print('root tag is also', root2.tag + ' (created through parse method")')
