import xml.etree.ElementTree as ET
import csv

tree = ET.parse("schooldata.xml")
root = tree.getroot()

# open a file for writing and give it the write permission
# open a file for writing
print 'Example: myfile.csv'
csvFile = raw_input('Enter the file to write to with the format: ')
School_data = open(csvFile, 'w')
print 'File creation and write permission granted'

# create the csv writer object, this object is the one that will write data(that we paas) into the csv file
csvwriter = csv.writer(School_data)
print 'Creating the csv writer object done'

#This list - array- is the one going to store the tags
school_head = []

count = 0
for member in root.findall('row'):
    if count == 0:
        #this section will run only once when we run the file
        #this section extract the tag name from the xml file
        category = member.find('category').tag
        school_head.append(category)

        school_name = member.find('school_name').tag
        school_head.append(school_name)

        address = member.find('address').tag
        school_head.append(address)

        city = member.find('city').tag
        school_head.append(city)

        zip_code = member.find('zip_code').tag
        school_head.append(zip_code)

        phone = member.find('phone').tag
        school_head.append(phone)

        url = member.find('url').tag
        school_head.append(url)

        csvwriter.writerow(school_head)
        count = count + 1

    school = [] #this list -array- is going to store the texts we extract
    #in this section of the loop we extract the text contents from the xml
    category = member.find('category').text
    school.append(category)

    school_name = member.find('school_name').text
    school.append(school_name)

    address = member.find('address').text
    school.append(address)

    city = member.find('city').text
    school.append(city)

    zip_code = member.find('zip_code').text
    school.append(zip_code)

    phone = member.find('phone').text
    school.append(phone)

    url = member.find('url').text
    school.append(url)

    csvwriter.writerow(school)
print 'XML file has been serialized to ', csvFile
School_data.close()
