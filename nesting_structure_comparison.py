import re
def same_structure_as(original,other):      
    '''
        una forma de optimizar es agregar al patron que detecte números también,
        así, evitamos el proceso de las list comprehesion y nos brincariamos directamente a
        return a == b

    '''
    pattern = re.compile("[\'].*[\']")

    a = re.sub(pattern, '', str(original))
    b = re.sub(pattern, '', str(other))

    pattern = re.compile("[0-9]")
    
    return re.sub(pattern, '', a) == re.sub(pattern, '', b)