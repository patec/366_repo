import sys
import MySQLdb as mdb

def load():

    con = mdb.connect(host='csc-db0.csc.calpoly.edu',user='jwilso43',passwd='abc123',db='jwilso43')

    with con:
       
        cur = con.cursor()

        # clean up
        f = open('DB-cleanup.sql','r')
        sql = f.read()
        f.close()
        sql = sql.split(';')[:-1]
        for s in sql:
            cur.execute(s)
       
        # set up
        f = open('DB-setup.sql','r')
        sql = f.read()
        f.close()
        sql = sql.split(';')[:-1]
        for s in sql:
            cur.execute(s)

        # open the file and read it into a string
        f = open('Specialties.tsv','r')
        data_raw = f.read()
        f.close()

        data_lines = data_raw.split('\n')[:-1]
        
        # insert all of the specialties data
        for i in range(1,len(data_lines)):
            data = data_lines[i].split('\t')
            cd = []
            for d in data:
                d = d.strip()
                if d == '':
                    d = None
                cd.append(d)
        
            parentid = cd[0]
            id = cd[1]
            title = cd[2]
            code = cd[3]
            url = cd[4]
            cur.execute('INSERT INTO Specialities VALUES(%s,%s,%s,%s,%s)',(parentid,id,title,code,url))
            
            if i % 1000 == 0:
                print 'Inserted ' + str(i) + ' rows...'
        
        # open the file and read it into a string
        f = open('Providers.tsv','r')
        data_raw = f.read()
        f.close()
        
        data_lines = data_raw.split('\n')[:-1]
        
        # insert all of the source providers data
        for i in range(1,len(data_lines)):
            data = data_lines[i].split('\t')
            cd = []
            for d in data:
                d = d.strip()
                if d == '':
                    d = None
                cd.append(d)
            id = cd[0]
            type = cd[1]
            name = cd[2] 
            gender = cd[3] 
            dob = cd[4] 
            isp = cd[5]
            m_street = cd[6]
            m_unit = cd[7]
            m_city = cd[8] 
            m_region = cd[9] 
            m_postcode = cd[10]
            m_county = cd[11]
            m_country = cd[12]
            p_street = cd[13]
            p_unit = cd[14]
            p_city = cd[15] 
            p_region = cd[16] 
            p_postcode = cd[17]
            p_county = cd[18]
            p_country = cd[19]
            phone = cd[20]
            p_spec = cd[21] 
            s_spec = cd[22] 
       
            cur.execute('INSERT INTO SourceProviders VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(id,type,name,gender,dob,isp,p_spec,s_spec))
            if m_street != None or m_unit != None or m_city != None or m_region != None or m_postcode != None or m_county != None:
                cur.execute('INSERT INTO Addresses VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(id,'m',m_street,m_city,m_country,m_postcode,m_unit,m_unit,m_region))
            if p_street != None or p_unit != None or p_city != None or p_region != None or p_postcode != None or p_county != None:
                cur.execute('INSERT INTO Addresses VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(id,'p',p_street,p_city,p_country,p_postcode,p_unit,p_unit,p_region))
            if phone != None:
                cur.execute('INSERT INTO PhoneNumbers VALUES(%s,%s)',(id,phone))
   
            if i % 1000 == 0:
                print 'Inserted ' + str(i) + ' rows...'

    con.commit()
    con.close()
    
def compare(master, row):    

    r_type = r_name = r_dob = r_isop = r_gen = ''

    if row[1] != None:
        r_type = row[1]
    if row[2] != None:
        r_name = row[2]
    if row[3] != None:
        r_dob = row[3]
    if row[4] != None:
        r_isop = row[4]
    if row[5] != None:
        r_gen = row[5]
    
    # concat what were comparing
    comp = r_type + r_name + r_dob + r_isop + r_gen          
    
    if comp in master:
        return True, comp
    
    return False, comp
    
def match():
    
    con = mdb.connect(host='csc-db0.csc.calpoly.edu',user='jwilso43',passwd='abc123',db='jwilso43')

    with con:
       
        cur = con.cursor()
    
        cur.execute('SELECT * FROM SourceProviders')
        rows = cur.fetchall()
      
        master = {}
        
        for i in range(len(rows)):
            
            row = rows[i]
            r_id = row[0]
           
            result, comp = compare(master, row)
            
            if result:
                master[comp].append(r_id)
            else:
                master[comp] = [r_id]

        for m in master:
            m = master[m]
            if len(m) > 1:
                print m
        print len(master)
    
    con.close()
        
            
if __name__ == '__main__':
    #load()
    match()
