## Apps

Every Project is composed of one or more ```Apps```. Apps are building blocks for projects and can provide data/files, visualize results (2D, 3D), implement code in Jupyter notebooks or perform computations to execute simulations within a project. The computational backend involves all apps needed to handle the actual computational workload. A computational workflow is described as a pipeline that sequentially processes a stream of data. Every pipeline consists of multiple algorithms, each one expecting specific input data and providing specific output data.

All these apps can be already provided within a project or can be set up from scratch by the user by selecting options in the App catalog.


<p align="center">
  <img width="80%" src="assets/dashboard/serviceworkbench.png">
</p>

<p style="text-align: center;">Connected Apps as well as selection of Apps via the App Catalog in the Workbench.</p>

   

### App Types

 * **Computational**: Computational Apps such as a ```Python Runner``` will allow the setting of some parameters (e.g., input files) and will perform a computation with no user interaction required. Interactive Apps only perform tasks with user interaction, as is the case for apps such as the ```JupyterLab```. JupyterLab apps will allow you to write and execute code within the JupyterLab GUI, but as with all interactive apps, will not run automatically when a project pipeline is launched. Computational Apps, on the other hand, will automatically read all input parameters at runtime and execute the static code embedded inside them.
 * **Interactive:** In terms of viewing, Interactive Apps will have a special view in the Workbench through the Interactive View tab. You may occasionally want to maximize this view to have a larger working area. To do this, you can click on the maximize button in the upper right-hand corner of the Interactive View.

<p align="center">
  <img width="60%" src="assets/dashboard/servicerestore.png">
</p>

<p style="text-align: center;">Restore button to get into the Interactive Mode.</p>

   

<p align="center">
  <img width="60%" src="assets/dashboard/servicemaximize.png">
</p>

<p style="text-align: center;">Maximize button in the Interactive Mode.</p>

   

This section functions very similarly in the ```TUTORIALS``` tab. To add apps to an existing project, you may access the ```App Catalog``` directly within a project workspace without going through the ```APPS``` tab.
