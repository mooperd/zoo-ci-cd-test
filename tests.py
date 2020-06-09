import requests
import json

test_list = [
    {"name": "tubby", "dob": "1262304000", "species_common": "domestic cat", "species_scientific": "felis testus", "genus_scientific": "felis"}, 
    {"name": "batman", "dob": "1262304001", "species_common": "domestic dogo", "species_scientific": "dogo testus", "genus_scientific": "dogo"} 
]

def add_records(input_dict):   
    pload_genus = {"scientific_name": input_dict["genus_scientific"]}
    genus_request = requests.post("http://127.0.0.1:5000/genus" , json=pload_genus)
    genus_id = genus_request.text
    print(genus_id)
    
    if genus_request.status_code == 200: 
        pload_species = {"scientific_name": input_dict["species_scientific"], "common_name" : input_dict["species_common"], "genus" : { "id" : genus_id}}
        species_request = requests.post("http://127.0.0.1:5000/species" , json=pload_species)
        species_id = species_request.text   
        print(species_id)
    else :
        exit(1)

    if species_request.status_code == 200:
        pload_specimen = {"name": input_dict["name"], "birth_date_time" : input_dict["dob"], "species" : {"id" : species_id}}
        specimen_requests = requests.post("http://127.0.0.1:5000/specimen" , json=pload_specimen)
    
    else:
        exit(1)


for input_dict in test_list: 
    add_records(input_dict)