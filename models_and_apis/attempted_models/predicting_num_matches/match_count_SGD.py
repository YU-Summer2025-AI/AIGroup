import pandas as pd
import numpy as np
import psycopg2
# import fastbook
# fastbook.setup_book()
# from fastbook import *
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset, random_split # Ensure DataLoader is from torch.utils.data
import torch # Keep this for general tensor operations
# import torch.optim as optim # ADD THIS
from torch.utils.data import TensorDataset, random_split
from sklearn.preprocessing import StandardScaler

class DeeperModel(nn.Module):
    def __init__(self, model_size):
        super().__init__()
        self.layer1 = nn.Linear(model_size, 100) # From input features to 100 hidden features
        self.layer2 = nn.Linear(100, 50)         # From 100 to 50 hidden features
        self.layer3 = nn.Linear(50, 1)            # From 50 to 1 output (num_matches)
        self.relu = nn.ReLU()                     # Non-linear activation function
        self.dropout = nn.Dropout(0.4)            # Regularization: randomly zero out 40% of neurons

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.dropout(x)  # Apply dropout after activation
        x = self.relu(self.layer2(x))
        x = self.dropout(x)  # Apply dropout again
        x = self.layer3(x)
        return x

def group_country(country):
    if country in ['United States', 'Canada']:
        return 'North America'
    elif country == 'Israel':
        return 'Israel'
    elif country in ['United Kingdom', 'France', 'Belgium']: # Add other European countries
        return 'Europe'
    else:
        return 'Other'

def create_feature_tensor(df_raw, target_col='num_matches'):
    # Make a copy to avoid modifying the original DataFrame
    df = df_raw.copy()

    # 1. Separate the target variable
    if target_col in df.columns:
        df = df.drop(columns=[target_col])

    # 2. Identify column types
    numerical_cols = df.select_dtypes(include=np.number).columns.tolist()

    # Define your multi-value and single-value categorical columns
    multi_value_cols = [
        'preference_regarding_ethnicity', 'body_type_preference', 'desired_female_hc',
        'desired_female_dress', 'acceptable_religious_orientation', 'acceptable_aliyah_responses',
        'acceptable_kosher_observance', 'acceptable_family_religious_background',
        'desired_torah_study', 'jewish_education_preference'
    ]

    # All other object/category columns are single-value
    all_categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    single_value_cols = [col for col in all_categorical_cols if col not in multi_value_cols]

    # --- Feature Processing Pipeline ---
    processed_dfs = []

    # A. Process Numerical Columns (Scaling)
    if numerical_cols:
        scaler = StandardScaler()
        df_numerical = pd.DataFrame(scaler.fit_transform(df[numerical_cols]),
                                    columns=numerical_cols,
                                    index=df.index)
        processed_dfs.append(df_numerical)

    # B. Process Single-Value Categorical Columns (One-Hot Encoding)
    if single_value_cols:
        df_single_cat = pd.get_dummies(df[single_value_cols], drop_first=True, dtype=int)
        processed_dfs.append(df_single_cat)

    # C. Process Multi-Value Categorical Columns (Multi-Hot Encoding)
    for col in multi_value_cols:
        if col in df.columns:
            # Your simplified function is good for one-at-a-time processing
            multi_hot_df = one_hot_encode_multi_value_column_simplified(df, col)
            processed_dfs.append(multi_hot_df)

    # D. Combine all processed features
    final_df = pd.concat(processed_dfs, axis=1)

    # Ensure all column names are strings (PyTorch requirement)
    final_df.columns = final_df.columns.astype(str)

    return torch.from_numpy(final_df.values).float()





def one_hot_encode_multi_value_column_simplified(df, column_name, delimiter=';'):
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

    temp_list_col = f'{column_name}_list_temp'
    df[temp_list_col] = df[column_name].astype(str).apply(
        lambda x: [item.strip() for item in x.split(delimiter) if item.strip()]
    )
    df_exploded = df[[temp_list_col]].explode(temp_list_col)
    df_exploded = df_exploded[df_exploded[temp_list_col] != '']
    dummies = pd.get_dummies(df_exploded[temp_list_col], prefix=column_name)
    final_encoded_df = dummies.groupby(dummies.index).sum()
    df.drop(columns=[temp_list_col], inplace=True)

    return final_encoded_df

def get_scaled_data(df):
    numerical_cols = df.select_dtypes(include=['number']).columns
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    return df

def encode_df_to_tensor(df_without_num_matches):
    df_encoded = one_hot_encode_multi_value_column_simplified(df_without_num_matches, 'preference_regarding_ethnicity')
    df_encoded = one_hot_encode_multi_value_column_simplified(df_without_num_matches, 'body_type_preference')
    df_encoded = one_hot_encode_multi_value_column_simplified(df_without_num_matches, 'desired_female_hc')
    df_encoded = one_hot_encode_multi_value_column_simplified(df_without_num_matches, 'desired_female_dress')
    df_encoded = one_hot_encode_multi_value_column_simplified(df_without_num_matches, 'acceptable_religious_orientation')
    df_encoded = one_hot_encode_multi_value_column_simplified(df_without_num_matches, 'acceptable_aliyah_responses')
    df_encoded = one_hot_encode_multi_value_column_simplified(df_without_num_matches, 'acceptable_kosher_observance')
    df_encoded = one_hot_encode_multi_value_column_simplified(df_without_num_matches, 'acceptable_family_religious_background')
    df_encoded = one_hot_encode_multi_value_column_simplified(df_without_num_matches, 'desired_torah_study')
    df_encoded = one_hot_encode_multi_value_column_simplified(df_without_num_matches, 'jewish_education_preference')

    df_encoded = pd.get_dummies(df_without_num_matches,
                                columns=df_without_num_matches.select_dtypes(include=['object', 'category']).columns,
                                drop_first=True,
                                dtype=int)
    return torch.from_numpy(df_encoded.values).float()

def get_training_and_validation_splits(dataset_tensor):
    train_size = int(0.8 * len(dataset_tensor))
    val_size = len(dataset_tensor) - train_size
    generator = torch.Generator().manual_seed(42)
    return random_split(dataset_tensor, [train_size, val_size], generator=generator)

# loss_func = nn.L1Loss()
loss_func = nn.HuberLoss(delta=1.0)
# loss_func = nn.MSELoss()

def calc_grad(details, num_matches, model):
    preds = model(details) #goes to linear model and gives a number based on the weights
    loss = loss_func(preds.squeeze(), num_matches)
    loss.backward()

def train_epoch(opt, model, dl):
    for details,num_matches in dl:
        calc_grad(details, num_matches, model)
        opt.step()
        opt.zero_grad()


def validate_epoch(model, valid_dl, original_targets_for_dl, epoch_num):  # Added epoch_num
    model.eval()
    maes = []
    accuracies = []  # ADDED BACK: To keep track of your custom accuracy

    with torch.no_grad():
        batch_idx = 0
        for details, log_num_matches in valid_dl:
            log_preds = model(details)
            original_scale_preds = torch.expm1(log_preds)

            start_idx = batch_idx * valid_dl.batch_size
            end_idx = start_idx + len(details)
            original_scale_targets = original_targets_for_dl[start_idx:end_idx]

            # --- MAE Calculation (as before) ---
            batch_mae = loss_func(original_scale_preds.squeeze(), original_scale_targets.squeeze()).item()
            maes.append(batch_mae)

            # # --- ADDED BACK: Accuracy Calculation ---
            # # Use the same original scale predictions and targets to calculate accuracy
            # absolute_diff = torch.abs(original_scale_preds.squeeze() - original_scale_targets.squeeze())
            # # I'm using your last known threshold of 20. You can change this value.
            # correct = (absolute_diff <= 20)
            # accuracies.append(correct.float().mean().item())
            # # ------------------------------------
            absolute_diff = torch.abs(original_scale_preds.squeeze() - original_scale_targets.squeeze())
            # Avoid division by zero for targets that are 0, though your query already prevents this.
            relative_error = absolute_diff / (original_scale_targets.squeeze() + 1e-6)
            # Let's say "correct" is a prediction within 20% of the actual value
            correct = (relative_error <= 0.2)
            accuracies.append(correct.float().mean().item())

            batch_idx += 1

    model.train()
    avg_mae = round(torch.tensor(maes).mean().item(), 4)
    avg_accuracy = round(torch.tensor(accuracies).mean().item(), 4)  # ADDED BACK

    # UPDATED PRINT STATEMENT: Now includes all three metrics
    print(f"Epoch {epoch_num} - Validation MAE: {avg_mae}, Validation Accuracy: {avg_accuracy}")

    #


def train_model(opt, model, dl, valid_dl, original_val_targets, epochs):
    for i in range(epochs):
        model.train()  # Set model to training mode
        for details, log_num_matches in dl:
            # The training loss is calculated in log space, which is fine and stable
            preds = model(details)
            loss = loss_func(preds, log_num_matches)  # targets are log-transformed
            loss.backward()
            opt.step()
            opt.zero_grad()

        # MODIFIED: Pass the current epoch number to the validation function.
        # The print statement is now handled inside validate_epoch.
        validate_epoch(model, valid_dl, original_val_targets, i + 1)

def main():
    conn = None # Initialize conn to None
    try:
        # Establish a connection
        conn = psycopg2.connect(
            host="localhost",
            database="SYAS",
            user="admin",
            password="admin",
            port="5432"
        )

        sql_query = """
                        SELECT
                            ethnicity,
                            preference_regarding_ethnicity, --explode
                            country,
                            my_marriage_status,
                            want_additional_children,
                            can_marry_cohen,
                            cohen,
                            willing_to_relocate,
                            desired_marital_status,
                            minimum_education_level,
                            acceptable_for_match_to_have_children,

                            gender,
                            age,
                            height_inches,
                            body_type,
                            eye_color,
                            hair_color,
                            mental_physical_disability,
                            how_active_are_you,
                            body_type_preference, --explode

                            religious_orientation,
                            family_religious_background,
                            female_hc,
                            desired_female_hc, --explode
                            female_dress,
                            desired_female_dress, --explode
                            male_hc,
                            kosher,
                            frequency_of_tefilah,
                            male_shul_attendance,
                            torah_study,
                            watching_tv,
                            going_out_to_movies,
                            watching_movies_at_home,
                            secular_education,
                            jewish_education,
                            study_in_israel,
                            plan_to_aliya,
                            acceptable_religious_orientation, --explode
                            acceptable_aliyah_responses, --explode
                            acceptable_kosher_observance, --explode
                            family_relgious_background AS acceptable_family_religious_background, --explode
                            desired_torah_study, --explode
                            jewish_education_preference, --explode

                            profession,
                            introvert_extravert,
                            sensor_intuitive,
                            thinker_feeler,
                            judger_perceiver,
                            political_orientation,

                            num_matches,
                            site
                        FROM members
                        WHERE num_matches > 0
                        AND height_inches IS NOT NULL;
                    """
        # sql_query = """
        #     SELECT
        #         gender,
        #         age,
        #         height_inches,
        #         body_type,
        #         country, -- Keep for now, we will handle it next
        #         profession, -- Keep for now
        #         religious_orientation,
        #         family_religious_background,
        #         kosher,
        #         torah_study,
        #         secular_education,
        #         want_additional_children,
        #         num_matches
        #     FROM members
        #     WHERE num_matches > 0
        #     AND height_inches IS NOT NULL;
        # """
        df = pd.read_sql(sql_query, conn)
        df['age_squared'] = df['age'] ** 2

        df['country_group'] = df['country'].apply(group_country)
        df = df.drop(columns=['country'])  # Drop the original
        
        num_matches_series = df['num_matches']
        df_without_num_matches = df.drop(columns=['num_matches'])

        # --- FIX: LOG-TRANSFORM THE TARGET VARIABLE ---
        num_matches_series = df['num_matches']
        log_num_matches_series = np.log1p(num_matches_series)  # log(x+1)
        # ----------------------------------------------

        # data scaling
        df_scaled_data = get_scaled_data(df_without_num_matches)

        log_num_matches_tensor = torch.from_numpy(log_num_matches_series.values).float().unsqueeze(1)
        tensor = create_feature_tensor(df_scaled_data)

        # make training and validation sets and dataloaders
        dataset = TensorDataset(tensor, log_num_matches_tensor)
        train_dataset, val_dataset = get_training_and_validation_splits(dataset)

        # --- We need the original validation targets for reporting ---
        val_indices = val_dataset.indices
        original_val_targets = torch.from_numpy(num_matches_series.iloc[val_indices].values).float()
        # -----------------------------------------------------------

        dl = DataLoader(train_dataset, batch_size=256)
        valid_dl = DataLoader(val_dataset, batch_size=256)

        model_size = tensor.shape[1] #num params
        print(f"Model size: {model_size}")

        # This model: Validation MAE: 53.0399, Validation Accuracy: 0.5918 Epoch 60 - 53.0399 before overfitting
        # lr = .01
        # linear_model = nn.Linear(model_size, 1)
        # opt = optim.SGD(linear_model.parameters(), lr)
        # train_model(opt, linear_model, dl, valid_dl, original_val_targets, 200)

        # This model: Validation MAE: 53.3348, Validation Accuracy: 0.5833 Epoch 115 - 53.3348 before overfitting
        # linear_model = nn.Linear(model_size, 1)
        # opt = optim.AdamW(linear_model.parameters(), lr=1e-3, weight_decay=0.01)
        # train_model(opt, linear_model, dl, valid_dl, 200)

        model = DeeperModel(model_size)
        opt = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
        train_model(opt, model, dl, valid_dl, original_val_targets, 100)

    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL database: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if conn:
            conn.close()
            print("\nPostgreSQL connection closed.")

main()