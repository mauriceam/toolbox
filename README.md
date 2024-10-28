# Rail Track Modelling Toolbox - Multi-project Evolution

## Introduction
The *Rail Track Modelling Toolbox* is a set of models dedicated to reducing railway noise and optimizing track maintenance. Initially developed as part of the *Novel Rail Pads for Improved Noise Reduction and Reduced Track Maintenance* project, the Toolbox has evolved through several research projects to incorporate advanced features.

## Development Context
The Toolbox has been developed across three major projects:

- **Novel Rail Pads for Improved Noise Reduction and Reduced Track Maintenance:** This project, funded by the [Swiss Federal Office for the Environment (FOEN)](https://www.bafu.admin.ch/bafu/en/home.html), aimed to develop new rail pads to reduce noise emissions and extend the maintenance intervals of railway tracks. The project was a collaboration between several Swiss research institutes:
  - [Swiss Federal Institute of Technology Lausanne (EPFL)](https://www.epfl.ch/en/)
  - [Swiss Federal Railways (SBB)](https://www.sbb.ch/en/home.html)
  - [School of Engineering and Management of Yverdon (HEIG-vd)](https://heig-vd.ch/en)
  - [Swiss Federal Laboratories for Materials Science and Technology (EMPA)](https://www.empa.ch/)

For the last phase of the project, a company has joined the consortium to develop prototype railpad:

- [Semperit Group](https://www.semperitgroup.com/) from Austria

The selected approach was the development of an experimental set-up combine with a digital twin (i.e. The Three Sleepers Model presented later). Other models have been developed and experimentally validated to achieve our goals.

- **Track System Evaluation:** This project expanded the Toolbox by adding tools to evaluate and assist in the design of all components of the railway track (rails, sleepers, fasteners, ballast, etc.). New features, such as tools for identifying pads and sleeper properties, were developed.

- **TopNoise (ongoing):** The *TopNoise* project is currently continuing the evolution of the Toolbox with new models for more advanced noise management and railway infrastructure improvements.

## Versions and Releases
The Toolbox releases reflect the different stages of development:

- **V1.0.0:** The first release following the *Novel Rail Pads* project. This version contains the initial models for noise reduction and rail optimization.
  
- **V2.0.0:** The second release after the *Track System Evaluation* project. This version introduces more modular models and new features to test all components of the railway track.

- **V3.0.0 (ongoing):** The current version under development as part of the *TopNoise* project. It includes further improvements, especially in noise management and advanced diagnostic tools.

## What is this toolbox for ?

As said previously, the toolbox have been develops to design new rail pads, and thus can be used in the same way.  
Furthermore, models has been created using open source tools and can be easily modified and/or incremented with new functionalities.  
Therefore this toolbox is the first step in the creation of a open source and collaborative platform for the rail way experts.  
Anyone interested and working in this field can use and/or developed the existing models or add new ones.

## What models composed the Toolbox ?

This toolbox is composed of four finite element models and one semi-analytical model:

1. The *PadStiffness* Model
2. The *Semi-Analytical* Model
3. The *Three Sleepers* Model
4. The *Impulse* Model
5. The *Multi-Sleepers* Model

![Railtrack Modelling Toolbox Overview](./src/RailTrackModellingToolbox.png?raw=true "Toolbox Overview")

Each model can be found separately in the *src* directory. Alternatively the full toolbox can be downloaded as a Virtual Machine container and run on any Linux distribution.

A overview of each model is presented in the following paragraphs, please refer to the specific chapter in the documentation for more information on the models.

### The PadStiffness model

The Pad Stiffness Model aim to estimate the static and dynamic stiffness of the input pad design. It is a digital twin of an experimental compression system.
After validation in static and low dynamic (10 and 20 Hz) compression with the experimental results, the model have been extended to provide the stiffness in various directions and with an extended frequency range.  

### The Semi-Analytical Track model

The Semi-Analytical Track Model is aimed at simulating the dynamic response in terms of point mobility and track decay rate (TDR) of a nearly infinite track as well evaluate the radiate noise. This model uses as input the frequency dependent stiffness and damping of the pads as evaluated by the PadStiffness model. 

### The Three Sleepers model

The Three-sleeper model is a Digital Twin of an existing test setup consisting of three sleepers with two 1.8m rails installed in our lab. It carries out an harmonic simulation of the system over a user defined frequency range (multiple bands on multiple CPUs) and is able to compute the frequency response of the setup as well as the radiated noise using a monopole superposition method. This model and experimental setup form together an efficient method to validate the modeling assumptions such as for example the frequency dependant complex moduli of the railpad material(s) or the effective properties of the prestressed concrete in the sleepers. This model allows to optionnally include undersleeper pads as well.

### The Impulse model

The Impulse model is a variation of the three sleepers model, operating in the time and not the frequency domain. The rail pad materials are modelled as a generalized Maxwell model described by a Prony series.  It aims to reproduce a pass-by of a bogie on a sleeper. Therefore a *M* shaped impulse is imposed to both rails above the middle sleeper. The model output can be used to evaluate the rail pad deformation / stresses, the clamping system deformation, the ballast deflection and the mean stress acting on the ballast. These results cab thus be used to evaluate fatigue of fastening component, rail pad visco elastic recovery time as well as ballas settlement. 

### The Multi-Sleepers model

The multi-sleeper FE model is a large scale 3D structural model of a railtrack (with an arbitrary number of sleepers) using frequency dependent dynamic substructuring to evaluate quickly but in great details the vibration response of the rail and sleepers as well as compute the radiated noise level. This model allows to optionnally include undersleeper pads as well.

## Download

There are multiple ways of using the toolbox depending on your needs and knowledges:
1. Downloading a custom version of CAELinux 2020 (ISO image).
2. Downloading a Singularity container image.
3. Downloading all the files and doing a manual installation.

### Custom version of CAELinux 2020

To facilitate the use of the toolbox, a custom version of CAELinux 2020 is provided as a ISO image which can be used to install a physical or virtual machine with all software preconfigured. 

Download link to the virtual machine image/ container: see [readme.md](./ToolboxVM/readme.md) in ToolboxVM folder.

### Singularity container

To use the toolbox in another Linux operating system. including Windows WSL2, a Singularity container image is provided.

To simplify the download and installation of Singularity two bash scripts have been done to automate all the steps:
1. The first one can be used to install Singularity programme on you linux (or WSL2) machine:
```bash
bash ./install_singularity_linux.sh
```
2. The second one automate the download of the singularity image, the github repository and create an overlay with the selected Github branch or last version of the toolbox on the container:
```bash
bash ./singularity_with_overlay.sh branch_name
```


### Manual installation

The code was developed to run in a CAELinux 2020 Lite (http://www.caelinux.com) but can be adapted to run on other similar distributions (Ubuntu 18.04 for example).

The toolbox requires the following software installed on the system to run:
1. Code_Aster with MFront support (tested version 14.6)
2. Salome-Meca 2019 
3. Python 2.7 with the following libraries:

python scripts:
os, sys, shutil, PyQt5, PyQt5.QtWidgets, PyQt5.uic, PyQt5.QtCore, pyperclip, json, multiprocessing, time, pickle, math, datetime, scipy, scipy.optimize, scipy.linalg, matplotlib, matplotlib.pyplot, csv, 

Salome scripts:
salome, salome.smesh, salome.geom, salome_notebook, SMESH, GEOM, SALOMEDS

Aster scripts:
Utilitai, aster_core

## Getting Started

This repository contain three folders: *Documentation*, *src* and *Toolbox-VM*. 

The first folder contain the documentation of the toolbox: description of the models, how to use the interface and so on. The second folder, *src*, contain the individual models. The last folder, *Toolbox-VM*, contain a ISO image of a customized CAELinux/Ubuntu 18.04 environment with the whole toolbox ready to be used. 

### CAELinux or custom installation

The easiest way to start using the toolbox is to download and use the *ISO* image in *Toolbox-VM*. This image can be used to create a bootable USB disk (using Ventoy https://www.ventoy.net is recommended) in order to boot and install the OS + toolbox on a physical PC. Or even simpler, the ISO image can be used directly to install a Virtual Machine, on any OS, for example in VMware player https://www.vmware.com/fr/products/workstation-player.html.

Once booted from the ISO image, the (virtual) machine can be installed by running.  

> sudo ubiquity gtk_ui

Please note the default username / password is :

*username*: caelinux

*password*: caelinux

If you decide to install "from scratch", you will need to have first a working installation of all the prerequisites (see src/INSTALL, src/dependencies.txt and src/installDependencies.sh) and then run the setup0.sh and setup.sh scripts in the root of the toolbox:

> cd PathToToolBox
> ./setup0.sh
> ./setup.sh

Once installed, the best way to start using the model is to use the GUI provided for each model. Part of the documentation describes the steps to follow in order to run a simulation with the selected model.

### Singularity

To launch and work with the Toolbox using the Singularity container, a specific documentation is available with the usual commands and basic explanations.

Nevertheless the toolbox can be launch using the following command:
```bash
   singularity run --overlay overlay.img toolbox.sif
   ```

## Hardware requirements

The FE models included in this toolbox require at least a 4 core CPU with 16Gb of RAM to run. However, to run simulations in parallel and with detailed 3D mesh, a 8 to 16 core CPU with at 64Gb of RAM is optimal. Most of the simulations that we have carried out have been running on AMD Threadripper 24 core 128Gb or 16core 64Gb workstations. To make use of the available computer resources, please edit the ".export" files in the "working_directory" folders of the models. See Code-Aster documentation for the details of the .export files.

## Model Documentation

For each model included in the Toolbox, comprehensive technical documentation is available. Refer to the corresponding files in the GitHub repository for detailed information on their usage and applications.

## Contributing

### Learning Code_Aster

If you want to learn more about *Code_Aster* you can visit their [official web site](https://www.code-aster.org/)

### Learning Salome

If you want to learn more about *Salome*, a multi-platform open source scientific computing environment, you can visit their [official web site](https://www.salome-platform.org/)

## License
This code is published under Gnu Public Licence v3 / GPL v3

## Development, Funding & Acknowledgement

This toolbox was developed in the framework of the "Novel Railpad Project" funded by the Swiss Federal Office of Environment and developed in collaboration with EPFL, HEIG-VD, EMPA and SBB.

The finite element models of the toolbox have been developed at COMATEC institute / HEIG-VD by Maurice Ammann, Raphael Nardin and Joël Cugnoni.

The semi-analytical track model was developed in the laboratory of acoustics at EMPA by Benjamin Morin and Bart Van Damme. 