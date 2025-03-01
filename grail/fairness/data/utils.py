"""This module contains utilitiy functions for the data fairness module"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/01_fairness_data_utils.ipynb.

# %% auto 0
__all__ = ['draw', 'apply_bias', 'create_biased_dataset', 'remark_spiel_generator']

# %% ../../../nbs/01_fairness_data_utils.ipynb 3
import numpy as np
import pandas as pd
from numpy.random import choice
import datetime


def draw(list_of_candidates: list, probability_distribution: list):
    """Function for choosing a random value given a list of valid values and a probability distribution."""
    number_of_items_to_pick = 1
    return choice(
        list_of_candidates, number_of_items_to_pick, p=probability_distribution
    )[0]


def apply_bias(
    x: pd.Series, choices: list, positive_dist: list, negative_dist: list
) -> any:
    """Function for creating a biased feature by prioritizing an advantaged class over all other classes given a probability distribution."""
    if x["target"] == 1:
        return draw(choices, positive_dist)

    return draw(choices, negative_dist)


def create_biased_dataset(df_len: int = 100) -> pd.DataFrame:
    """
    Compute class imbalance.

    Parameters
    ----------
    df_len
        the size of the desired dataset

    Returns
    -------
    pd.DataFrame
        the biased dataset
    """
    df = pd.DataFrame(
        {
            "id": np.arange(0, df_len, 1),
            "age": np.random.randint(18, 60, df_len),
            "loan_application_date": [
                np.random.choice(
                    pd.date_range(
                        datetime.datetime(2013, 1, 1), datetime.datetime(2020, 1, 3)
                    )
                )
                for i in range(df_len)
            ],
            "loan_type": [
                np.random.choice(["gloan", "gcredit", "ggives", "borrowload"])
                for i in range(df_len)
            ],
            "feature_x": np.random.randint(20, df_len, df_len),
            "target": [draw([1, 0], [0.8, 0.2]) for i in range(df_len)],
        }
    )
    df["gender"] = df.apply(
        apply_bias,
        choices=["male", "female"],
        positive_dist=[0.95, 0.05],
        negative_dist=[0.1, 0.9],
        axis=1,
    )
    df["location"] = df.apply(
        apply_bias,
        choices=["loc1", "loc2", "loc3"],
        positive_dist=[0.5, 0.3, 0.2],
        negative_dist=[0.2, 0.4, 0.4],
        axis=1,
    )

    return df

# %% ../../../nbs/01_fairness_data_utils.ipynb 6
def remark_spiel_generator(feature_name: str, group: str, metric_name: str, exceeds_flag: bool, lower_bound: float=None, upper_bound: float=None, threshold: float=None) -> str:
    """
    Generate a remarks spiel for a fairness data metric based on a given threshold. Choose between supplying a lower and upper bound threshold or just a single threshold.

    Parameters
    ----------
    feature_name
        feature column name
    group
        underpriviledged group name
    metric_name
        fairness data metric name
    exceeds_flag
        flag to tell if metric exceeded the thresholds or not
    lower_bound
        lower bound of the threshold
    upper_bound
        upper bound of the threshold
    threshold
        threshold if lower and upper bound is not applicable.

    Returns
    -------
    str
        the generated remarks spiel
    """
    if lower_bound or upper_bound:
        assert lower_bound and upper_bound, "Please provide both lower and upper bounds"
        assert threshold is None, "Please choose between lower and upper bounds or threshold"
        exceeds_spiel = f"Group {group} of Feature {feature_name} exceeded the {metric_name} threshold of {lower_bound} and {upper_bound}"
        
    if threshold:
        assert lower_bound is None and upper_bound is None, "Please choose between lower and upper bounds or threshold"
        exceeds_spiel = f"Group {group} of Feature {feature_name} exceeded the {metric_name} threshold of {threshold}"

    spiel_map = {
        True: exceeds_spiel,
        False: "Acceptable"
    }
    return spiel_map[exceeds_flag]
