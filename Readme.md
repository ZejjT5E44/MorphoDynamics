# Morphodynamics <img src="/images/logo.png" alt="alt text" width="50">

This software can be used to analyze the dynamics of single-cells imaged by time-lapse fluorescence microscopy. The dynamics of morphology and fluorescence intensity distribution can be jointly analyzed through the segmentation and splitting of cells into a set of smaller regions (windows) that can be represented as two-dimensional grids to facilitate interpretation of events.

This software has been developed at Bern University by Cédric Vonesch (Science IT Support and Pertz lab) and Guillaume Witz (Microscopy Imaging Center and Science IT Support) with the collaboration of Jakobus van Unen (Pertz lab).

**For a complete documentation see the [Morphodynamics website](https://guiwitz.github.io/MorphoDynamics/mydocs/Introduction.html)**.

## Install the package

The Morphodynamics package had undergone a massive change between version 0.2.4 and 0.3.0, in particular with a new interace in napari and a more customized way of generating post-processing plots. If you want to install the old 0.2.x series version, please use:

```
pip install git+https://github.com/guiwitz/morphodynamics.git@v0.2.4
```

To install the latest version of the software, please use:

```
pip install --upgrade git+https://github.com/guiwitz/morphodynamics.git
```

## Notebooks

While the software can be used via its API, notebooks implementing a user interface are also provided. You can download two notebooks for interactive analysis here:
- [Morpho_segmentation.ipynb](https://guiwitz.github.io/MorphoDynamics/Morpho_segmentation.ipynb) where you can run cell segmentation and splitting interactively
- [Postprocessing.ipynb](https://guiwitz.github.io/MorphoDynamics/Postprocessing.ipynb) where you can generate post-processing figures for shape, displacement, intensities etc.

## Environment

To ensure that you have all recommended packages to perform interactive work, we recommend to create en environment with conda. If you don't have conda installed yet, follow [these instructions](https://docs.conda.io/en/latest/miniconda.html) to install a minimal version called miniconda.

To create the appropriate environment that will for example also contain the optional dependency ```cellpose``` for cell segmentation, save the following [environment.yml](https://raw.githubusercontent.com/guiwitz/MorphoDynamics/master/environment.yml) file to your computer (use ```Save as``` in your browser) and execute the following command from where you downloaded it:

```
conda env create -f environment.yml
```

Then activate the environment:

```
conda activate morphodynamics
```

The Morphodynamics package is automatically installed in that environment.


## Updates

To update your local installation with the latest version available on GitHub, activate the environment and install the package directly from GitHub:

```
conda activate morphodynamics 
pip install --upgrade git+https://github.com/guiwitz/MorphoDynamics.git@master#egg=morphodynamics
```

Note: close all notebooks (click on File | Close and Halt) prior to the update and reopen them afterwards.

## Usage

Whenever you want to use Jupyter and the Morphodynamics package, open a terminal, activate the environment 

```
conda activate morphodynamics
```

and start a Jupyter session:

```
jupyter notebook
```

## Development

Versioning is done automatically via ```setuptools_scm```. To increment a version, create a new tag and push it to GitHub:

```
git tag -m "git versioning" -a X.Y.Z
git push origin X.Y.Z
```
