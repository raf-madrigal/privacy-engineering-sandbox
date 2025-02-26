# GRAIL 


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Usage

### Installation

Install latest from the GitHub
[repository](https://gitlab2.mynt.xyz/data-office/ml-engineering/standard-libraries/grail):

``` sh
$ pip install https://oauth2:$GITLAB_TOKEN@gitlab2.mynt.xyz/data-office/ml-engineering/standard-libraries/grail.git
```

### Documentation

Documentation can be found hosted on this GitLab
[repository](https://gitlab2.mynt.xyz/data-office/ml-engineering/standard-libraries/grail)’s
[pages](https://gitlab2.mynt.xyz/data-office/ml-engineering/standard-libraries/grail).

## How to use

Fill me in please! Don’t forget code examples:

``` python
from grail.fairness.data.utils import create_biased_dataset

df = create_biased_dataset(100)
df.head()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | id  | age | loan_application_date | loan_type  | feature_x | target | gender | location |
|-----|-----|-----|-----------------------|------------|-----------|--------|--------|----------|
| 0   | 0   | 59  | 2016-08-15            | gcredit    | 30        | 0      | female | loc1     |
| 1   | 1   | 27  | 2014-05-08            | borrowload | 64        | 1      | male   | loc1     |
| 2   | 2   | 37  | 2017-04-18            | gcredit    | 87        | 0      | female | loc2     |
| 3   | 3   | 52  | 2014-11-15            | ggives     | 35        | 1      | male   | loc2     |
| 4   | 4   | 49  | 2017-01-29            | gloan      | 93        | 1      | male   | loc1     |

</div>

``` python
from grail.fairness.data.metrics import class_imbalance

df_col = df.gender
class_imbalance(df_col, risk_group="female")
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | feature | metric          | risk_group | metric_value |
|-----|---------|-----------------|------------|--------------|
| 0   | gender  | class_imbalance | female     | 0.6          |

</div>

## Developer Guide

### Setup

This package is built using [nbdev](https://nbdev.fast.ai/) and
[poetry](https://python-poetry.org/).

nbdev is used to develop the library code using jupyter notebooks while
poetry is used for dependency management.

It is recommended to develop in a jupyter environment like Jupyterhub.

Once you have a jupyter environment, create a new python environment for
grail.

#### poetry

To install package depdencies, first install poetry using the following
command

``` sh
    curl -sSL https://install.python-poetry.org | python3 -
```

Then, install the project dependencies by doing

``` sh
    poetry install
```

This will install the dependencies found in the `poetry.lock` file.

#### pre-commit

pre-commit allows us to run hooks or some steps to check our code before
we commit and push to the repository. Run

``` sh
pre-commit install
```

This will install our checkers which will run everytime you commit
changes to the code.

#### nbdev

If you are new to using `nbdev`, read
[this](https://nbdev.fast.ai/tutorials/tutorial.html) end-to-end example
on how to develop using nbdev.

Basically, `nbdev` allows us to develop our package code using
`Jupyter Notebooks`. This is really advantageous for data science
packages since you can test the output of your functions in a jupyter
cell and see it’s results visually in a notebook. When you are done
developing your code, `nbdev` converts your notebook code into *.py*
files for your python package distribution.

Also, `nbdev` allows you to have tests and documentation in the jupyter
notebooks you use to develop your modules.

Once, you have installed the project depedencies using `poetry`, nbdev
should already be installed in your environment.

Do the following command, to install it’s git hooks **(you only need to
do this once)**:

``` sh
nbdev_install_hooks
```

Once you are done, you can start contrubuting to the package.

Before pushing changes, remember to do

``` sh
nbdev_prepare
```

This will export your notebooks into python code, run your notebooks for
testing, and generate documentation for your code.

### Install grail in Development mode

``` sh
# make sure grail package is installed in development mode
$ pip install -e .

# make changes under nbs/ directory
# ...

# compile to have changes apply to grail
$ nbdev_prepare
```
