# Morphodynamics <img src="/images/logo.png" alt="alt text" width="50">

This software can be used to analyze the dynamics of single-cells imaged by time-lapse fluorescence microscopy. The dynamics of morphology and fluorescence intensity distribution can be jointly analyzed through the segmentation and splitting of cells into a set of smaller regions (windows) that can be represented as two-dimensional grids to facilitate interpretation of events.

This software has been developed at Bern University by Cédric Vonesch (Science IT Support and Pertz lab) and Guillaume Witz (Microscopy Imaging Center and Science IT Support) with the collaboration of Jakobus van Unen (Pertz lab).

**For a complete documentation see the [Morphodynamics website](https://guiwitz.github.io/MorphoDynamics/mydocs/Introduction.html)**.

## Installation

## pip

This software can be installed via pip using the following command:

```
pip install --upgrade git+https://github.com/guiwitz/morphodynamics.git@master#egg=morphodynamics
```

## Interactivity

As the software has a strong interactive component via Jupyter notebooks, we suggest to install ```morphodynamics``` within an environment where notebooks can be run. To create such an environment we recommend to use conda. If you don't have conda installed yet, follow [these instructions](https://docs.conda.io/en/latest/miniconda.html) to install a minimal version called miniconda.

### Creating the environment

The [```environment.yml```](environment.yml) file in this repository can be used to create the appropriate environment that will for example also contain the optional dependency ```cellpose``` for cell segmentation. To use it, just [download the file](https://guiwitz.github.io/MorphoDynamics/environment.yml) and then execute the following command wherever you downloaded it:

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

Two notebooks are provided in the [notebooks](notebooks) folder. [Morpho_segmentation.ipynb](notebooks/Morpho_segmentation.ipynb) allows you to perform cell segmentation and windowing. It accepts data in the form of series of tiffs, tiff stacks or nd2 files (still experimental). Once segmentation is done and saved, that information can be used to proceed to the data analysis per se in the [InterfaceFigures.ipynb](notebooks/InterfaceFigures.ipynb) notebooks. There you import the segmentation, and can choose from a variety of different analysis to plot.

## Development

When releasing a new version v.X.Y.Z, bump the version in the [version.txt](morphodynamics/version.txt) file, commit-push, and create an annotated tag:

```
git tag -m "git versioning" -a X.Y.Z
git push origin X.Y.Z
```

When updating the master branch in between releases, automatically bump the version in the [version.txt](morphodynamics/version.txt) file by using the [version.py](morphodynamics/version.py) module: activate the environment, move to the project folder and execute:

```
python morphodynamics/version.py
```

The new version will be listed in ```conda list``` and the ```morphodynamics.__version__``` variable.
