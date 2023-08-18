import numpy as np 
from dicompylercore import dicomparser, dvh, dvhcalc
from matplotlib import pyplot as plt 
import matplotlib.cm as cm
import seaborn as sns

CT = dicomparser.DicomParser("CT_RTSTRUCT_RTDOSE_Woche12/CT1.2.826.0.1.3680043.9.7275.1.10283212537801390882772228330690033.dcm")
RD = dicomparser.DicomParser("CT_RTSTRUCT_RTDOSE_Woche12/RD1.2.752.243.1.1.20200806103223959.1000.31013.dcm")
RS = dicomparser.DicomParser("CT_RTSTRUCT_RTDOSE_Woche12/RS1.2.752.243.1.1.20210720131129727.2000.87564.dcm")


#Printing patients name
print(RD.ds[0x0010,0x0010])

#printing image position 
print("CT: \n", CT.ds[0x0020,0x0032], "\n RS: \n", RD.ds[0x0020,0x0032])

CT_image  = CT.GetImage()
plt.imshow(CT_image, cmap = 'gray')
plt.savefig("CT.png")
plt.close()

#wanted z cut = 25.7
dose_plot = sns.heatmap(RD.GetDoseGrid(25.7))
#dose_plot.set(xticklabels=[])
#dose_plot.set(yticklabels=[])
#dose_plot.tick_params(bottom=False)
#dose_plot.tick_params(left =False)

plt.savefig("Dose.png")
plt.close()

#Look for structures in RS
structures = RS.GetStructures()
#print(structures) # ---> found Roi at 28, i.e. CTV 5580

ROIcoords = RS.GetStructureCoordinates(28)
ROI_datapoints = np.array(ROIcoords['25.70'][0]['data'])

idk = sns.heatmap(CT.ds.pixel_array*CT.ds.RescaleSlope+CT.ds.RescaleIntercept,  cmap = 'gray')
plt.savefig("3e.png")
plt.close()

RDthing = sns.heatmap(RD.GetDoseGrid(25.70)*RD.ds.DoseGridScaling)
plt.savefig("3f.png")
plt.close()