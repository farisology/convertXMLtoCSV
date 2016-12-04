import xml.etree.ElementTree as ET
import csv

tree = ET.parse("schoolsbeautified.xml")
root = tree.getroot()

# open a file for writing

School_data = open('parsedSchools.csv', 'w')
print 'File creation and write permission granted'
# create the csv writer object

csvwriter = csv.writer(School_data)
school_head = []

count = 0
for member in root.findall('row'):
    school = []
    if count == 0:
        category = member.find('category').tag #name
        school_head.append(category)

        school_name = member.find('school_name').tag #phoneNumber
        school_head.append(school_name)

        address = member.find('address').tag #Email address
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
School_data.close()
