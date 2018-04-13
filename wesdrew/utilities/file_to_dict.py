##################################################################################
# To populate a template with a dictionary as context, scan a file               #
# with the format '{keyword}{separator}{value}\n' and package it as a dictionary #
#                                                                                #
#     @arg separator: char used to seperate keyword and value                    #
#     @file: file containing key-value pairs                                     #
##################################################################################

KEY=0
VALUE=1


def file_to_dict(separator, file):
    """
    Open file for reading. Scan by line, ignoring any line starting with 
    a comment('#'). Then, separate by the line with the separator (duh)
    and store it in the dictionary. Overwrite key-value pair if key appears
    in file more than once.
    """
    d = {}
    f = open(file, 'r')
    for line in f:
        if line.startswith('#'):
            pass
        kv_pair = line.split(separator)
        d[kv_pair[KEY].lstrip().rstrip()] = kv_pair[VALUE].lstrip().rstrip()
    f.close()
    return d
