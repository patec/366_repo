import sys

''' 0 ID TYPE NAME GENDER DOB SOLE_PROP 
6 M_STREET M_UNIT M_CITY M_REGION M_POSTCODE M_COUNTY M_COUNTRY 
13 P_STREET P_UNIT P_CITY P_REGION P_POSTCODE P_COUNTY P_COUNTRY
20 PHONE P_SPEC S_SPEC
'''

def main():
    # open the file and read it into a string
    f = open(sys.argv[1],'r')
    data_raw = f.read()
    f.close()

    # split on the \n
    data_lines = data_raw.split('\n')

    # insert statements
    phone_insert = 'INSERT INTO PhoneNumbers (SourceId, PhoneNumber)'
    prov_insert = 'INSERT INTO SourceProviders (ID, Type, Name, Gender, DoB, IsSoleProprietor, PrimarySpecialty, SecondarySpecialty) VALUES\n'
    address_insert = 'INSERT INTO Address (SourceId, Type, Street, Unit, City, Region, PostCode, County, Country)\n'
    
    for i in range(1, len(data_lines)):
        
        data = data_lines[i].split('\t')
        # for last line
        if len(data) == 23:
            prov_insert += '('+data[0]+',"'+data[1]+'","'+data[2]+'","'+data[3]+'","'+data[4]+'","'+data[5]+'","'+data[21]+'","'+data[22].strip()+'")'
            address_insert += '('+data[0]+',"m","'+data[6]+'","'+data[7]+'","'+data[8]+'","'+data[9]+'","'+data[10]+'","'+data[11]+'","'+data[12]+'"),\n'
            address_insert += '('+data[0]+',"p","'+data[13]+'","'+data[14]+'","'+data[15]+'","'+data[16]+'","'+data[17]+'","'+data[18]+'","'+data[19]+'")'
            phone_insert += '('+data[0]+',"'+data[20]+'")'    
        
        if i == len(data_lines) - 2: # hack for newline
            prov_insert += ';\n'
            address_insert += ';\n'
            phone_insert += ';\n'
            break
        else:
            prov_insert += ',\n'
            address_insert += ',\n'
            phone_insert += ',\n'

    f = open(sys.argv[2],'w')
    f.write(prov_insert)
    f.write(address_insert)
    f.write(phone_insert)
    f.close()

    print 'Done'
            
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage file_to_load file_to_create'
        sys.exit(1)
    main()
