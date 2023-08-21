import numpy as np 
#from dicompylercore import dicomparser, dvh, dvhcalc
from matplotlib import pyplot as plt 
import matplotlib.cm as cm
import seaborn as sns
import pydicom
import pandas as pd

dcm_data = pydicom.dcmread('../../DoseCTV.dcm')
#df  = pd.read_csv("../../DoseCTV.csv", header = None)

scaling_factor = 100.0  # Modify this as needed

print("Dose Scaling: ", dcm_data.DoseGridScaling)
print(np.max(dcm_data.pixel_array[:]))

# Scale the pixel values
#dcm_data.pixel_array[:] = dcm_data.pixel_array * scaling_factor

# Adjust the DoseGridScaling value
dcm_data.DoseGridScaling = dcm_data.DoseGridScaling *1000000

print("Dose Scaling: ", dcm_data.DoseGridScaling)

# add new tag
dcm_data.add_new((0x3004, 0x0002), 'CS', 'GY')

# Save the modified DICOM to a new file
dcm_data.save_as('../../data/CT/DicomDaten/Dose.dcm')


