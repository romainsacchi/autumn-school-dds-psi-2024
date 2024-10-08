# INSTRUCTIONS BEFORE ARRIVAL

Please follow the below instructions before arriving at the course.
Ideally, do this **at least one week before the course starts**, so
that you have time to ask/write us questions if you encounter any issues.

# WORK ON SERVERS vs. LOCAL MACHINES

During the course, we will work on servers provided by Départ de Sentier.
This allows us to have **a consistent environment for all participants**.
However, we recommend that you install the necessary software on your
local machine as well, so that you can continue working on the exercises
after the course and during group projects from Thursday to Friday.

# ANACONDA AND GIT

We ask the participants to download and install Anaconda (or the 
Python environments manager of your choice) and Git 
before the course:

- Anaconda: https://www.anaconda.com/products/distribution
- Git: https://git-scm.com/downloads

We recommend using homebrew to install Git on Mac:

```bash
  brew install git
```

For Windows users, you can download teh Git installer from the link above (you most likely
need the 64-bit version).

## Change the Anaconda solver

Once you have installed Anacoda on your computer, you may consider installing 
the `libmamba` solver in conda, for faster environment resolution.
Open the terminal (Anaconda terminal in Windows, or Terminal on Mac) 
and run the following commands:

```bash
  conda install -n base conda-libmamba-solver
  conda config --set solver libmamba
```

## Clone this repository

Using your Windows/Mac terminal, navigate to the folder where you want 
to store the course material.For example, you can create a folder 
called `autumn-school-2024` in your `Documents` folder. To navigate to 
the `Documents` folder, you can run the following command:

```bash
  cd Documents
```

To go back to the previous folder, you can run the following command:

```bash
  cd ..
```

If you want to create a new folder, you can run the following command:

```bash
  mkdir autumn-school-2024
```

Once you are in the folder of your choice, you can **clone** this Github repository 
using Git onto your computer by running the following command in your terminal:

```bash
  git clone https://github.com/romainsacchi/autumn-school-dds-psi-2024.git
```

You can now navigate to the `autumn-school-dds-psi-2024` folder and 
access its content on your computer.

## Environments setup

When you will do exercises on your computer, you will use a number of libraries
that are not installed by default in Anaconda. To make sure you have all the
necessary libraries, we will create Anaconda **environments** for you, using
**recipes** that we have prepared.

We have prepared three recipes which install three different environments:
- `bw25_env_xxx.yaml`: it will install the `brightway` library as well as Activity Browser
- `wurst_env_xxx.yaml`: it will install the `wurst` library and its dependencies
- `premise_env.yaml`: it will install the `premise` library and its dependencies

After running the recipe files, you will have three environments on your computer:
- `wurst`
- `premise`
- `bw25`

Using your terminal, navigate to the `environments` folder of the repository:

```bash
  cd autumn-school-dds-psi-2024/envs
```

Then, run the following command to create the `wurst` environment:

If you use Windows or Mac with an Intel processor:

```bash
  conda env create -f wurst_env_win64.yaml
```

If you use Mac with an Mx processor:

```bash
  conda env create -f wurst_env_osxARM.yaml
```

This will create a conda environment called `wurst` with all the required dependencies.

Then, run the following command to create the `premise` environment:

```bash
  conda env create -f premise_env.yaml
```

This will create a conda environment called `premise` with all the required dependencies.

Finally, run the following command to create the `bw25` environment:

On Windows or Mac with an Intel processor:


```bash
  conda env create -f bw25_env_win64.yaml
```

On a Mac with an Mx processor:

```bash
  conda env create -f bw25_env_osxARM.yaml
```

This will create a conda environment called `bw25` with all the required dependencies.

You can check that the environments have been created by running the following command:

```bash
  conda env list
```

You should see the three environments listed in the terminal (plus the `base` environment).

You can activate an environment by running the following command:

```bash
  conda activate wurst
```

and check the installed packages by running:

```bash
  conda list
```

## Ecoinvent database

Also, please acquire credentials (username and password) to 
download the [ecoinvent](https://ecoinvent.org) database.
We will be using the ecoinvent 3.10 database for the course.

# IDE

We recommend using **PyCharm** or **Visual Studio Code** as an IDE for the course.
Both are free (Community edition) and have a lot of features that will 
help you during the course.



