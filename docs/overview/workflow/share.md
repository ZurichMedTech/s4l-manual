## Sharing and Publishing Projects

There are two ways in which your work on the online platform can be accessed by others. You may either share an instance of your Project with other member(s) of an organization, or publish the Project as a Template for other members to copy. 

<!-- For a full demonstration of these functionalities, take a look at o²S²PARC webinar on collaboration! 

<p align="center">
<iframe width="784" height="441" src="https://www.youtube.com/embed/cI5p0bki258" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

-->

## Organization
An organization is any group of **_S4L_<sup>_lite_</sup>** users that can share _**Projects**_. To see which organizations you are a part of, go to your user preferences through your [Profile](dashboard.md) button on the top right corner of the user interface. Then choose the ```Organizations``` which will display all organizations you belong to and you may see the members of each organization by clicking on it. The member details will be then displayed in the lower half of the window under ```Members```. There are four different types of members in an organization:
1. **User**
    * Can not see the members of other organizations
    * Can not share content with the organization
2. **Member**
    * Has access to shared content of the organization
    * Can share content with the organization
3. **Manager**
    * Has Member privileges
    * Can add or remove Members
    * Can promote Members to Managers
4. **Administrator**
    * Has Manager privileges
    * Can edit the organization’s description
    * Can delete the organization

To create a new organization, click the ```+ New Organization``` button and add members by entering each new member's email address and then clicking ```Invite```. Note that you may only add members that are already registered **_S4L_<sup>_lite_</sup>** users. If a user is successfully added, you will see a confirmation message and if there was an error, e.g., the email address is not registered, you will see an error message pop up. You may then change each member's privileges by clicking on that member's name. 

<!-- ![organization](../../_media/organization.png) -->

## Sharing a Project
Sharing a Project instance with other users allows collaboration on the same pipeline and code. When one member of the shared users is editing a Project, the Project is locked for the others. When that user finishes and returns to their Dashboard, the changes will be updated when another member accesses the Project. 

<p align="center">
  <img width="90%" src="assets/share.png">
</p>

To share a Project:
1. Access the Project's options from the Dashboard by clicking on the three dot button on the upper right hand corner of the Project's card. 
2. Choose the ```More options``` option. A window should appear.
3. In the popup window, there is a panel menu to the left. Click on the ```Sharing``` button (second button from the top) to switch to the Sharing tab.
4. In the Sharing tab, click on the ```Organizations and Members``` dropdown to see the list of users you may share with. Choose one or more people/organizations to share your Project with, and then click the ```Add``` button.
5. The Project will then appear in the ```PROJECTS``` tab of the user(s) you have shared with. 

There are three types of roles for projects :
1. **Viewer**
    * Can open the project
    * Can not modify the project
2. **Collaborator**
    * Can open the project
    * Can modify the project
    * Can share the project with other members
    * Can not delete the project
3. **Owner**
    * Can open the project
    * Can modify the project
    * Can share the project with other members
    * Can delete the project

## Publishing a Project as a Tutorial
Publishing a Project as a Tutorial will save the state of the Project at the current moment and it will appear as a Tutorial Project in the ```TUTORIALS``` tab of the Dashboard. Any changes made to the original Project after publishing as a Tutorial will not change the Tutorial. Clicking on the Tutorial Project in the ```TUTORIALS``` tab will create a copy of the contents of the Tutorial accessible in your ```PROJECTS``` tab. Any changes you make to this new Project will not affect the original Tutorial. 

To publish your Project as a Tutorial:
1. Access the Project's options from the Dashboard by clicking on the three dot button on the upper right hand corner of the Project's card. 
2. Choose the ```More options``` option. A window should appear.
3. In the popup window, there is a panel menu to the left. Click on the ```Save as Tutorial``` button (bottom-most button)  to switch to the Tutorial tab.
4. Set the access rights of the Tutorial in the popup menu. You may make the Tutorial accessible to only yourself or members of organizations. If you choose Organizations, you will be able to select from the list of organizations that you are a part of. 

<p align="center">
  <img width="90%" src="assets/tutorials.png">
</p>

5. You may also choose to publish the Tutorial with the data inside (for example, if you have any files saved in a JupyterLab inside the Project). To publish with data, scroll down in the modal and make sure the "Publish with data" field is checked. To export the pipeline structure without any customizations, uncheck the box.
6. Click the ```Publish``` button on the bottom right hand corner.
7. The Tutorial will now appear as a Tutorial Project in your ```TUTORIALS``` tab. If you have chosen to share the Tutorial with members of an organization, others in that same organization will also see the Project in their respective ```TUTORIALS``` tabs. 

There are three types of roles for projects :
1. **Viewer**
    * Can create a copy of the tutorial by clicking
2. **Colloborator**
    * Can create a copy of the tutorial by clicking
    * Can edit the tutorial
    * Can share the tutorial with other members
    * Can not delete the tutorial
3. **Owner**
    * Can create a copy of the tutorial by clicking
    * Can edit the tutorial
    * Can share the tutorial with other members
    * Can delete the tutorial
