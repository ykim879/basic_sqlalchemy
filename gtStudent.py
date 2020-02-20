from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory:', echo=True) #created engne
Session = sessionmaker(bind=engine) #made session before creating engine(=no parameter)-> Session.configure(bind=engine)
Base = declarative_base()

class GTStudent(Base): #base enable to created any number of mapped classes
	__tablename__ = 'GTStudent' #class will be mapped in to this table

	gtid = Column(Integer, primary_key=True) #need at least one primary key
	name = Column(String) # name and datatype of columns
	graduateYear = Column(Integer)
	gpa = Column(Float)

	def __repr__(self):
		return "Student info: \n\tGTid: %d \n\tname: %s\n\tExpected graduate year: %d\n\tCurrent GPA: %.2f" % \
		(self.gtid, self.name, self.graduateYear, self.gpa)
session = Session() #Whenever you need to have a conversation with the database, you instantiate a Session:
Base.metadata.create_all(engine) #passing in our Engine as a source of database connectivity
#print "This is the table: \n", GTStudent.__table__
yiyeon = GTStudent(gtid = 903550379, name = 'Yiyeon', graduateYear = 2021, gpa = 4.0)
session.add(yiyeon) #session maker has no attribute of add()
checkYiyeon = session.query(GTStudent).filter_by(name = 'Yiyeon').first()
print "is checkYiyeon as same as yiyeon: ", checkYiyeon is yiyeon
print checkYiyeon
#test add_all
session.add_all ([GTStudent(gtid = 99887777, name = 'Suggie', graduateYear = 2022, gpa = 3.9), GTStudent(gtid = 9922384756, name = 'Will', graduateYear = 2022, gpa = 3.8)])
#check data
for student in session.query(GTStudent):
	print student
#put data with null
session.add(GTStudent(gtid = 44444444, name = 'Racheal', graduateYear = 2021)) #leave gpa as null
checkRacheal = session.query(GTStudent).filter_by(gtid = 44444444).first()
#print checkRacheal#cannot print because of none

#revise Racheal
checkRacheal.gpa = 3.8
print checkRacheal # after emitting none, possible to print
#check session.dirty
for student in session.dirty:
	print student #inside of session dirty there is racheal

