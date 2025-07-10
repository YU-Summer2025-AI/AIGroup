import shap
import joblib
import matplotlib.pyplot as plt
import pandas as pd
import shap
from fastai.tabular.all import *
from sqlalchemy import create_engine, text
import joblib

trait_y_names = [
    'avg_lean_slender',
    'avg_introvert', 
    'avg_sensor', 
    'avg_feeler', 
    'avg_athletic_fit',
    'avg_proportional', 
    'avg_firm_toned', 
    'avg_perceiver', 
    'avg_large_broad_build',
    'avg_medium_build',
    'avg_a_few_extra_pounds',
    'avg_age',]

religion_y_names = [
    'avg_heimish',
    'avg_traditional',
    'avg_middle_of_road',
    'avg_strickly_frum',
    'avg_machmir',
    'avg_conservadox',
    'avg_chassidish',
    'avg_conservative',
    'avg_m_yeshivish',
    'avg_spiritual_but_not_religious',
    'avg_m_o_liberal',
    'avg_lubavitch',
    'avg_just_jewish',
    'avg_reform',
    'avg_yeshivish',
]
#trait graph
shap_values, X_small_full = joblib.load("shap_female_religion.pkl")
mask = [not col.startswith("avg_") for col in X_small_full.columns]

X_small = X_small_full.loc[:, mask]
cont_names = list(X_small.columns)

shap_values = shap_values[:, mask, :]
target_names = trait_y_names
target_indices = [trait_y_names.index(name) for name in target_names]

fig, axes = plt.subplots(3, 4, figsize=(24, 16))
axes = axes.flatten()

for i, ax in enumerate(axes):
    plt.sca(ax)
    shap_values_target = shap_values[:, :, target_indices[i]]
    shap.summary_plot(
        shap_values_target,
        X_small,
        feature_names=cont_names,
        show=False,
        plot_type="dot",
        plot_size=(None)
    )
    plt.gca().tick_params(axis='y', labelsize=6)
    ax.set_title(f"SHAP for {target_names[i]}")

plt.tight_layout(pad = 3.0)
plt.subplots_adjust(wspace=0.5, hspace=0.4)
plt.show()


# religion graph
shap_values, X_small_full = joblib.load("shap_female_religion.pkl")
mask = [not col.startswith("avg_") for col in X_small_full.columns]

X_small = X_small_full.loc[:, mask]
cont_names = list(X_small.columns)

shap_values = shap_values[:, mask, :]
target_names = religion_y_names
target_indices = [religion_y_names.index(name) for name in target_names]

fig, axes = plt.subplots(3, 5, figsize=(24, 16))
axes = axes.flatten()

for i, ax in enumerate(axes):
    plt.sca(ax)
    shap_values_target = shap_values[:, :, target_indices[i]]
    shap.summary_plot(
        shap_values_target,
        X_small,
        feature_names=cont_names,
        show=False,
        plot_type="dot",
        plot_size=(None)
    )
    plt.gca().tick_params(axis='y', labelsize=6)
    ax.set_title(f"SHAP for {target_names[i]}")

plt.tight_layout(pad = 3.0)
plt.subplots_adjust(wspace=0.5, hspace=0.4)
plt.show()