import arcpy
import os

os.mkdir("Temp")

ws = os.path.dirname(os.path.realpath(__file__))
mxd = arcpy.mapping.MapDocument('MappingEx.mxd')
df = arcpy.mapping.ListDataFrames(mxd)


for dataframe in df:
    filePath = os.path.join(ws + "\\Temp\\" + str(dataframe.name) + ".pdf")
    pdf = arcpy.mapping.ExportToPDF(mxd, filePath)


pdfPath = os.path.join(ws + "\\Temp\\AllMaps.pdf")
pdfDoc = arcpy.mapping.PDFDocumentCreate(pdfPath)


for dataframe in df:
    fileappend = os.path.join(ws + "\\Temp\\" + str(dataframe.name) + ".pdf")
    pdfDoc.appendPages(fileappend)


del mxd
