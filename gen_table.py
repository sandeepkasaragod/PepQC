#Table like PD
#trans_table = ""
def create_table(peptide, charge, theo_spectra): 
    trans_table = ""
    dict_len = (len(theo_spectra))
    for i in range(len(peptide)):
        if dict_len == 6: # Charge 1
            trans_table = trans_table +  str(theo_spectra['b1-H2O'][i]) + '\t' + str(theo_spectra['b1-NH3'][i]) + '\t' + str(theo_spectra['b1'][i]) + '\t' + \
                          peptide[i] + '\t' + str(theo_spectra['y1'][i]) + '\t' + str(theo_spectra['y1-H2O'][i]) + '\t' + str(theo_spectra['y1-NH3'][i]) + '\n'
        elif dict_len == 8: #charge 2
            trans_table = trans_table + str(theo_spectra['b1-H2O'][i]) + '\t' + str(theo_spectra['b1-NH3'][i]) + '\t' + str(theo_spectra['b2'][i]) + '\t' + \
                          str(theo_spectra['b1'][i]) + '\t' + peptide[i] + '\t' + str(theo_spectra['y1'][i]) + '\t' + str(theo_spectra['y2'][i]) + \
                          '\t' + str(theo_spectra['y1-NH3'][i]) + '\t' + str(theo_spectra['y1-H2O'][i]) + '\n'
        elif dict_len == 10: #charge 3
            trans_table = trans_table + str(theo_spectra['b1-H2O'][i]) + '\t' + str(theo_spectra['b1-NH3'][i]) + '\t' + str(theo_spectra['b3'][i]) + '\t' + \
                          str(theo_spectra['b2'][i]) + '\t' + str(theo_spectra['b1'][i]) + '\t' + peptide[i] + '\t' + str(theo_spectra['y1'][i]) + \
                          '\t' + str(dicts_theo['y2'][i]) + '\t' + str(dicts_theo['y3'][i]) +  '\t' + str(theo_spectra['y1-NH3'][i]) + '\t' + \
                          str(theo_spectra['y1-H2O'][i]) + '\n'            
        elif dict_len == 12: #charge 4
            trans_table = trans_table + str(theo_spectra['b1-H2O'][i]) + '\t' + str(theo_spectra['b1-NH3'][i]) + '\t' + str(theo_spectra['b4'][i]) + '\t' + \
                          str(theo_spectra['b3'][i]) + '\t' + str(theo_spectra['b2'][i]) + '\t' + str(theo_spectra['b1'][i]) + '\t' + \
                          peptide[i] + '\t' + str(theo_spectra['y1'][i]) + '\t' + str(theo_spectra['y2'][i]) + '\t' + str(theo_spectra['y3'][i]) + \
                          '\t' + str(theo_spectra['y4'][i])+ '\t' + str(theo_spectra['y1-NH3'][i]) + '\t' + str(theo_spectra['y1-H2O'][i]) + '\n'
        elif dict_len == 14: #charge 5
            trans_table = trans_table + str(theo_spectra['b1-H2O'][i]) + '\t' + str(theo_spectra['b1-NH3'][i]) + '\t' + str(theo_spectra['b5'][i]) + '\t' + \
                          str(theo_spectra['b4'][i]) + '\t' + str(theo_spectra['b3'][i]) + '\t' + str(theo_spectra['b2'][i]) + '\t' \
                          + str(theo_spectra['b1'][i]) + '\t'  + peptide[i] + '\t' + str(theo_spectra['y1'][i]) + '\t' + str(theo_spectra['y2'][i]) + \
                          '\t' + str(theo_spectra['y3'][i]) + '\t' + str(theo_spectra['y4'][i]) + '\t' + str(theo_spectra['y5'][i]) + \
                          '\t' + str(theo_spectra['y1-NH3'][i]) + '\t' + str(theo_spectra['y1-H2O'][i]) + '\n'
        elif dict_len == 16: #charge 6
            trans_table = trans_table + str(theo_spectra['b1-H2O'][i]) + '\t' + str(theo_spectra['b1-NH3'][i]) + '\t' + str(theo_spectra['b6'][i]) + '\t' + \
                          str(theo_spectra['b5'][i]) + '\t' + str(theo_spectra['b4'][i]) + '\t' + str(theo_spectra['b3'][i]) + '\t' + str(theo_spectra['b2'][i]) +  \
                          '\t' + str(theo_spectra['b1'][i]) + '\t'  + peptide[i] + '\t' + str(theo_spectra['y1'][i]) + '\t' + str(theo_spectra['y2'][i]) + \
                          '\t' + str(theo_spectra['y3'][i]) + '\t' + str(theo_spectra['y4'][i]) + '\t' + str(theo_spectra['y5'][i])  + '\t' + \
                          str(theo_spectra['y6'][i]) + '\t' + str(theo_spectra['y1-NH3'][i]) + '\t' + str(theo_spectra['y1-H2O'][i]) + '\n'            
        elif dict_len == 18: #charge 7
            trans_table = trans_table + str(theo_spectra['b1-H2O'][i]) + '\t' + str(theo_spectra['b1-NH3'][i]) + '\t' + str(dicts_theo['b7'][i]) + '\t' \
                          + str(dicts_theo['b6'][i]) + '\t' + str(dicts_theo['b5'][i]) + '\t' + str(dicts_theo['b4'][i]) + '\t' \
                          + str(dicts_theo['b3'][i]) + '\t' + str(dicts_theo['b2'][i]) + '\t' + str(dicts_theo['b1'][i]) + '\t'  + peptide[i] + '\t' \
                          + str(dicts_theo['y1'][i]) + '\t' + str(dicts_theo['y2'][i]) + '\t' + str(dicts_theo['y3'][i]) + '\t' + str(dicts_theo['y4'][i]) \
                          + '\t' + str(dicts_theo['y5'][i])  + '\t' + str(dicts_theo['y6'][i]) + '\t' + str(dicts_theo['y7'][i]) + '\t' + str(theo_spectra['y1-NH3'][i]) \
                          + '\t' + str(theo_spectra['y1-H2O'][i]) + + '\n'
        elif dict_len == 20: #charge 8
            trans_table = trans_table + str(theo_spectra['b1-H2O'][i]) + '\t' + str(theo_spectra['b1-NH3'][i]) + '\t' + str(dicts_theo['b8'][i]) + '\t' + \
                          str(dicts_theo['b7'][i]) + '\t' + str(dicts_theo['b6'][i]) + '\t' + str(dicts_theo['b5'][i]) + '\t' \
                          + str(dicts_theo['b4'][i]) + '\t' + str(dicts_theo['b3'][i]) + '\t' + str(dicts_theo['b2'][i]) + '\t' + \
                          str(dicts_theo['b1'][i]) + '\t'  + peptide[i] + '\t' + str(dicts_theo['y1'][i]) + '\t' + str(dicts_theo['y2'][i]) \
                          + '\t' + str(dicts_theo['y3'][i]) + '\t' + str(dicts_theo['y4'][i]) + '\t' + str(dicts_theo['y5'][i])  + '\t' + \
                          str(dicts_theo['y6'][i]) + '\t' + str(dicts_theo['y7'][i]) + '\t' + str(dicts_theo['y8'][i]) + '\t' + str(theo_spectra['y1-NH3'][i]) \
                          + '\t' + str(theo_spectra['y1-H2O'][i])+ '\n'
        elif dict_len == 22: #charge 9
            trans_table = trans_table + str(theo_spectra['b1-H2O'][i]) + '\t' + str(theo_spectra['b1-NH3'][i]) + '\t' + str(theo_spectra['b9'][i]) + \
                          '\t' + str(theo_spectra['b8'][i]) + '\t' + str(theo_spectra['b7'][i]) + '\t' + str(theo_spectra['b6'][i]) + '\t' \
                          + str(theo_spectra['b5'][i]) + '\t' + str(theo_spectra['b4'][i]) + '\t' + str(theo_spectra['b3'][i]) + '\t' +\
                          str(theo_spectra['b2'][i]) + '\t' + str(theo_spectra['b1'][i]) +'\t'  + peptide[i] + '\t' + str(theo_spectra['y1'][i]) + \
                          '\t' + str(dicts_theo['y2'][i]) + '\t' + str(theo_spectra['y3'][i]) + '\t' + str(theo_spectra['y4'][i]) + '\t' + \
                          str(theo_spectra['y5'][i])  + '\t' + str(theo_spectra['y6'][i]) + '\t' + str(theo_spectra['y7'][i]) + '\t' + \
                          str(theo_spectra['y8'][i]) + '\t' + str(theo_spectra['y9'][i]) + '\t' + str(theo_spectra['y1-NH3'][i]) + '\t' + \
                          str(theo_spectra['y1-H2O'][i])+ '\n'
        elif dict_len == 24: #charge 10
            trans_table = trans_table + str(theo_spectra['b1-H2O'][i]) + '\t' + str(theo_spectra['b1-NH3'][i]) + '\t' + str(theo_spectra['b10'][i]) + \
                          '\t' + str(theo_spectra['b9'][i]) + '\t' + str(theo_spectra['b8'][i]) + '\t' + str(theo_spectra['b7'][i]) + '\t' \
                          + str(theo_spectra['b6'][i]) + '\t' + str(theo_spectra['b5'][i]) + '\t' + str(theo_spectra['b4'][i]) + '\t' + \
                          str(theo_spectra['b3'][i]) + '\t' + str(theo_spectra['b2'][i]) + '\t' + str(theo_spectra['b1'][i]) +'\t' \
                          + peptide[i] + '\t' + str(theo_spectra['y1'][i]) + '\t' + str(theo_spectra['y2'][i]) + '\t' + str(theo_spectra['y3'][i]) \
                          + '\t' + str(theo_spectra['y4'][i]) + '\t' + str(theo_spectra['y5'][i])  + '\t' + str(theo_spectra['y6'][i]) + \
                          '\t' + str(theo_spectra['y7'][i]) + '\t' + str(theo_spectra['y8'][i]) + '\t' + str(theo_spectra['y9'][i]) + '\t' \
                          + str(theo_spectra['y10'][i]) + '\t' + str(theo_spectra['y1-NH3'][i]) + '\t' + str(theo_spectra['y1-H2O'][i]) + '\n'
    
    return trans_table
