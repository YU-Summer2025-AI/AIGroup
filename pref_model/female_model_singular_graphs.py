import shap
import joblib
import matplotlib.pyplot as plt
import pandas as pd
import shap
from fastai.tabular.all import *
from sqlalchemy import create_engine, text
import joblib
engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/postgres")

sql_query = text("SELECT * FROM total_female")
with engine.connect() as conn:
    df = pd.read_sql(sql_query, conn) 
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
# traits model
shap_values_traits, X_traits = joblib.load("shap_female_traits.pkl")
feature_names_traits = X_traits.columns.tolist()
num_individuals = 8
indices = np.random.choice(X_traits.shape[0], num_individuals, replace=False)
fig, axes = plt.subplots(2, 4, figsize=(32, 14))
axes = axes.flatten()

for i, idx in enumerate(indices):
    ax = axes[i]
    plt.sca(ax)
    shap.summary_plot(
        shap_values_traits[idx:idx+1],
        X_traits.iloc[idx:idx+1],
        feature_names=feature_names_traits,
        plot_type="bar",
        show=False,
        class_names=trait_y_names
    )
    ax.tick_params(axis='y', labelsize=6)
    traits_member_id = df.iloc[idx]["female_id"]
    ax.set_title(f"Religion Model: ID {traits_member_id}", fontsize=12)
    ax.set_xlabel("mean(|SHAP value|)", fontsize=6)
    legend = plt.gca().get_legend()
    class_indices = np.where(np.abs(shap_values_traits[idx]).sum(axis=0) > 0)[0]  
    for i, text in enumerate(legend.get_texts()):
        if i not in class_indices:
            text.set_visible(False)
        else:
            text.set_fontsize(6)
            text.set_fontname('Arial')


plt.tight_layout(pad=4.0)
plt.subplots_adjust(left=0.08, wspace=0.6, hspace=0.4)
plt.show()

# religion model
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
shap_values_religion, X_religion = joblib.load("shap_female_religion.pkl")
feature_names_religion = X_religion.columns.tolist()
fig, axes = plt.subplots(2, 4, figsize=(32, 14))
axes = axes.flatten()

for i, idx in enumerate(indices):
    ax = axes[i]
    plt.sca(ax)
    shap.summary_plot(
        shap_values_religion[idx:idx+1],
        X_religion.iloc[idx:idx+1],
        feature_names=feature_names_religion,
        plot_type="bar",
        show=False,
        class_names=religion_y_names  
    )
    ax.tick_params(axis='y', labelsize=6)
    religion_member_id = df.iloc[idx]["female_id"]
    ax.set_title(f"Religion Model: ID {religion_member_id}", fontsize=12)
    ax.set_xlabel("mean(|SHAP value|)", fontsize=6)
    legend = plt.gca().get_legend()
    class_indices = np.where(np.abs(shap_values_religion[idx]).sum(axis=0) > 0)[0]  
    for i, text in enumerate(legend.get_texts()):
        if i not in class_indices:
            text.set_visible(False)
        else:
            text.set_fontsize(6)
            text.set_fontname('Arial')


plt.tight_layout(pad=4.0)
plt.subplots_adjust(left=0.08, wspace=0.6, hspace=0.4)
plt.show()
