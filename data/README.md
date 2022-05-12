# Data information

This folder contains experimental data for the arXiv preprint, [Microplankton life histories revealed by holographic microscopy and deep learning](https://arxiv.org/abs/2202.09046)

The data files are stored in numpy array format. 

## data_figure1

  - fig1_data.npy: Example holograhic image of planktons. The data is used to generate **Figure. 1a**, and **Figure. 1b** in the paper. 
  
The code for generating the figures can be found in [1-example_RU-Net.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/1-example_RU-Net.ipynb).

## data_figure2

  - Oxyrrhis_data.npy: A 50-frame image sequence of *Oxyrrhis marina*. The data is used to generate **Figure. 2a** in the paper.
  - Correlation_data: Contains the predicted dry masses and radii for different plankton species. The data is used to generate **Figure. 2b** and **Figure. 2c** in the paper.

The code for generating the figures can be found in [1-example_RU-Net.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/1-example_RU-Net.ipynb).

## data_figure3

### Feeding event

  - predator_sequence.npy: Predator image sequence in the feeding event (**Figure. 3**)
  - prey_sequence.npy: Prey image sequence in the feeding event (**Figure. 3**)
  - predator_2d_coords.npy: In-plane (2D) coordinates of predator
  - prey_2d_coords.npy: In-plane (2D) coordinates of prey
  - Correlation_data: Contains the dry mass data of prey and predators in feeding event (**Figure. 3e**).

The code for generating the figures can be found in [2-example_WAC-Net.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/2-example_WAC-Net.ipynb)


## data_figure4

### Double division event

  - Cell1_sequence.npy: Parent cell image sequence in the divsion event (**Figure. 4**). Also contains 
  - Cell2_sequence.npy:
  - Cell3_sequence.npy:
  - Correlation_data: