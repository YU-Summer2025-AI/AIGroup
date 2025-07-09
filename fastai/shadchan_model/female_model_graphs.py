import shap
import joblib
import matplotlib.pyplot as plt
import pandas as pd
import shap
from fastai.tabular.all import *
from sqlalchemy import create_engine, text
import joblib
y_names = [
    'avg_age',
    'avg_introvert', 
    'avg_sensor', 
    'avg_feeler', 
    'avg_athletic_fit',
    'avg_machmir', 
    'avg_just_jewish', 
    'avg_heimish', ]
cont_names = [
    'height',
    'age', 
    'introvert', 
    'sensor', 
    'feeler', 
    'perceiver',
    'athletic_fit', 
    'lean_slender', 
    'yeshivish', 
    'just_jewish', 
]


shap_values, X_small_full = joblib.load("shap_female.pkl")

mask = [not col.startswith("avg_") for col in X_small_full.columns]

X_small = X_small_full.loc[:, mask]
cont_names = list(X_small.columns)

shap_values = shap_values[:, mask, :]
target_names = y_names
target_indices = [y_names.index(name) for name in target_names]

fig, axes = plt.subplots(2, 4, figsize=(24, 12))
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