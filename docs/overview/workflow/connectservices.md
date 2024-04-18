## Connecting Services

Once your data are uploaded, you can connect them to the appropriate services in the *Service* catalog. Services that take input will often take multiple inputs. However, the file picker gives data from a single file. Thus, it is important to set the input settings appropriately when connecting multiple file pickers to the same service.

### Auto-Connect Option
   You may also activate or deactivate an option to automatically assign inputs to respective ports. By default, auto-connect is activated. This automatic assignment only is possible, however, when there exists unique compatible input types between the inputs being connected to a service and the input types that the service expects. For example, if a service expects one file input and one numerical input, automatic port connection is only possible when a single file output and a single numerical output are connected from a previous service to the current service.

   To de-activate the auto-connect option :
   1. Click on your username at the top right corner, and choose *Preferences*.  
   2. In the popup window, click on the question mark icon on the left side.
   3. Un-check the box next to *Connect ports automatically*.

   To re-activate this feature, simply un-check the *Connect ports automatically* box.

<p align="center">
  <img width="80%" src="assets/workflow/AutoConnect.png">
</p>

<p style="text-align: center;">Enabling auto-connect option.</p>



### Connection Indicator
   As a visual guide to connecting services, the Pipeline Workspace UI shows either dashed or solid-line arrows between Services, indicating the status of the port connections. If two Services are connected but the input ports have not been mapped, the connection between the Services will appear as a dashed line. If the ports have been mapped such that the input types of the incoming Service match those of the input ports of the receiving Service, the line between Services will appear as a solid line.

<p align="center">
  <img width="80%" src="assets/workflow/ConnectionIndicator.png">
</p>

<p style="text-align: center;">Different connection indicators between services and data.</p>

    

### Disconnecting Inputs and Outputs
   To unlink an input, click the unlink button next to the input line in the settings menu.

   To delete a connection, simply select the arrow connecting two nodes and a small unlink button will appear in the lower right-hand corner of the Pipeline Workspace. Clicking this button will disconnect the two nodes.


<p align="center">
  <img width="80%" src="assets/workflow/DisconnectIndicator.png">
</p>

<p style="text-align: center;">Disconnecting indicators between services and data.</p>

     

    
