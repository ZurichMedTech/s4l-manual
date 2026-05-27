# Release Notes (sim4life.web)

## Sim4Life Service

### Version: 9.4.3
- Release Date: 27.04.2026
- Selected New Features/Improvements
    - Added AxWare support for Blackwell architecture. 
    - Added drag/drop support for Mask Filter.
- Fixed
    - Fixed a bug when selecting file paths.
    - Fix an issue where jobs cannot be submitted because the controller could not be found.


### Version: 9.4.2
- Release Date: 09.04.2026
- Selected New Features/Improvements
    - In-App Release Notes
        - New version popups are now more informative.
        - When a new platform version is released, the “New Version Released” dialog now displays the full release notes directly in the app, so you can review changes without opening an external link.
    - More Resilient Service State Tracking
        - No more services stuck in “Pending”.
        - Interactive services no longer get stuck showing a "pending" state when a WebSocket notification is lost. A periodic REST polling fallback has been added so the frontend will always catch up with the actual service state, even if the real-time channel drops a message.
    - Fixes & Stability Improvements
        - Fixed a race condition affecting file picker progress updates (RTC).
        - Fixed an issue where active dashboard filters were not displayed correctly.
        - Prevented users from duplicating projects that are currently open

### Version: 9.4
- Release Date: 05.03.2026
- Selected New Features/Improvements
    - The new thermal unstructured stationary solver enables the calculation of steady-state temperature distribution in complex geometries using an unstructured mesh. It determines the temperature field once thermal equilibrium is reached. This approach is particularly useful for irregular shapes where flexible meshing improves accuracy and where only the final stabilized thermal condition is required. It also supports multiport configurations, similar to the rectilinear solver, allowing multiple thermal inputs to be defined within the same simulation.
    - The T-increase Thermal Transient Simulation option enabled also for thermal unstructured solver.
    - The option to directly link the multiport low-frequency solver to the neuron solver enables users to assign the weight factor for each port directly in the neuron solver’s source settings.
    - Users can now disable the current conversation check with the checkbox within sources in the Magneto-Static Vector-Potential solver when current loops are closed using PEC instead of line element loops.nd easier installation.
    - Stability, performance, and quality assurance: Improved robustness under demanding workloads, smoother handling of large models, clearer feedback during long-running operations, and a faster patch delivery cycle help ensure that complex projects remain stable and reproducible.
    - Integrated AI assistant: Directly accessible from the search bar, the AI assistant answers questions about tools, workflows, solvers, and APIs, — helping users navigate modeling tasks, understand concepts, and locate relevant functionality more efficiently.
    - A cleaner, more consistent user interface: Streamlined tool organization reduces visual clutter and improves focus during multi-step simulation workflows.
    - Stronger scripting and documentation coherence: Improved alignment between GUI and Python workflows, a clearer API structure, and more accessible documentation support the kind of large-scale, script-driven studies illustrated above.
    - Rebuilt Manual and Python API reference to provide better navigation, improved browsing, and enhanced search functionality.
    - Easier tag management through an improved user interface, making it faster to organize projects without interrupting your workflow.

### Version: 9.3
- Release Date: 13.01.2026
- Selected New Features/Improvements
    - New color palette and design
    - Update symbol server python libraries
    - Replace Typesense with Meilisearch in search service
    - Cleanup snap features in neuron tools
    - Rename "Place Electrodes" to "Place Templates", add option to specify an offset
    - Extend Move tool: add modifier to allow "Move From To" to align moved entity with the normal at the target surface
    - Allow specifying image spacing during model import for png, tiff and bmp files
    - Add option for periodic pulse shapes in neuron simluations
    - Keep chat history in AI Chatbot
    - Adds Hornet plugin
    - Add tool (and Python API) to sample points on triangle mesh surfaces (and patches)
    - Add option to place local coordinate system "anchors" at sample points, to simplify placing template models at these positions
    - Add modeling tool to create patch at the interface between a selection of triangle mesh entities
    - Add tool to convert (interpret) an image as a labelfield
    - Add context menu tool to load tissue list for labelfield
- Fixed
    - Fix hanging iSolve when subgridding setup is wrong
    - Fix issue with ImageFaceting that breaks loading certain documents
    - Fix for Delete Triangle Patch to preserve preexisting patches
    - Fix for simulations with virtual thin layers being unable to run

### Version: 9.2
- Release Date: 07.10.2025
- Selected New Features/Improvements
    - Modeling Intelligence
        - Upgraded Optimizer integrates advanced surrogate modeling with a multi-objective genetic algorithm (MOGA) for powerful and efficient design optimization.
        - Transforming complex parameter sweeps into interactive, visual analyses for faster and deeper insight.
        - Pareto Front Visualization clearly displays trade-offs between competing objectives such as safety, efficacy, and energy efficiency.
        - Proven Impact: In a spinal cord stimulation study, discovered pulse shapes delivering the same neural recruitment with up to 5× lower energy consumption.
    - Third-generation Advanced Anatomical Modeling and AI-Powered Tools
        - Third-generation deep learning model auto-labels head, neck, and torso tissues from MRI/CT scans.
        - Generating solver-ready models directly from raw images, reducing setup time and user interaction by about 50% compared to previous versions.
    - OpenFOAM Plugin
        - The user can run OpenFOAM solvers directly from Sim4Life’s Plugin Manager — no command-line required.
        - Simple Workflow: Import meshed anatomy, choose a fluid or small-strain-mechanics solver, set boundary conditions, and click “Run.”
        - All dictionaries, solver logs, and post-processing outputs are stored within the Sim4Life project for full reproducibility.
    - Broadband Skin Power Absorption Model
        - New Broadband Skin Model implements the latest Christ et al. (2025) model, now adopted by IEC/IEEE standards.
        - Enabling absorbed power density determination for regulatory compliance and device safety evaluation across 10 and 110 GHz.
        - Applicable across all use cases and human models within Sim4Life.web V9.2.
    - Deep Brain Stimulation (DBS)/Stereoelectroencephalography (sEEG) Electrode Generator
        - New tool rapidly creates parameterized DBS and sEEG electrode models for neurostimulation applications.
        - The user can customize diameter, contact length, spacing, arc angle, segmentation, and tip offset interactively or via Python API.
        - Enabling seamless, scriptable design and simulation of personalized neurostimulation implants.
    - Help Center
        - Integrated Help Center connects directly with Application Support from within Sim4Life.web V9.2.
        - Faster Troubleshooting by easily sharing logs and screenshots (opt-in).
        - Simplifying support requests, improves feedback loops and helps new users get started faster.

### Version: 9.1
- Release Date: 09.10.2025
- Selected New Features/Improvements
    - Add Filter to Task Manager
    - Add a Table for visualizing tabular data in forms
    - Ignore capitalization of file endings in file dialog filters (*.step vs *.STEP)
    - Default to disabling Accurate Transparency to avoid hanging rendering
- Fixed
    - Fix bug in selection order of modeling tree
    - Fix bug with visibility of 2D plots
    - Fix crash when importing multiple modeling files at once
    - Fix bug when Application goes into Unresponsive State and never recovers (at startup and when rendering)
    - Fixes invitations links produced by PO center

### Version: 9.0.1
- Release Date: 14.08.2025
- Selected New Features/Improvements
    - Activity Overview Improvements
        - The Activity Overview backend has been redesigned for better performance and accuracy.
        - Multiport simulations from Sim4Life now appear as a single run for easier tracking.
    - Metamodeling
        - Metamodeling now includes Functions support.
        - Default inputs are now editable when creating new functions.
        - Functions Browser allows the user to list available functions, edit the title and description and view function details.
    - Conversations Upgraded
        - Project Conversations are now more powerful and collaborative.
        - Multiple conversations per project to separate topics. 
        - Edit and Delete messages.
        - Real-time updates between multiple users — chat is instantaneous.
        - Notify specific users.
        - Pinned conversations in pipeline for location-specific discussions.
    - Extended Project Search
        - The Projects tab search widget now supports searching across My Projects, Templates and Public Projects.
- No longer broken
    - Concurrent download of multiport results would yield to corrupt files
    - Fix bug related to rate limits in plugins discover that would break the full sim4life as well
    - Hide noisy JSON MONITORING in logs
    - Fix issue in synchronization of job states file
    - Fix the wrong handling of faulty job creation
    - Fix removal of empty task groups in Task Manager
    - Fix Index behaviour for popup windows
    - Fix issue with stopping deleting jobs in local isolve


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

<h3 id="v1.92.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.92.0.md">Version: 1.92.0</a></h3>
 
 - Release Date: 19.05.2026
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.92.0.md) 

<h3 id="v1.91.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.91.0.md">Version: 1.91.0</a></h3>
 
 - Release Date: 09.04.2026
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.91.0.md) 

<h3 id="v1.90.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.90.0.md">Version: 1.90.0</a></h3>
 
 - Release Date: 05.03.2026
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.90.0.md) 

  <h3 id="v1.89.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.89.0.md">Version: 1.89.0</a></h3>
 
 - Release Date: 12.02.2026
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.89.0.md) 

 <h3 id="v1.88.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.88.0.md">Version: 1.88.0</a></h3>
 
 - Release Date: 13.01.2026
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.88.0.md) 

<h3 id="v1.87.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.87.0.md">Version: 1.87.0</a></h3>
 
 - Release Date: 04.11.2025
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.87.0.md) 


<h3 id="v1.86.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.86.0.md">Version: 1.86.0</a></h3>
 
 - Release Date: 07.10.2025
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.86.0.md) 

<h3 id="v1.85.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.85.0.md">Version: 1.85.0</a></h3>
 
 - Release Date: 09.09.2025
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.85.0.md) 


<h3 id="v1.84.0"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.84.0.md">Version: 1.84.0</a></h3>
 
 - Release Date: 14.08.2025
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v1.84.0.md) 

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



