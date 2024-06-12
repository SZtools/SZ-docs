Susceptibility Zoning plugin (SZ)
=================================

Introduction
------------

This repository contains the code for a plugin for `QGIS <https://www.qgis.org>`_, called "Susceptibility Zoning plugin" (SZ-plugin), aiming at creating maps of susceptibility to various natural forcing elements.

The plugin has been developed with a main focus and application towards landslides susceptibility, but it can be applied to different types of natural events or inter-disciplinary applications.

The plugin uses several type of statistical model for susceptibility evaluation, such as:

* Weight of Evidence
* Frequency Ratio
* Logistic Regression
* Decision Tree
* Support Vector Machine
* Random Forest

The plugin allows to cross-validate the results by simple random selection of test/train samples or allows to cross-validate by k-fold cross-validation method.

Installation
------------

.. toctree::
   :maxdepth: 1
   :hidden:

   installation/requirements
   installation/download

The SZ plugin is not an official QGIS plugin.

Minimum requirements
~~~~~~~~~~~~~~~~~~~~~

Minimum tested version of QGIS is 3.28

Tested on:

* Ubuntu 20.04 - QGIS 3.34
* Windows 10 - QGIS 3.28/QGIS 3.34
* MacOS Sonoma 14.4 - QGIS 3.28

Download and install
~~~~~~~~~~~~~~~~~~~~

It can be installed on QGIS >= 3.28 adding the Plugin Repository to QGIS ``manage and install plugins``:
- flag ``show also experimental plugins``

.. image:: ./images/experimental.png
   :width: 500px

- add plugin repository

.. image:: ./images/addrepo.png
   :width: 500px

- edit repository and add `https://sztools.github.io/SZ/sz.xml <https://sztools.github.io/SZ/sz.xml>`_ (THIS REPOSITORY IS TEMPORARY)

.. image:: ./images/repodetail.png
   :width: 500px

or

cloning the `GitHub repository <https://github.com/SZtools/SZ-plugin>`_ or downloading it as zip file (and then unzipping it) and copying the ``sz_module`` folder in your local ``python/plugin`` folder (read `here <https://docs.qgis.org/3.10/en/docs/user_manual/plugins/plugins.html#core-and-external-plugins>`_ for more information).

Lunch QGIS 3.x, and abilitate the plugin from ``manage and install plugin/installed/sz_processing``

.. image:: ./images/install.png
   :width: 500px

or

cloning the `GitHub repository <https://github.com/SZtools/SZ-plugin>`_ or downloading it as zip file (and then unzipping it), and zip the folder ``sz_module`` to ``sz_module.zip``. Finally you can install the plugin by using the menu ``install from zip``.

.. image:: ./images/install.png
   :width: 500px

At the end you should have the SZ plugin in your processing toolbox

.. image:: ./images/gui.png
   :width: 300px

GUI
---

The functions are grouped into 3 categories:
* *Data preparation*
* *SI*
* *SI k-fold*
* *Classify SI*

*Data preparation* functions can be used for data pre-processing
*SI* functions run the statistic models for susceptibility, cross-validate by a simple random selection of train/test samples and evaluate the prediction capacity by ROC curves
*SI k-fold* functions run the statistic models for susceptibility, cross-validate by k-fold method and evaluate the prediction capacity by ROC curves
*Classify SI* functions allows to categorize the susceptibility index into *n* classes on the base of AUC maximization.

Input data of SI and SI k-fold functions
----------------------------------------

Input data for SI k-fold or SI functions should be a vector layer with a number of fields for independent variables and a field for the dependent variable classified binomially: 0 for absence, >0 for presence.

.. image:: ./images/use.png
   :width: 500px

Test
----

A dataset and QGIS project are available in `test <./test_data>`_ folder to test the plugin.

.. image:: ./images/test.png
   :width: 500px

.. image:: ./images/output.png
   :width: 500px

Third-part libraries and plugins used
-------------------------------------

* `Scikit-learn <https://scikit-learn.org/stable/index.html>`_
* `libpysal <https://pysal.org/libpysal/>`_

Tutorial
--------

video tutorial: https://www.youtube.com/watch?v=XpsiCkVF11s

Application
-----------

Titti G, Sarretta A, Lombardo L, Crema S, Pasuto A and Borgatti L (2022) Mapping Susceptibility With Open-Source Tools: A New Plugin for QGIS. Front. Earth Sci. 10:842425. doi: 10.3389/feart.2022.842425

`Referenced dataset <https://zenodo.org/record/6575572>`_

Publications
------------

*A few examples and references about applications*

Titti G, Sarretta A, Lombardo L, Crema S, Pasuto A and Borgatti L (2022) Mapping Susceptibility With Open-Source Tools: A New Plugin for QGIS. Front. Earth Sci. 10:842425. doi: 10.3389/feart.2022.842425

Titti, G., van Westen, C., Borgatti, L., Pasuto, A., & Lombardo, L. (2021). When Enough Is Really Enough? On the Minimum Number of Landslides to Build Reliable Susceptibility Models. Geosciences, 11(11), 469.

Titti, G., Borgatti, L., Zou, Q., Cui, P., & Pasuto, A. (2021). Landslide susceptibility in the Belt and Road Countries: continental step of a multi-scale approach. Environmental Earth Sciences, 80(18), 1-18. `10.1007/s12665-021-09910-1 <https://doi.org/10.1007/s12665-021-09910-1>`_

Titti, G., Borgatti, L., Zou, Q., Pasuto, A., 2019. Small-Scale landslide Susceptibility Assessment. The Case Study of the Southern Asia. Proceedings 30, 14. `10.3390/proceedings2019030014 <https://doi.org/10.3390/proceedings2019030014>`_

Presentations
-------------

*A list of presentations made about the plugin and its applications*

Titti, Giacomo, Sarretta, Alessandro, Crema, Stefano, Pasuto, Alessandro, & Borgatti, Lisa. (2020, March). Sviluppo e applicazione del plugin Susceptibility zoning per il supporto alla pianificazione territoriale. Zenodo. `10.5281/zenodo.3723353 <https://zenodo.org/record/3723353>`_

Credits
-------

Giacomo Titti, Alessandro Sarretta and Luigi Lombardo, Padova, November 2021

please cite as: Giacomo Titti, Alessandro Sarretta and Luigi Lombardo. (2021). CNR-IRPI-Padova/SZ: SZ plugin (Version v1.0). Zenodo.

Contacts
--------

If you have any problem, please write to giacomotitti@gmail.com or create new issue `here <https://github.com/SZtools/SZ-plugin/issues>`_
