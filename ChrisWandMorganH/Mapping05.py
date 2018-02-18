import arcpy

mxd= arcpy.mapping.MapDocument("CURRENT")

df=arcpy.mapping.ListDataFrames(mxd,"Canada")[0]
addLayer1= arcpy.mapping.Layer(r"H:\GIS4207_ArcCustom\Data\World\Continents.lyr")
addlayer2= arcpy.mapping.Layer(r"H:\GIS4207_ArcCustom\Data\World\World Cities.lyr")
arcpy.mapping.AddLayer(df,addLayer1,"AUTO_ARRANGE")
arcpy.mapping.AddLayer(df,addlayer2,"AUTO_ARRANGE")

del df, mxd
arcpy.RefreshActiveView()
arcpy.RefreshTOC()