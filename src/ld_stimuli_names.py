
supported_languages = ['french', 'english']

picturesNamesEnglish = {
    'a001': 'penguin',
    'a002': 'pig',
    'a003': 'snake',
    'a004': 'squirrel',
    'a005': 'turtle',
    'a006': 'crocodile',
    'a007': 'bear',
    'a008': 'deer',
    'a009': 'dog',
    'a010': 'eagle',
    'a011': 'elephant',
    'a012': 'fish',
    'a013': 'rabbit',
    'a014': 'rhinoceros',
    'a015': 'sheep',
    'a016': 'chicken',

    'b001': 'pliers',
    'b002': 'power outlet',
    'b003': 'fridge',
    'b004': 'chair',
    'b005': 'rolling pin',
    'b006': 'salt',
    'b007': 'television',
    'b008': 'watering can',
    'b009': 'glass',
    'b010': 'hammer',
    'b011': 'key',
    'b012': 'lamp',
    'b013': 'saw',
    'b014': 'pan',
    'b015': 'screwdriver',
    'b016': 'spoon',
    
    'c001': 'pants',
    'c002': 'shoe',
    'c003': 'skirt',
    'c004': 'sock',
    'c005': 'pullover',
    'c006': 'tie',
    'c007': 'jacket',
    'c008': 'boot',
    'c009': 'dress',
    'c010': 'hat',
    'c011': 'coat',
    'c012': 'mitten',
    'c013': 'necklace',
    'c014': 'glove',
    'c015': 'button',
    'c016': 'purse'
}

picturesNamesFrench = {
    'a001': 'pingouin',
    'a002': 'cochon',
    'a003': 'serpent',
    'a004': 'écureuil',
    'a005': 'tortue',
    'a006': 'crocodile',
    'a007': 'ours',
    'a008': 'cerf',
    'a009': 'chien',
    'a010': 'aigle',
    'a011': 'éléphant',
    'a012': 'poisson',
    'a013': 'lapin',
    'a014': 'rhinocéros',
    'a015': 'mouton',
    'a016': 'coq',

    'b001': 'pinces',
    'b002': 'prise',
    'b003': 'réfrigérateur',
    'b004': 'chaise',
    'b005': 'rouleau',
    'b006': 'sel',
    'b007': 'télévision',
    'b008': 'arrosoir',
    'b009': 'verre',
    'b010': 'marteau',
    'b011': 'clé',
    'b012': 'lampe',
    'b013': 'scie',
    'b014': 'casserole',
    'b015': 'tournevis',
    'b016': 'cuillère',

    'c001': 'pantalon',
    'c002': 'chaussure',
    'c003': 'jupe',
    'c004': 'chaussette',  # bas?
    'c005': 'pull',
    'c006': 'cravate',
    'c007': 'veste',
    'c008': 'botte',
    'c009': 'robe',
    'c010': 'chapeau',
    'c011': 'manteau',
    'c012': 'moufle',  # mitaine?
    'c013': 'collier',
    'c014': 'gant',
    'c015': 'bouton',
    'c016': 'sac à main'
}

pictureNames = {'english': picturesNamesEnglish, 'french': picturesNamesFrench}
classNames = {'english': {'a': 'animals', 'b': 'household', 'c': 'clothes'},
              'french': {'a': 'animaux', 'b': 'maison', 'c': 'vêtements'},
              None: {'a': 'a', 'b': 'b', 'c': 'c'}}
soundNames = {
    None: {0: 'S1', 1: 'S2', 2: 'S3'},
    'english': {0: 'standard', 1: 'noise', 2: 'high pitch'},
    'french': {0: 'standard', 1: 'bruit', 2: 'aigu'}}

rest_screen_text = {'english': ' REST ', 'french': ' REPOS '}
ending_screen_text = {'english': ' THANK YOU ', 'french': ' MERCI '}
presentation_screen_text = {'english': ' PRESENTATION ', 'french': ' PRÉSENTATION '}
ttl_instructions_text = {'english': ' PLEASE INPUT TTL ', 'french': ' EN ATTENTE DU TTL '}
