
## Running a Pipeline


### Running Computational Pipeline
   For your custom models and basic computations, running a project is straightforward. Once you have your pipeline connected, click the *Run* button at the bottom right-hand side of the screen. Please note that this will not run code that is written inside JupyterLab Services. Running a pipeline will execute only "computational" Services.

   The *Run* Button is located at the top left corner of your Pipeline Workspace, highlighted with blue in the figure below.

   To see run progress logs, you may change the Workspace View to the *Logger* tab, by clicking the third button on the Workbench Views menu at the top of the Pipeline Workspace.

<p align="center">
  <img width="80%" src="assets/workflow/runpipeline0.png">
</p>

<p style="text-align: center;"> Run button.</p>



<p align="center">
  <img width="80%" src="assets/workflow/runpipeline1.png">
</p>

<p style="text-align: center;">The Progress logs.</p>

    

   Interactive Services (such as JupyterLabs and viewer Services) will be unaffected by the *Run* and *Stop* buttons. This is because there is no default execution of these services. Computational Services, on the other hand, simply run their execution tasks with the user-defined input parameters.

### Interactive Services
   JupyterLab Services will allow you to write and execute code within the JupyterLab GUI, but as with all Interactive Services, will not run automatically when a project pipeline is launched. To work with an interactive Service, you may double-click on it to access the *Interactive* View.

<p align="center">
  <img width="80%" src="assets/workflow/runpipeline2.png">
</p>

<p style="text-align: center;"> Interactive services available to run a pipeline.</p>

### Activity Center
The Activity Center, always available in the top navigation bar, shows you everything currently running across all your Projects. 

<p align="center">
  <img width="100%" src="assets/workflow/activity_log.gif">
</p>



