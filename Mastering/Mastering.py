import sys
import MySQLdb as mdb

def master(con):
	


def main():
	 con = mdb.connect(host='csc-db0.csc.calpoly.edu',user='jwilso43',passwd='abc123',db='jwilso43')
	 with con:
		con.query("""CREATE TABLE CopySP AS SELECT * FROM SourceProviders """)
	 
	 con.commit()
	 con.close()