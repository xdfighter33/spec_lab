import numpy as np
import matplotlib.pyplot as pl
import pandas as pd

#I dont know what unit the measurement was in, so I made an educated guess and thought TRZ due to how similar they look



data = np.loadtxt('smoothed_gotham.txt')
mole_data = pd.read_csv('mole_data.csv')



#found molecule el(K)
finding_file1 = data[:,0]


#found molecule (TRZ??)
finding_file2 = data[:,1]

#Hacky fix :(

mole_data["TMZ"] = mole_data["TMZ"].apply(lambda x: ''.join(filter(str.isdigit, str(x))))

# Molecules wavelength
molecule_TRZ = pd.to_numeric(mole_data["TMZ"], errors='coerce')

# Molecules luminosity??
molecule_ELK = pd.to_numeric(mole_data["EL(K)"], errors='coerce')



match_count = 0
matched_molecules = []


#VERY HACCKY FIX 
min_length = min(len(molecule_TRZ), len(molecule_ELK))

print("lengtrh of the array", len(finding_file1))
#Loop through each itieration and check if there is a match
for i in range(min_length):
    if np.isclose(finding_file1[i], molecule_TRZ[i], rtol=1e-10) and \
       np.isclose(finding_file2[i], molecule_ELK[i], rtol=1e-10):
        
        match_count += 1
        matched_molecules.append(mole_data["Species"][i])
#Priting out matches then checking the rest 
print("Number of matches:", match_count)


#now check for matches

if match_count > 0:
    print("Matched molecules:")
    for molecule in matched_molecules:
        print(molecule)
else:
    print("No matches found.")


