'''
CREATE TABLE Specialties (
parentId INT,
id INT,
title VARCHAR(1000),
code VARCHAR(100),
description VARCHAR(1000));
'''
import sys

def main():
    # open the file and read it into a string
    f = open(sys.argv[1],'r')
    data_raw = f.read()
    f.close()

    # split on the \n
    data_lines = data_raw.split('\n')

    spec_insert = 'INSERT INTO Specialties (parentId, id, title, code, description) VALUES\n'

    # 1 so that we dont get the titles
    for i in range(1,len(data_lines)):
        data = data_lines[i].strip().split('\t')
        if len(data) == 5: # for the last line
            #if there is no parent id its id is now -1
            if len(data[0]) == 0:
                data[0] = '-1'
            spec_insert += '(' + data[0] + ',' + data[1] + ',"' + data[2] + '","' + data[3] + '","' + data[4].strip() + '")'
            if i == len(data_lines) - 2: # hack for newline
                spec_insert += ';'
            else:
                spec_insert += ',\n'

    f = open(sys.argv[2],'w')
    f.write(spec_insert)
    f.close()

    print 'Done'
            
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage file_to_load file_to_create'
        sys.exit(1)
    main()
