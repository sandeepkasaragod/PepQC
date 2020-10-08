def label_to_index(charge):
    ''' conver the labels to value for plot the table '''
    dict_label_idx = {}
    if charge == 1:
        dict_label_idx = {'b1-H2O':0, 'b1-NH3':1, 'b1':2, 'y1':4, 'y1-NH3':5, 'y1-H2O':6}
    elif charge == 2: 
        dict_label_idx = {'b1-H2O':0, 'b1-NH3':1, 'b2':2, 'b1':3, 'y1':5, 'y2':6, 'y1-NH3':7, 'y1-H2O':8}
    elif charge == 3: 
        dict_label_idx = {'b1-H2O':0, 'b1-NH3':1, 'b3':2, 'b2':3, 'b1':4, 'y1':6, 'y2':7, 'y3':8, 'y1-NH3':9, 'y1-H2O':10}
    elif charge == 4: 
        dict_label_idx = {'b1-H2O':0, 'b1-NH3':1, 'b4':2, 'b3':3, 'b2':4, 'b1':5, 'y1':7, 'y2':8, 'y3':9, 'y4':10, 'y1-NH3':11, 'y1-H2O':12}
    elif charge == 5: 
        dict_label_idx = {'b1-H2O':0, 'b1-NH3':1, 'b5':2, 'b4':3, 'b3':4, 'b2':5, 'b1':6, 'y1':8, 'y2':9, 'y3':10, 'y4':11, 'y5':12, 'y1-NH3':13, 'y1-H2O':14}
    elif charge == 6: 
        dict_label_idx = {'b1-H2O':0, 'b1-NH3':1, 'b6':2, 'b5':3, 'b4':4, 'b3':5, 'b2':6, 'b1':7, 'y1':9, 'y2':10, 'y3':11, 'y4':12, 'y5':13, 'y6':14, 'y1-NH3':15, \
                          'y1-H2O':16}
    elif charge == 7: 
        dict_label_idx = {'b1-H2O':0, 'b1-NH3':1, 'b7':2, 'b6':3, 'b5':4, 'b4':5, 'b3':6, 'b2':7, 'b1':8, 'y1':10, 'y2':11, 'y3':12, 'y4':13, 'y5':14, 'y6':15, \
                          'y7':16, 'y1-NH3':17, 'y1-H2O':18}
    elif charge == 8: 
        dict_label_idx = {'b1-H2O':0, 'b1-NH3':1, 'b8':2, 'b7':3, 'b6':4, 'b5':5, 'b4':6, 'b3':7, 'b2':8, 'b1':9, 'y1':11, 'y2':12, 'y3':13, 'y4':14, 'y5':15, 'y6':16, \
                          'y7':17, 'y8':18, 'y1-NH3':19, 'y1-H2O':20}
    elif charge == 9: 
        dict_label_idx = {'b1-H2O':0, 'b1-NH3':1, 'b9':2, 'b8':3, 'b7':4, 'b6':5, 'b5':6, 'b4':7, 'b3':8, 'b2':9, 'b1':10, 'y1':12, 'y2':13, 'y3':14, 'y4':15, 'y5':16, \
                          'y6':17, 'y7':18, 'y8':19, 'y9':20, 'y1-NH3':21, 'y1-H2O':22}
    elif charge == 10: 
        dict_label_idx = {'b1-H2O':0, 'b1-NH3':1, 'b10':2, 'b9':3, 'b8':4, 'b7':5, 'b6':6, 'b5':7, 'b4':8, 'b3':9, 'b2':10, 'b1':11, 'y1':13, 'y2':14, 'y3':15, 'y4':16, \
                          'y5':17, 'y6':18, 'y7':19, 'y8':20, 'y9':21, 'y1-NH3':22, 'y1-H2O':23}
    return dict_label_idx
