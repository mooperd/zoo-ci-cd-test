
from sqlalchemy import Integer, Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()



# Genus is currently the "parent" of everything. It is the "root".
class Genus(Base):
    __tablename__ = 'genus'
    id = Column(Integer, primary_key=True)
    scientific_name = Column(String, unique=True)

    def __repr__(self):
        return "<Genus(scientific_name='%s')>" % (self.scientific_name)


# Species is a child of Genus
class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    scientific_name = Column(String, unique=True)
    common_name = Column(String)
    # We define the relationship between Species and Genus here.
    genus = relation("Genus", backref="species")
    genus_id = Column(Integer, ForeignKey('genus.id'))

    def __repr__(self):
        return "<Species(common_name='%s')>" % (self.common_name)


class Specimen(Base):
    __tablename__ = 'specimen'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    birth_date_time = Column(Integer)
    # We define the relationship between Species and Specimen here.
    species = relation("Species", backref="specimen")
    species_id = Column(Integer, ForeignKey('species.id'))

    def __repr__(self):
        return "<Specimen(name='%s')>" % (self.name)

# A bunch of stuff to make the connection to the database work.
def dbconnect():
    engine = create_engine('sqlite:///zoo.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()