
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask
from flask import jsonify
from flask import request
from model import Species, Specimen, Genus, dbconnect
app = Flask(__name__)

Base = declarative_base()


def addSpecimen(session, specimen_input):
    try:  # Lets check if we can retreive the species matching the specimen record.
        species = session.query(Species).filter(Species.scientific_name == specimen_input["species"]["scientific_name"]).one()
    except:
        species = Species()
        species.scientific_name = specimen_input["species"]["scientific_name"]
        session.add(species)
    specimen = Specimen()
    specimen.name = specimen_input["name"]
    specimen.birth_date_time = specimen_input["birth_date_time"]
    specimen.species = species
    session.add(specimen)
    session.commit()


def addSpecies(session, species_input):
    genus = Genus()
    try: 
        genus = session.query(Genus).filter(Genus.scientific_name == species_input["genus"]["scientific_name"]).one()
    except:
        genus = Genus()
        genus.scientific_name = species_input["genus"]["scientific_name"]
        session.add(genus)
    species = Species()
    species.scientific_name = species_input["scientific_name"]
    species.common_name = species_input["common_name"]
    species.genus = genus
    session.add(species)
    session.commit()

# I want to create functions that add Genus, Species and Specimen. Then these fundctions will be called in the endpoints

def addGenus(session, genus_input):
    print("creating new Genus:" + genus_input)
    genus = Genus()
    try: 
        genus = session.query(Genus).filter(Genus.scientific_name == genus_input["scientific_name"]).one()
        print(genus)
        return genus
    except:
        genus.scientific_name = genus_input["scientific_name"]
        result = session.add(genus)
        print(result)
        return result


def addSpecies2(session, species_input):
    genus_id = addGenus(session, species_input["genus"])
    print("creating new Species:" + species_input)
    species = Species()
    species.scientific_name = species_input["scientific_name"]
    species.common_name = species_input["common_name"]
    species.genus = genus_id
    session.add(species)
    session.commit()


