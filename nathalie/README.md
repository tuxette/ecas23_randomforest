# Welcome to Nathalie's subrepository!

Welcome to this repository! I will regularly update this README file to let you
know when some of the materials that I am preparing for this class is ready. 
You will also find detailed installation instructions for the practical sessions
here (maybe, if I'm inspired) as advices to be sure to be able to run the code 
prepared for these sessions during the class.

Do not hesitate to contact me (preferentially **before** the beginning of the
class) using the contact information available on my 
[professional website](http://www.nathalievialaneix.eu/).

TD;DR:

1. Clone this github repository on your computer

2. Download the course material as described in the README files of the directories `*/class/`

3. Download the data as described in the README files of the directories `*/data/`

4. Install R and R packages `ggplot2`, `reshape2`, and `SISIR`

5. Install Python and the Python librairies `matplotlib`, `numpy`, `pyts`, `session_info`, and `sklearn`

## Material

My class will cover 2-3 topics, including:

* **random forest for functional data analysis** (e.g., mostly time series)
  * [slides (theoretical part)](http://www.nathalievialaneix.eu/doc/pdf/2023-10-09_vialaneix_ECASSFdS2023-FDA.pdf) 
  are ready! You are welcome to download them. Minor changes can be introduced 
  later in these slides. The last version is of *September 7th, 2023*.
  * practical part on "Using random forest for functional data with time-series 
  random forest and BOSS random forest": 
  [Analysis of the GunPoint dataset](https://colab.research.google.com/drive/1PXkbIhrC0YkJ2UoWJe2edWsm6NoGHJhs?usp=sharing) 
  shared through [Google Colab](https://colab.research.google.com). This file is
  a Jupyter notebook also available in the directory `fda/practical` of this 
  repository. You are free to either: i) use it directly on Google Colab by 
  creating a copy (File / Save a copy in drive), ii) use it on your own computer
  (be sure to have the necessary Python libraries installed), or iii) use it in 
  a RStudio cloud account. The last version is of *September 7th, 2023*.
  * practical part on "Interval selection for random forest with functional 
  data": <a href="/doc/html/truffle_analysis.html">Truffle analysis with random 
  forest</a>. This file is the HTML output of a Quarto file (i.e., Rmarkdow) and
  its source code is available in the directory `/fda/practical` of this 
  repository. You are free to either: i) directly use this file and copy/paste 
  the code in an R terminal, ii) use directly the Quarto file on your own 
  computer (make sure to have downloaded the data and installed the packages), 
  or iii) use the Quarto file in a RStudio cloud account. Data for this 
  practical session have to be downloaded as described in README file of the 
  directory `fda/data`. The last version is of *September 7th, 2023*.
  
* * **random forest for network inference (in biology)**
  * [slides (theoretical part)](http://www.nathalievialaneix.eu/doc/pdf/2023-10-09_vialaneix_ECASSFdS2023-network.pdf)
  are ready! Your are welcome to download them. Minor changes can be introduced
  later in these slides. The last version is of *September 15th, 2023*.
  
## Technical information

I am using Ubuntu 22.04 LTS (xubuntu distribution) and can probably help you
install R and Python packages and librairies on this distribution, on linux, or
even maybe on Mac, providing that you send me complete description of the errors
(screenshots are welcome).

- *Python configuration*: On my computer, I am using Python 3.10.12 with Jupyter
notebook (6.4.12). The following librairies are required for the notebooks 
(versions are given for the records but the Google Colab versions are not the 
same and the notebook works perfectly):
  - `matplotlib`          3.6.2
  - `numpy`               1.23.5
  - `pyts`                0.13.0
  - `session_info`        1.0.0
  - `sklearn`             1.3.0
- *R configuration*: I am using R 4.3.1 in RStudio (any recent version should 
work). The following packages are required for the Quarto files:
  - `ggplot2`             3.4.3
  - `reshape2`            1.4.4
  - `SISIR`               0.2.2
  
For **R**, the [`renv`](https://rstudio.github.io/renv/articles/renv.html) configuration file is provided. If you want to use `renv`, the **R** command line `renv::init()` using the "Restore" option should properly install all the required packages for the practicals.

  
Information provided on this page is duplicated at [http://www.nathalievialaneix.eu/teaching/ecas_sfds_rf.html].
  
