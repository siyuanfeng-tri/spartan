filename = _argv[1]

meshes, actors = ioUtils.readObjMtl(filename)

for m, a in zip(meshes, actors):

    color = a.GetProperty().GetColor()
    opacity = a.GetProperty().GetOpacity()

    obj = vis.showPolyData(m, 'mesh', color=color)
    obj.setProperty('Alpha', opacity)
    obj.actor.SetTexture(a.GetTexture())
