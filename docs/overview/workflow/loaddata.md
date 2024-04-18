## Loading Data

To create any model or data processing pipeline, you will often need to load your data. For now, this will only be done with the *File Picker Service*. Files can be added either from your local computer, an existing project, or from a file hosted publicly on the internet.

### Adding a Local File
   - Open the file browser of your local computer and find the file you would like to add (refer to **1** in Figure below).
   - Drag and drop the file from your local file browser into the empty space of your Pipeline Workspace (refer to **2** in Figure below).
   - Create a *File Picker Service* by double clicking in the empty space of your Pipeline Workspace and choosing the *File Picker Service* in the resulting popup (refer to **3** in Figure below). It will now appear on your Pipeline Workspace. Click on the *Upload* button with a cloud icon. In the popup window, you may choose the file you would like to add. For large files, the upload will take a moment and the status will be displayed in a loading bar.



<p align="center">
  <img width="90%" src="assets/workflow/LoadData.png">
</p>

<p style="text-align: center;">Adding a local file to a project.</p>

    

### Adding a Remote File

 * (1) Adding a file via link  (refer to **1** in Figure below)
    - Create a *File Picker Service* by double-clicking in the empty space of your Pipeline Workspace and choosing the *File Picker Service* in the resulting popup. It will now appear on your Pipeline Workspace.
    - Click on the newly created *File Picker* and you should now see its upload options in the secondary column of Workbench.
    - Provide its URL link in the *Type a Link* field at the bottom of the *File Picker* options and click the *Select* button.

 * (2) Using a file from another project (refer to **2** in Figure below)
   - Create a *File Picker Service* by double-clicking in the empty space of your Pipeline Workspace and choosing the *File Picker Service* in the resulting popup. It will now appear on your Pipeline Workspace.
   - Click on the newly created *File Picker* and you should now see its upload options in the secondary column of Workbench. You should also see the *Storage* tab open in the primary column of the *Workbench*.
   - Click the expansion on ``simcore.s3`` to access all the Studies you have created on **Sim4life**.
   - Navigate to the project and then service in that project where the file you desire is located. Drag and drop that file from the primary column into the *Drop File Here* area in the secondary column.



<p align="center">
  <img width="90%" src="assets/workflow/RemoteData.png">
</p>

<p style="text-align: center;">Adding remotely located data files to a project.</p>


    
