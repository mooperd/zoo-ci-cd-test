from import_functions import addSpecimen, addSpecies
# from model import Species, Specimen, Genus, dbconnect
from model import dbconnect


# Define a list of dicts of our species.
species_list = [
    {"common_name": "Domestic Cat", "scientific_name": "Felis catus", "genus": {"scientific_name": "Felis"} },
    {"common_name": "Black Footed cat", "scientific_name": "Felis nigripes", "genus": {"scientific_name": "Felis"}},
    {"common_name": "Jungle cat", "scientific_name": "Felis chaus", "genus": {"scientific_name": "Felis"}},
    {"common_name": "Domestic Dog", "scientific_name": "Canis familiaris", "genus": {"scientific_name": "Canis"}},
    {"common_name": "Elk", "scientific_name": "Cervus canadensis", "genus": {"scientific_name": "Cervus"}},
    {"common_name": "Giant amoeba", "scientific_name": "Chaos carolinense", "genus": {"scientific_name": "Chaos"}},
    {"common_name": "Common Bottlenose Dolphin", "scientific_name": "Tursiops truncatus", "genus": {"scientific_name": "Tursiops"}},
    {"common_name": "Sea otter", "scientific_name": "Enhydra lutris", "genus": {"scientific_name": "Enhydra"}},
    {"common_name": "Wolf", "scientific_name": "Canis lupus", "genus": {"scientific_name": "Canis"}}
] 

session = dbconnect()

for species in species_list:
    addSpecies(session, species)


# Define a list of dicts of our specimens.
specimen_list = [
    {"name": "bongo", "species": {"scientific_name": "Felis nigripes"}, "birth_date_time": "1262304000"},
    {"name": "coco", "species": {"scientific_name": "Cervus canadensis"}, "birth_date_time": "1293840000"},
    {"name": "lola", "species": {"scientific_name": "Tursiops truncatus"}, "birth_date_time": "1325376000"},
    {"name": "shadow", "species": {"scientific_name": "Tursiops truncatus"}, "birth_date_time": "1356998400"},
    {"name": "stella", "species": {"scientific_name": "Enhydra lutris"}, "birth_date_time": "1420070400"}
]

for specimen in specimen_list:
    addSpecimen(session, specimen)