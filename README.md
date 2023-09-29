
# Companion repository for ECAS-SFdS 2023 school

Welcome to the ECAS-SFdS 2023 school **Random forests: basics,
extensions and applications**.

In this repository, you will find all the documents associated to the
school and notably the different files needed for practicals sessions.
There is one folder per speaker.

*NEWS*:

- Nathalie’s material for the school is ready. Check instructions in
  `nathalie/README.md`!
- Robin's material for the school is ready. Check description in
`robin/README.md`!

*INSTRUCTIONS*:

Here is some tasks that we recommend you to perform before the school
(the main reason is that the internet speed available there could be
quite moderate):

1.  Clone this github repository on your computer by using the green
    button **\<\> Code** (for installation/use of git you can follow
    this [Happy Git with
    R](https://happygitwithr.com/install-git.html)). You can also
    download the ZIP archive of the repository (but in this case you
    will have to re-download it in case of an update).

2.  Download the courses materials as described in the different folders.

3.  Download the practicals materials and/or data as described in the
    different folders.

4.  **Install R** (<https://cloud.r-project.org/>) and the following **R
    packages** (we recommend the use of the [RStudio
    IDE](https://posit.co/download/rstudio-desktop/)):

    - `ggplot2`
    - `grf`
    - `igraph`
    - `mlbench`
    - `PRROC`
    - `randomForest`
    - `randomForestSRC`
    - `ranger`
    - `reshape2`
    - `rfPermute`
    - `SISIR`
    - `GENIE3` (BioConductor)
    - `RLT` [GitHub Version 4.2.5](https://github.com/teazrq/RLT)

    you can use the following commands (from within R) to do that:

    ``` r
    install.packages(c("ggplot2", "grf", "igraph", "mlbench", "PRROC", "randomForest", "randomForestSRC",
    "ranger", "reshape2",  "rfPermute", "SISIR", "BiocManager", "remotes"))
    BiocManager::install("GENIE3")                   
    remotes::install_github("teazrq/RLT")
    ```

    for further information and in case of issues of installation of the
    `RLT` package, follow [Install the RLT
    package](https://teazrq.github.io/random-forests-tutorial/rlab/basics/packages.html#Install_the_RLT_Package).
    
    On linux, some system dependencies (C++ librairies) might be needed too.

5.  **Install Python** (we recommend [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) or [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html) and the following **Python libraries**:

    - `matplotlib`
    - `numpy`
    - `pandas
    - `pyts`
    - `session_info`
    - `sklearn`
    - `rfpimp`
    - `xgboost
    
    you can use the following commands (from a terminal on Linux/MacOS or from 'Anaconda prompt', accessible from the Start menu, on Windows) to do that:
    
    ``` bash
    pip install matplotlib numpy pandas pyts session_info sklearn rfpimp xgboost
    ```

**Alternatively**, you can use cloud solutions, which prevent you from
installing R or Python on your computer and can also help you resolve
some installation issues:

- [Posit cloud](https://posit.cloud/) for which you **need** to create a
  **Posit account** (please note that the free account might not be sufficient 
  for all practical sessions)

- [Google Colab](https://colab.research.google.com/) for which you
  **need** a **Google account**

You may still have to install the different packages/libraries once
you’re logged in (depending of the type of document/project shared by
the speakers). We recommend that you do it before the class has started.
