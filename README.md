
# Companion repository for ECAS-SFdS 2023 school

Welcome to the ECAS-SFdS 2023 school **Random forests: basics,
extensions and applications**.

In this repository, you will find all the documents associated to the
school and notably the different files needed for practicals sessions.
There is one folder per speaker.

*NEWS*:

- Nathalie’s material for the school is ready. Check instructions in
  `nathalie/README.md`!

*INSTRUCTIONS*:

Here is some tasks that we recommend you to perform before the school
(the main reason is that the internet speed available there could be
quite moderate):

1.  Clone this github repository on your computer by using the green
    button **\<\> Code** (for installation/use of git you can follow
    this [Happy Git with
    R](https://happygitwithr.com/install-git.html)). You can also
    download the ZIP archive of the repository (but in this case you
    will have to re-download it in case of update)

2.  Download the courses materials as described in the different folders

3.  Download the practicals materials and/or data as described in the
    different folders

4.  **Install R** (<https://cloud.r-project.org/>) and the following **R
    packages** (we recommend the use of the [RStudio
    IDE](https://posit.co/download/rstudio-desktop/)):

    - `ggplot2`
    - `grf`
    - `mlbench`
    - `randomForest`
    - `randomForestSRC`
    - `ranger`
    - `reshape2`
    - `SISIR`
    - `RLT` [GitHub Version 4.2.5](https://github.com/teazrq/RLT)

    you can use the following commands to do that:

    ``` r
    install.packages(c("ggplot2", "grf", "mlbench", "randomForest",
                       "randomForestSRC", "ranger", "reshape2", "SISIR"))
    remotes::install_github("teazrq/RLT")
    ```

    for further information and in case of issues of installation of the
    `RLT` package, follow [Install the RLT
    package](https://teazrq.github.io/random-forests-tutorial/rlab/basics/packages.html#Install_the_RLT_Package).

5.  **Install Python** and the following **Python libraries**:

    - `matplotlib`
    - `numpy`
    - `pyts`
    - `session_info`
    - `sklearn`

**Alternatively**, you can use cloud solutions, which prevent you from
installing R or Python on your computer and can also help you resolve
some installation issues:

- [Posit cloud](https://posit.cloud/) for which you **need** to create a
  **Posit account**

- [Google Colab](https://colab.research.google.com/) for which you
  **need** a **Google account**

You may still have to install the different packages/libraries once
you’re logged in (depending of the type of document/project shared by
the speakers).
