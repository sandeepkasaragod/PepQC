from pyteomics import mgf, pepxml, mass
import gen_label as gl
import re
dicts_mod_pos = {}

def fragments(peptide, types=('b', 'y'), maxcharge=1):
    """
    The function generates all possible m/z for fragments of types
    `types` and of charges from 1 to `maxharge`.
    """
    for i in range(1, len(peptide)):
        for ion_type in types:
            for charge in range(1, maxcharge+1):
                if ion_type[0] in 'abc':
                    yield mass.fast_mass(
                            peptide[:i], ion_type=ion_type, charge=charge)
                else:
                    yield mass.fast_mass(peptide[i:], ion_type=ion_type, charge=charge)

def get_theo_spectra_no_mod(peptide, charge):
    a = fragments(peptide, ('b', 'y'), charge)
    ls = [x for x in a] # Adding the fragments to list
    keys = gl.generate_label(charge)  #genares the list like ['b1', 'y1', 'b2' ...................]
    keys_count = len(keys)
    a = {keys[index]: ls[index:len(ls):keys_count] for index in range(0,keys_count)}
    a['b1-NH3'] = [float(x)-17.02655 for x in a['b1']]
    a['y1-NH3'] = [float(x)-17.02655 for x in a['y1']]
    
    a['b1-H2O'] = [float(x)-18.01057 for x in a['b1']]
    a['y1-H2O'] = [float(x)-18.01057 for x in a['y1']]
    return a

def get_theo_spectra_with_mod(peptide, charge, ptm_mods, modification_list):
    a = fragments(peptide, ('b', 'y'), charge)
    ls = [x for x in a] # Adding the fragments to list
    keys = gl.generate_label(charge)  #genares the list like ['b1', 'y1', 'b2' ...................]
    keys_count = len(keys)
    a = {keys[index]: ls[index:len(ls):keys_count] for index in range(0,keys_count)}
    a['b1-NH3'] = [float(x)-17.02655 for x in a['b1']]
    a['y1-NH3'] = [float(x)-17.02655 for x in a['y1']]

    a['b1-H2O'] = [float(x)-18.01057 for x in a['b1']]
    a['y1-H2O'] = [float(x)-18.01057 for x in a['y1']]

    mod_pos = {}
    mod_pos_rev = {}
    if re.search('\((.*?)\)', ptm_mods):
        for string in ptm_mods.split(';'):
            if re.search('\((.*?)\)', string).group(1).strip() in modification_list:
                # storing actual modification location -1 to match the list items of dictioanry keys
                mod_pos[int(re.search('\d+', string).group(0).strip()) - 1] = [float(modification_list[re.search('\((.*?)\)', string).group(1)])] # for b ions
                mod_pos_rev[(len(peptide)-1) - (int(re.search('\d+', string).group(0).strip()) - 1)] = [float(modification_list[re.search('\((.*?)\)', string).group(1)])] #for y ions
    
    #return mod_pos, mod_pos_rev
    for m, n in a.items():
        num = re.search("\d+", m)
        #print (num[0], m)
        a = 0.0
        if 'b' in m:
            for i in range(len(n)):
                if i not in mod_pos:
                    if m not in dicts_mod_pos:
                        dicts_mod_pos[m] = [n[i] + float(a)]
                    else:
                        dicts_mod_pos[m].append(n[i] + float(a))
                else:
                    if num > 1:
                        dicts_mod_pos[m].append(n[i] + (mod_pos[i][0] / num) + float(a))
                        a+=(mod_pos[i][0]/ num)
                    else:
                        dicts_mod_pos[m].append(n[i] + mod_pos[i][0] + float(a)) 
                        a+=mod_pos[i][0]
        
        if 'y' in m:
            n_rev = [x for x in n[::-1]]
            for i in range(len(n_rev)):
                if i not in mod_pos_rev:
                    if m not in dicts_mod_pos:
                        dicts_mod_pos[m] = [n_rev[i] + float(a)]
                    else:        
                        dicts_mod_pos[m].append(n_rev[i] + float(a))
                else:
                    if num > 1:
                        dicts_mod_pos[m].append(n_rev[i] + (mod_pos_rev[i][0] / num) + float(a))
                        a+=(mod_pos_rev[i][0]/num)
                    else:
                        dicts_mod_pos[m].append(n_rev[i] + mod_pos_rev[i][0] + float(a))                        
                        a+=mod_pos_rev[i][0]
    return dicts_mod_pos
