
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from model import dbconnect, Species, Specimen, Genus
from sqlalchemy import exc

app = Flask(__name__)
CORS(app)

@app.route('/genus', methods=['POST'])
def add_genus():
    session = dbconnect()
    request_dict = request.get_json()
    try:
        genus_instance = Genus()
        genus_instance.scientific_name = request_dict["scientific_name"]
        session.add(genus_instance)
        session.commit()
        return jsonify(genus_instance.id)
    except exc.IntegrityError:
        session.rollback()
        return "already exists", 400


@app.route('/species',  methods=['POST'])
def add_species():
    session = dbconnect()
    request_dict = request.get_json()
    try:
        genus_instance = session.query(Genus).filter(Genus.id == request_dict["genus"]["id"]).one()
    except:
        return "Genus does not exist, please add it", 400
    
    try:
        species = Species() 
        species.scientific_name = request_dict["scientific_name"]
        species.common_name = request_dict["common_name"]
        species.genus_id = genus_instance.id
        session.add(species)
        session.commit()
        return jsonify(species.id)
    except exc.IntegrityError:
        session.rollback()
        return "already exists", 400




@app.route('/specimen', methods=['POST'])
def add_specimen(): 
    session = dbconnect()
    request_dict = request.get_json()
    try: 
        species = session.query(Species).filter(Species.id == request_dict["species"]["id"]).one()
    except: 
        return "Species does not exist, please add it", 400
    try:
        specimen = Specimen()
        specimen.name = request_dict["name"]
        specimen.birth_date_time = request_dict["birth_date_time"]
        specimen.species_id = species.id    
        session.add(specimen)
        session.commit()
        return jsonify(specimen.id)
    except exc.IntegrityError:
        session.rollback()
        return "already exists", 400


@app.route('/genus/<search_term>', methods=['GET'])
def get_genus(search_term):
    session = dbconnect()
    return_list = []
    if search_term == "all":
        for row in session.query(Genus).all():
            row_dict = row.__dict__
            row_dict.pop("_sa_instance_state")
            return_list.append(row_dict)
    else:
        for row in session.query(Genus).filter(Genus.id == search_term).all():
            row_dict = row.__dict__
            row_dict.pop("_sa_instance_state")
            return_list.append(row_dict)
    return jsonify(return_list)

@app.route('/species/<search_term>', methods=['GET'])
def get_species(search_term):
    session = dbconnect()
    return_list = []
    if search_term == "all":
        for row in session.query(Species).all():
            row_dict = row.__dict__
            row_dict.pop("_sa_instance_state")
            return_list.append(row_dict)
    else:
        for row in session.query(Species).filter(Species.id == search_term).all():
            row_dict = row.__dict__
            row_dict.pop("_sa_instance_state")
            return_list.append(row_dict)
    return jsonify(return_list)

@app.route('/specimen/<search_term>', methods=['GET'])
def get_specimen(search_term):
    session = dbconnect()
    return_list = []
    if search_term == "all":
        for row in session.query(Specimen).all():
            row_dict = row.__dict__
            row_dict.pop("_sa_instance_state")
            return_list.append(row_dict)
    else:
        for row in session.query(Specimen).filter(Specimen.id == search_term).all():
            row_dict = row.__dict__
            row_dict.pop("_sa_instance_state")
            return_list.append(row_dict)
    return jsonify(return_list)



# to get the error message on the url
if __name__ == '__main__':

    app.run(debug=True)



