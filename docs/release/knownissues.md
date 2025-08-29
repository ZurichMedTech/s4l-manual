## Known Issues

Version: **sim4life.io** V8.0.0, **sim4life.science** V8.0.0

### 1. Video Streaming

If you experience performance/quality decrease for the video streaming, please try to switch the streaming mode to "Jpeg", however, we'd recommend to use video streaming whenever possible (with enough bandwidth).

<p align="center">
  <img width="70%" src="assets/videostream.png">
</p>

### 2. Job submission into the cloud

There is currently a bug that prevents the user to have 10 concurrent iSolve jobs running. If the jobs are submitted within a short time of each other, they will eventually end up on one ec2-instance and run sequentially. This typically happens with MultiPort Simualtions.

### 3. Integer buffer overflow with MPI iSolve Jobs

Large LF simulations that use `PETSc` can fail with integer overflow. The workaround is to use more than 1 or 2 MPI ranks in the Solver Settings.

### 4. Cuda simulation memory error

The EmFdtd Cuda solver suffers from a memory allocation buffer. This typically happens when simulations run on more than on NVIDIA A10 cards (`MEDIUM`). Workaround is to use the other option with hardware acceleration.

### 5. Disk space limits

The current limits for disk space are for the sim4life GUI are:

- `MEDIUM`: 200 GB
- `LARGE`: 800 GB
- `XLARGE`: 800 GB

Due to the algorithm used to orchestrate the machines, it may happen that you end up on a `LARGE` machine (with constraint CPU/RAM usage) although you chose a `MEDIUM`. Since we do not yet limit the disk space you might actually create a 200 GB workspace without noticing. However, when you start the project the next time on a `MEDIUM` machine, you will run out of disk space. (You can see this in the log of a failed to start service). Workaround in that case is to use a `LARGE` instance for your project.


### 6. Sim4Life application randomly hangs when working with projects containing complex CAD models

This issue can occur due to the rendering settings. Please try the following steps:
  - Open "Preferences" → "3D Renderer" → "Visuals" and set "Accurate Transparency Mode" to "Disabled" (you can do this in an empty project).
  - Close the "Preferences" window.
  - Go back to the dashboard, or restart the application via "Preferences" → "Application" → "Force Application Restart".

Since "Preferences" are stored globally, the change will apply the next time you start a new Sim4Life service.
**Important**: Make sure no other project is open when you change the setting. If a project is open, its stored settings may overwrite your "Preferences" when closing.