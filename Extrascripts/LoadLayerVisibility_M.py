import arcpy

mxd = arcpy.mapping.MapDocument('CURRENT')
dframes = arcpy.mapping.ListDataFrames(mxd)

intext = open("LayerVisibility.txt", "r")

mylist = []
for i in intext.readlines():
    h = i.split('\t')  # split line by tab character
    h = [x.strip() for x in h] #strip white space from all elements in list
    mylist.append(h) # append to new list
intext.close()

for dframe in dframes:
    for layer in arcpy.mapping.ListLayers(dframe):
        for item in mylist:
            if dframe.name == item[0]:
                if layer.name == item[1]:
                    print 'Changing {}-{}-{} to {}-{}-{}'.format(dframe.name, layer.name, layer.visible, item[0], item[1], item[2])
                    layer.visible = item[2]

mxd.save()

arcpy.RefreshTOC()
arcpy.RefreshActiveView()

del mxd
