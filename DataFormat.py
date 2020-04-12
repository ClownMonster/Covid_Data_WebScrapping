'''
    Foramts the sent Data in the desired format and send  it the array format

'''


def dataformat(un_formated_data):
    my_list = str(un_formated_data)
    data_in_format = ''

    for i in my_list:
        if i == '\n':
            data_in_format = data_in_format + ' '
            continue
        else:
            data_in_format = data_in_format + i

    formated_data = data_in_format.split(' ')
    del formated_data[-1]
    del formated_data[0]
    del formated_data[-1]
    del formated_data[-1]
    return formated_data