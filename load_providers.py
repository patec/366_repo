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
    phone_insert1 = 'INSERT INTO PhoneNumbers (SourceId, PhoneNumber) VALUES '
    prov_insert1 = 'INSERT INTO SourceProviders (ID, Type, Name, Gender, DoB, IsSoleProprietor, PrimarySpeciality, SecondarySpeciality) VALUES '
    address_insert1 = 'INSERT INTO Addresses (SourceId, Type, Street, Unit, City, Region, PostCode, County, Country) VALUES '
    prov_insert = ""
    phone_insert = ""
    address_insert = ""
    
    for i in range(1, len(data_lines)):
        
        data = data_lines[i].split('\t')
        # for last line
        if len(data) == 23:
            primaryspec = data[21]
            secondaryspec = data[22].strip()
            if len(data[21]) == 0:
               primaryspec = "NULL"
            else:
               primaryspec = '"' + primaryspec + '"'
            if len(secondaryspec) == 0:
               secondaryspec = "NULL"
            else:
               secondaryspec = '"' + secondaryspec + '"'
            prov_insert += prov_insert1 + '('+data[0]+',"'+data[1]+'","'+data[2]+'","'+data[3]+'","'+data[4]+'","'+data[5]+'",'+primaryspec+','+ secondaryspec+');\n'
            address_insert += address_insert1 + '('+data[0]+',"m","'+data[6]+'","'+data[7]+'","'+data[8]+'","'+data[9]+'","'+data[10]+'","'+data[11]+'","'+data[12]+'");\n'
            address_insert += address_insert1 + '('+data[0]+',"p","'+data[13]+'","'+data[14]+'","'+data[15]+'","'+data[16]+'","'+data[17]+'","'+data[18]+'","'+data[19]+'");\n'
            phone_insert += phone_insert1 + '('+data[0]+',"'+data[20]+'");\n'    
        '''
        if i == len(data_lines) - 2: # hack for newline
            #prov_insert += ';\n'
            address_insert += ';\n'
            phone_insert += ';\n'
            break
        
        else:
            #prov_insert += ',\n'
            address_insert += ',\n'
            phone_insert += ',\n'
        '''
        

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
