
## Projects Tab

Each card listed in the ```PROJECTS``` tab represents a simulation project that belongs to you or is shared with you. The user needs to click on the card and then click the ```Open``` button on the project details window to open the project. 

### Project Details

When you click on a project an overview page will be shown. This page shows more details on the project (e.g., the project description, creation date, etc...) and allows you to perform actions (e.g., opening it, sharing, etc...). Depending on the access rights, you will able to modify the Project details (e.g., description and thumbnail, add tags, etc.), by using the pencil icons.

In addition, by clicking on the left-most icons, you will able to perform more operations on the project.

<p align="center">
  <img width="80%" src="assets/dashboard/StudyDetails.png">
</p>

<p style="text-align: center;">The Project Details.</p>


### Project Workbench
  
After you open a project, click the ```Restore``` button at the right corner to open the *Interactive* view of the project workbench. You can select *Workbench* to create and edit your flow chart, see your *Services*, debug and run your project .

<p align="center">
  <img width="80%" src="assets/dashboard/StudyWorkbench.png">
</p>

<p style="text-align: center;">The Project Workbench.</p>
   

(1) Primary Column
 - In the Nodes list tab, you can see the list of Services that are included in the project and rename or delete them. To delete a Service, select the Service and then click the Delete button on the menu bar. You can also rename a Service by selecting a Service and clicking the rename button on the menu bar.
 - In the Storage tab, you can browse all the data from any project you have created.

(2) Secondary Column
 - When no Service is selected, this tab will show the Project metadata.
 - When a Service is selected as in the case of the image above, the inputs and output parameters of that service will be shown in separate tabs.

(3) Workbench Views
 - **Pipeline:** This is the default view of the pipeline, showing Services and their connections
 - **Interactive:** When an Interactive Service is selected in the pipeline view or in the primary column, this tab will show the GUI for the Interactive Service
 - **Logger:** This tab will display all messages pertinent to the running of your project. These messages can be filtered by keywords/keyphrases entered into the *Filter* field.

(4) Run/Stop: For pipelines containing Computational Services, the Run button is used to execute the pipeline while the Stop button can abort a running pipeline.

(5) Pipeline Workspace: When viewing the Pipeline tab, this is where you can create and edit the Project by adding new services, deleting services, and linking them together.

(6) Service: Each Service is visible in the Pipeline workspace as a box with a name, input port, and/or an output port.

(7) Dashboard: When you have finished working on your Project, click on the ```Dashboard``` button to go back to your Dashboard. While doing so, any changes you made to your project will be saved.

