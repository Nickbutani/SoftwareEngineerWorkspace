def extract_full_names(people):
    full_names = [person['first'] + ' ' + person['last'] for person in people]
    
    return full_names