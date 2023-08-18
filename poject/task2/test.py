import numpy as np 
from dicompylercore import dicomparser, dvh, dvhcalc
from matplotlib import pyplot as plt 
import matplotlib.cm as cm
import seaborn as sns


dp = dicomparser.DicomParser("../../data/CT/DicomDaten/Dose.dcm")

#dvh = dvh.DVH.from_dicom_dvh(dp, 0)

structures = dp.GetStructures()
print(structures)