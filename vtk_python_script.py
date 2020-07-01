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


    # Create a mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    # mapper.SetInputConnection(sphereSource.GetOutputPort())
    # Changed mapper to read data from loaded vtp file
    mapper.SetInputData(poly_data)
    actor = vtk.vtkActor()
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
    renderer.SetBackground(colors.GetColor3d('Black'))

    # Render and interact
    renderWindow.Render()
    # *** SetWindowName after renderWindow.Render() is called ***
    renderWindow.SetWindowName("Test")
    renderWindowInteractor.Start()