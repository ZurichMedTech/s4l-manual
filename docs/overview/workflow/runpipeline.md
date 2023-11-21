
## Running a Pipeline


### Running Computational Pipeline
   For your custom models and basic computations, running a project is straightforward. Once you have your pipeline connected, click the *Run* button at the bottom right-hand side of the screen. Please note that this will not run code that is written inside JupyterLab Services. Running a pipeline will execute only "computational" Services.

   The *Run* Button is located at the top left corner of your Pipeline Workspace, highlighted with blue in this image (refer to :numref:`s4l_web_run0`).

   To see run progress logs, you may change the Workspace View to the *Logger* tab, by clicking the third button on the Workbench Views menu at the top of the Pipeline Workspace (refer to :numref:`s4l_web_run1`).

FIGURE

    The *Run* button.


FIGURE

    The Progress logs.

   Interactive Services (such as JupyterLabs and viewer Services) will be unaffected by the *Run* and *Stop* buttons. This is because there is no default execution of these services. Computational Services, on the other hand, simply run their execution tasks with the user-defined input parameters.

### Interactive Services
   JupyterLab Services will allow you to write and execute code within the JupyterLab GUI, but as with all Interactive Services, will not run automatically when a project pipeline is launched. To work with an interactive Service, you may double-click on it to access the *Interactive* View.

FIGURE

    Interactive services available to run a pipeline.
