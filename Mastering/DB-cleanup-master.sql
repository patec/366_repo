use cperry03;

DROP TABLE IF EXISTS MasteredWorksAt;
DROP TABLE IF EXISTS MasteredHasPhoneNumber;
DROP TABLE IF EXISTS ReceivesMasteredMailAt;
DROP TABLE IF EXISTS MasteredSpeciality1;
DROP TABLE IF EXISTS MasteredSpeciality2;
DROP TABLE IF EXISTS Crosswalk;
DROP TABLE IF EXISTS Changes;
DROP TABLE IF EXISTS Audit;
DROP TABLE IF EXISTS MasterProviders;

CREATE TABLE IF NOT EXISTS MasterProviders(
	ID			INT UNIQUE NOT NULL AUTO_INCREMENT,
	Type			VARCHAR(13) NOT NULL,
	Name			VARCHAR(40),
	DoB 			DATE,
	IsSoleProprietor	VARCHAR(1),
	Gender			VARCHAR(1),
	Established		DATE, 
	PRIMARY KEY(ID)
);
CREATE TABLE IF NOT EXISTS Audit(
	AuditNum		INT UNIQUE NOT NULL AUTO_INCREMENT,
	Date			DATE,
	Comment			VARCHAR(300),
	CodeLine		INT,
	Active			BOOLEAN,
    	PRIMARY KEY(AuditNum)
);
CREATE TABLE IF NOT EXISTS MasteredSpeciality1(
	MasterID		INT,
	Speciality		INT,
	PRIMARY KEY(MasterID, Speciality),
	FOREIGN KEY(MasterID) REFERENCES MasterProviders(ID),
	FOREIGN KEY(Speciality) REFERENCES Specialities(ID)
);
CREATE TABLE IF NOT EXISTS MasteredSpeciality2(
	MasterID 		INT,
	Speciality 		INT,
	PRIMARY KEY(MasterID, Speciality),
	FOREIGN KEY(MasterID) REFERENCES MasterProviders(ID),
	FOREIGN KEY(Speciality) REFERENCES Specialities(ID)
);
CREATE TABLE IF NOT EXISTS Crosswalk(
	SourceID		INT,
	MasterID		INT,
	PRIMARY KEY(SourceID, MasterID),
	FOREIGN KEY(SourceID) REFERENCES SourceProviders(ID),
	FOREIGN KEY(MasterID) REFERENCES MasterProviders(ID)
);
CREATE TABLE IF NOT EXISTS MasteredWorksAt(
	MasterID		INT,
	SourceID		INT,
	PRIMARY KEY(MasterID, SourceID),
	FOREIGN KEY(MasterID) REFERENCES MasterProviders(ID),
	FOREIGN KEY(SourceID) REFERENCES SourceProviders(ID)
);
CREATE TABLE IF NOT EXISTS ReceivesMasteredMailAt(
	MasterID		INT,
	SourceID		INT,
	PRIMARY KEY(MasterID, SourceID),
	FOREIGN KEY(MasterID) REFERENCES MasterProviders(ID),
	FOREIGN KEY(SourceID) REFERENCES SourceProviders(ID)
);
CREATE TABLE IF NOT EXISTS Changes(
	AuditNumber		INT,
	MasterID		INT,
	SourceID		INT,
	PRIMARY KEY(AuditNumber, MasterID, SourceID),
	FOREIGN KEY(AuditNumber) REFERENCES Audit(AuditNum),
	FOREIGN KEY(MasterID) REFERENCES MasterProviders(ID),
	FOREIGN KEY(SourceID) REFERENCES SourceProviders(ID)
);
CREATE TABLE IF NOT EXISTS MasteredHasPhoneNumber(
	MasterID		INT,
	SourceID		INT,
	PRIMARY KEY(MasterID, SourceID),
	FOREIGN KEY(MasterID) REFERENCES MasterProviders(ID),
	FOREIGN KEY(SourceID) REFERENCES PhoneNumbers(SourceID)
);
