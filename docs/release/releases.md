# Release Notes (sim4life.web)

## Sim4Life Service

### Version: 9.0
 - Release Date: 26.06.2025
 - [Sim4Life](https://sim4life.swiss/) V9.0 is the latest version of our online simulation platform for computational life science research, device design, and optimization, as well as safety and electromagnetic compliance evaluations. This release includes new tools for optimization, artificial intelligence (AI-) driven modeling, solver plugin support and pipelining to facilitate powerful, automated workflows throughout the entire modeling chain. Sim4Life V9.0 – available for both web and desktop – delivers more power, flexibility, and integration to your simulation workflows.

 - Selected new features
    - Unified Ecosystem
        - Fully integrated with the o²S²PARC platform, providing access to all functionalities of o²S²PARC.
        - Cloud-based platform connecting specialized simulation tools, data analysis pipelines, and computational models from across health and life sciences research communities.
        - Enables complex, the multi-disciplinary workflows and empowers research beyond capabilities of isolated simulation tools.
    - Third-Party Plugin Integration
        - New open plugin framework allowing integration of user-provided or third-party simulators and solvers, thereby expanding the range of supported physics applications and enabling custom workflows, all within a unified interface.
        - Plugin simulators benefit from Sim4Life’s powerful modeling, preprocessing, cloud computing, and post-processing functionalities.
    - Rich Automated Workflows
        - New pipelining and workflow environment allowing users to build, automate, and share advanced multi-stage simulation pipelines.
        - Connecting applications – in an automated manner – across the expanded Sim4Life ecosystem for integrated, reproducible and collaborative research.
    - Cloud Scalability – Now on Desktop, Too
        - Submit and manage simulations via the Sim4Life desktop or web interface.
        - Access to nearly limitless high-performance computing infrastructure.
        - Transparent job tracking, real-time cost monitoring, one-click publishing.
    - Advanced Anatomical Modeling and AI-Powered Tools
        - New AI-powered segmentation tools for head-related modeling (e.g., automatic 10-10 system placement).
        - AI-powered registration of detailed atlases to the brain.
        - Automated trunk segmentation from MRI/CT images.
        - Expanded tissue property database with updated thermal and water content data.
    - Meta-Modeling, Optimization, and Uncertainty Quantification (Preview)
        - New meta-modeling framework leveraging state-of-the-art intelligent algorithms (e.g., from Dakota Project integration (Sandia National Laboratories)).
        - Surrogate modeling or response surfaces, optimization and uncertainty quantification.
        - Efficient design-of-experiment tools.
        - Upcoming expansion with new tools and applications.
    - Activity Center, accessible anytime from the top navigation bar, displays all active processes across your Projects.
    - Conversations feature to enhance collaboration and ensure alignment across teams.
    - Upgrade to CUDA 12.8 runtime everywhere.
    - Upgrade base docker images from Ubuntu 20.04 to Ubuntu 24.04

- No longer broken
    - Fixed issues with legend in plots.
    - Fixed issues with monitoring plots in Task Manager.
    - Fixed a bug that blocked output ports from downloading, which was preventing dynamic services from starting properly.
    - Resolved an issue where projects appeared as "undefined-metadata" in the Billing Center — project names now display correctly!



### Version: 8.4.0
 - Release Date: 11.03.2025
 - [Sim4Life](https://sim4life.swiss/) V8.4.0 is the latest version of our online simulation platform for computational life science research, device design, and optimization, as well as safety and electromagnetic compliance evaluations. This new version introduces improvements and fixes to enhance your simulation experience and makes Sim4Life more user-friendly and efficient.
 - Selected new features
    - The Shop
        - Direct online access to all functionalized ViP models from the IT’IS Foundation and to EM phantoms from SPEAG.
        - Allows users to incorporate these gold-standard models into simulations directly via the web GUI, simplifying setup and improving workflows.
    - Intuitive Project Organization
        - New drag-and-drop functionality for managing simulations online, allowing users to effortlessly organize their workspaces and maintain an overview of multiple projects.
        - Recovery of deleted items thanks to a new trash bin for projects, folders, and workspaces.
    - Streamlined Platform Experience and Enhanced Ecosystem
        - “New” menu simplifies the creation of not only Sim4Life projects, but also of complementary iSeg and JupyterLab projects.
        - A significant step toward comprehensive support and integration with additional applications, planned for the forthcoming Sim4Life V9.0 release.
    - Simplified Neuro-Stimulation Settings
        - A single checkbox in the settings provides access to different tissue/electrode contact impedance models, making it easier to account for the effects of non-ideal interfaces on pulse shapes.
        - Support for importing compressed .hoc data files, essential for users who want to modify neuron models from online sources such as ModelDB, the Human Brain Project (HBP), or the Allen Brain Institute for use in Sim4Life neuron simulations.
    - JupyterLab and Cloud-Powered Flexibility
        - Users can now effortlessly launch a full-featured, standalone JupyterLab environment, complete with access to the Sim4Life Python API and AWS computational resources.
        - Robust cloud infrastructure provides reliable and accessible simulation capabilities at scale.
    - Project cards with icons offer a quick visual hint of each project’s contents, making them easier to recognize at a glance.
    - Simplified full-screen mode improves usability.
    - Front-end UI configurations are now stored in the backend.

- No longer broken
    - Fixed issue where service startup time was unnecessarily long.
    - Fixed issue where project/study remained locked until the page was refreshed.
    - Fixed issue where heavy dynamic services would fail to start.


### Version: 8.2.1
 - Release Date: 23.01.2025
 - [Sim4Life](https://sim4life.swiss/) V8.2.1 is the latest version of our online simulation platform for computational life science research, device design, and optimization, as well as safety and electromagnetic compliance evaluations. This new version introduces improvements and fixes to enhance your simulation experience and makes Sim4Life more user-friendly and efficient.
 - Selected new features
    - Upgrade of all python libraries
    - Upgrade to JupyterLab 4.3.1
    - Refactored tree library in frontend to make the trees render much faster
    - Updated task manager for better UX
    - Added missing icons

- Selected improvements
    - Fixed bug with Task Manger and Multiport Simulations
    - Fixed slow startup in ImageML plugin
    - Fixed tree metadata for testing
    - Fixed bi-directional theme change
    - Fix shared memory problem for ImageML
    - Fix bug in context menu
    - Vulkan configuration mounted into s4l-jupyter

### Version: 8.2.0
 - Release Date: 14.11.2024
 - Selected new features
    - Introduced a new resource monitoring widget for CPU and RAM usage.
    - Launched a new Help Center for advanced search.
    - Added guided tours for first-time users.
    - IPython-based Python console for simple scripting tasks.
    - Python upgrade to version to 3.11.9.
    - Upgrade to Neuron Solver 8.2.6.
    - New service: s4l-python runners (CPU/MPI and GPU) for running Sim4Life as a computational job.

- Performance and usability enhancements
    - Speed improvements in tree navigation for projects with many entities.
    - Faster application startup using compressed project files.
    - Completely revamped the video streaming backend for increased stability.

- New tools
    - Material calculator.
    - Screen capture with download functionality.
    - Cursor and ruler added in the modeler.
    - Symmetry Tool.
    - Extrude Patch.
    - Reconstruct Hull.
    - Join Wires.
    - Annotate Tool.

- Selected improvements
    - Fixed inconsistency in results when searching with different cases (lowercase or uppercase).
    - Fixed issue with compiling Neuron mechanism files\

### Version: 8.0.0
 - Release Date: 14.03.2024
 - [Sim4Life](https://sim4life.swiss/) V8.0.0 is the first public release of the powerful web-based simulation platform that allows you to model and analyze real-world phenomena and design complex technical devices in a validated environment. 
 - Features
    - Accessible fully online
    - Based on o<sup>2</sup>S<sup>2</sup>PARC technology
    - User-friendly GUI
    - 3D modeling environment and CAD translators
    - Postprocessing and visualization of the simulation results 
    - Solvers & Tissue Models
        * P-EM-FDTD: Electromagnetics Full Wave Solvers
        * P-EM-LF: full EM finite element method (FEM) low-frequency solver suite
        * P-Thermal: Thermodynamic Solver based on Pennes Bioheat equations
        * P-Acoustics: Acoustics Solver
        * T-Neuro: Neuronal Tissue Models, allowing neurostimulation investigations
    - Computational anatomical models Yoon-sun (the first Korean human model of the IT'IS [Virtual Population](https://sim4life.swiss/virtual-population)) and Duke
    - Material database
    - Python and Jupyter Notebook scripting
    - Click [here](https://sim4life.swiss/specifications) for the complete list


## sim4life.web Platform

<h3 id="v1.83.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.83.0.md">Version: 1.83.0</a></h3>
 
 - Release Date: 26.06.2025
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.83.0.md) 

<h3 id="v1.80.2"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.80.2.md">Version: 1.80.2</a></h3>
 
 - Release Date: 11.03.2025
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.80.2.md) 

<h3 id="v1.79.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.79.0.md">Version: 1.79.0</a></h3>
 
 - Release Date: 15.01.2025
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.79.0.md) 

<h3 id="v1.78.2"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.78.2.md">Version: 1.78.2</a></h3>
 
 - Release Date: 14.11.2024
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.78.2.md)

<h3 id="v1.78.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.78.0.md">Version: 1.78.0</a></h3>
 
 - Release Date: 07.11.2024
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.78.0.md)

<h3 id="v1.77.3"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.77.3.md">Version: 1.77.3</a></h3>
 
 - Release Date: 23.09.2024
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.77.3.md)

<h3 id="v1.77.2"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.77.2.md">Version: 1.77.2</a></h3>
 
 - Release Date: 20.09.2024
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.77.2.md)

<h3 id="v1.77.1"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.77.1.md">Version: 1.77.1</a></h3>
 
 - Release Date: 20.09.2024
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.77.1.md)

<h3 id="v1.77.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.77.0.md">Version: 1.77.0</a></h3>
 
 - Release Date: 20.09.2024
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.77.0.md)

<h3 id="v1.76.1"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.76.1.md">Version: 1.76.1</a></h3>
 
 - Release Date: 22.08.2024
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.76.1.md)

<h3 id="v1.76.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.76.0.md">Version: 1.76.0</a></h3>
 
 - Release Date: 22.08.2024
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.76.0.md)


<h3 id="v1.75.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.75.0.md">Version: 1.75.0</a></h3>
 
 - Release Date: 11.07.2024
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.75.0.md)



