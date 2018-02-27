import arcpy
import os

if os.path.exists("../mxdTemp/MappingEx.mxd"):
    os.remove("../mxdTemp/MappingEx.mxd")
if os.path.exists("../mxdTemp"):
    os.rmdir("../mxdTemp")


os.mkdir("../mxdTemp")

ws = os.path.dirname(os.path.realpath(__file__))

arcpy.env.workspace = ws

mxdList = arcpy.ListFiles("*.mxd")

for filename in mxdList:
    filePath = os.path.join(ws, filename)
    mxd = arcpy.mapping.MapDocument(filePath)
    mxd.relativePaths = True

    copyPath = os.path.join("../mxdTemp", filename)
    mxd.saveACopy(copyPath)
    print filePath

    del mxd
