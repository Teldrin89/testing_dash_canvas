import vtk


def main():
    colors = vtk.vtkNamedColors()

    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetCenter(0.0, 0.0, 0.0)
    sphereSource.SetRadius(5)

    # Read poly data from vtp file
    reader = vtk.vtkXMLPolyDataReader()
    reader.SetFileName("data/diskout.vtp")
    reader.Update()
    poly_data = reader.GetOutput()
    print("check for poly data read")
    print(type(poly_data))

    # Trial setting a 3D mesh for loaded poly data using Delaunay method
    dela = vtk.vtkDelaunay3D()
    print("vtkDelaunay3D variable set")
    dela.SetInputData(poly_data)
    print("input data set")
    # dela.SetTolerance(1)
    print("tolerance set")
    mapMesh = vtk.vtkPolyDataMapper()
    print("vtk poly data mapper set for mesh")
    mapMesh.SetInputConnection(dela.GetOutputPort())
    print("mapper input data set with mesh - through output port")
    meshActor = vtk.vtkActor()
    print("mesh actor set")
    meshActor.SetMapper(mapMesh)
    print("mesh actor set with mesh mapper")
    meshActor.GetProperty().SetColor(colors.GetColor3d('MidnightBlue'))
    print("mesh actor set with blue color")
    # Trial for volume calculation using the mass poroperties
    # mass = vtk.vtkMassProperties()
    # mass.SetInputData(dela)
    # volume = mass.GetVolume()
    # print("show the volume of model")
    # print(volume)
    # print()



    # Create a mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    # mapper.SetInputConnection(sphereSource.GetOutputPort())
    # Changed mapper to read data from loaded vtp file
    mapper.SetInputData(poly_data)
    actor = vtk.vtkActor()
    # Set different mapper - the one with mesh - for rendering
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Bisque'))

    # Setup a renderer, render window, and interactor
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    # renderWindow.SetWindowName("Test")

    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the scene
    renderer.AddActor(actor)
    # Add the actor of mesh to the scene
    print("before addition of mesh actor - checking it")
    print(type(meshActor))
    print("for reference check the std actor")
    print(type(actor))
    print()
    # renderer.AddActor(meshActor)
    renderer.SetBackground(colors.GetColor3d('Black'))

    # Render and interact
    renderWindow.Render()
    # *** SetWindowName after renderWindow.Render() is called ***
    renderWindow.SetWindowName("Test")
    renderWindowInteractor.Start()