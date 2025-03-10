# Frequently Asked Questions

Below you will find answers to some of the questions we get frequently from our users. Please contact us at [s4l-web-feedback@zmt.swiss](mailto:s4l-web-feedback@zmt.swiss) in case you don't find answers to your questions. You can also join our forum page https://forum.zmt.swiss to exchange ideas or tips with other **Sim4Life** users.

1. [How can I import a .smash file generated using Sim4Life desktop?](#faq1)
2. [What happens to running simulations when I go back to the dashboard?](#faq2)
3. [Is it possible to automatically save my study?](#faq3)
4. [What options do I have when I want to run my simulations on GPU?](#faq4)
5. [I experience degraded rendering and deteriorated performance such as visualization delays in 3D window. What can I do to fix it?](#faq5)
6. [I lost my internet connection when using Sim4Life.web. Can I refresh the page?  Will it cause problems with the model?](#faq6)


---

### <a id="faq1"></a> 1. How can I import a .smash file generated using Sim4Life desktop?

- Click ```Start Sim4Life``` to create a new project.
- Click ```Dropdown Burger Menu``` and select ```Open ...```.
- Click ```UPLOAD FILE```. Browse the .smash file you would like to upload and click ```Open```. 
- If you need to upload also the results, then click the small triangle next to ```UPLOAD FILE``` and select ```Upload folder```. Browse the folder you would like to upload and click ```Upload```.
- Select the .smash file and click ```Open``` to open this project. 

<br>
<p align="center">
  <img src="assets/import.gif">
</p>


---

###  <a id="faq2"></a> 2. What happens to running simulations when I go back to the dashboard?

The simulations will continue running and your file will be automatically saved. It is recommended to close the GUI if not needed (not to spend credits for GUI), once you submit your simulation jobs.   

---

###  <a id="faq3"></a> 3. Is it possible to automatically save my study?

- When you close a Sim4Life.web project by clicking ```Dashboard``` button, the project will be automatically saved. If you didn't give a name before then it will be saved as ```AutoSave.smash```
- When you submit a job to run, the project will be also automatically saved. 
- In addition, you can enable/disable automatically saving option or set the saving interval on ```Application``` window which can be reached by clicking ```Preferences``` via  ```Dropdown Burger Menu``` and selecting ```Application```.

---

###  <a id="faq4"></a> 4. What options do I have when I want to run my simulations on GPU?

When your simulation is ready and if you select aXware or CUDA as Kernel, then you will see three options when you click ```Run``` button. 

<p align="center">
  <img width="20%" src="assets/runoptions.png">
</p>

- (1) ```Run```: if you click this button, your simulation will run in the same machine in AWS where you have the *Sim4Life* running. It is currently a computer with 16 CPU cores, 64 GB of RAM and 16 GB of a T4 NVIDIA GPU card. If you run with this option, you have to keep the GUI open until the simulation is completed.
- (2) ```SMALL[GPU]```" If you click this button, your simulation will be detached from the GUI and will run on another setup, It is currently a computer with 8 CPU cores, 32 GB RAM, 24 GB of a A10G NVIDIA GPU card. If you run with this option, you can log out and come back later.
- (3) ```MEDIUM[GPU]```" If you click this button, your simulation will be detached from the GUI and will run on another setup, It is currently a computer with 48 CPU cores, 192 GB RAM, 4xA10G NVIDIA GPU card with 4x24 GB Video RAM. If you run with this option, you can log out and come back later.

---

###  <a id="faq5"></a> 5. I experience degraded rendering and deteriorated performance such as visualization delays in 3D window. What can I do to fix it? 

Please follow the suggestions below to improve the video streaming:
  - move to a 2.4GHz WiFi network (if available), or
  - use a cable/ethernet connection.

If any of the above-mentioned solutions are not available or the performance is not improved, please follow the steps below to change the video streaming settings:
 - Click “Menu” and select “Preferences”.
 - Select “3D Rendering | Streaming”.
 - Change “Streaming type” to “Jpeg”.

<p align="center">
  <img width="70%" src="assets/videostream2.png">
</p>


<!-- <details> 
  <summary><b>5. I experience degraded rendering and deteriorated performance such as visualization delays in 3D window. What can I do to fix it?</b></summary>
  
  Please follow the suggestions below to improve the video streaming:
  - move to a 2.4GHz WiFi network (if available), or
  - use a cable/ethernet connection.
  
  If any of the above-mentioned solutions are not available or the performance is not improved, please follow the steps below to change the video streaming settings:
  - Click “Menu” and select “Preferences”.
  - Select “3D Rendering | Streaming”.
  - Change “Streaming type” to “Jpeg”.
  
<p align="center">
  <img width="70%" src="assets/videostream2.png">
</p>
</details> -->

---

###  <a id="faq6"></a> 6. I lost my internet connection when using Sim4Life.web. Can I refresh the page?  Will it cause problems with the model?

There is a timeout of 15 minutes. You can refresh the page. After refreshing, if you end up on the dashboard, just open the study again.
