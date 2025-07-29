import pandas as pd
import numpy as np

def add_rejection_products(df_matches: pd.DataFrame) -> pd.DataFrame:
    epsilon = 1e-6
    df_matches['male_rejects_female_product_physical_look'] = (df_matches['male_male_reason_rejecting_count_physical_look'] + 1) * \
                                                              (df_matches['female_female_rejection_count_physical_look']  + 1)
    df_matches['male_rejects_female_product_physical_look'] = np.log(np.log(df_matches['male_rejects_female_product_physical_look'] + epsilon))


    df_matches['female_rejects_male_product_physical_look'] = (df_matches[
                                                                   'female_female_reason_rejecting_count_physical_look'] + 1) * \
                                                              (df_matches[
                                                                   'male_male_rejection_count_physical_look'] + 1)
    df_matches['female_rejects_male_product_physical_look'] = np.log(np.log(df_matches['female_rejects_male_product_physical_look']+ epsilon))


    df_matches['female_rejects_male_product_null'] = (df_matches[
                                                                   'female_female_reason_rejecting_count_null'] + 1) * \
                                                              (df_matches[
                                                                   'male_male_rejection_count_null'] + 1)
    df_matches['female_rejects_male_product_null'] = np.log(np.log(df_matches['female_rejects_male_product_null']+ epsilon))


    df_matches['female_rejects_male_product_other'] = (df_matches[
                                                                   'female_female_reason_rejecting_count_other'] + 1) * \
                                                              (df_matches[
                                                                   'male_male_rejection_count_other'] + 1)
    df_matches['female_rejects_male_product_other'] = np.log(np.log(df_matches['female_rejects_male_product_other']+ epsilon))


    df_matches['male_rejects_female_product_other'] = (df_matches[
                                                                   'male_male_reason_rejecting_count_other'] + 1) * \
                                                              (df_matches[
                                                                   'female_female_rejection_count_other'] + 1)
    df_matches['male_rejects_female_product_other'] = np.log(np.log(df_matches['male_rejects_female_product_other']+ epsilon))


    df_matches['male_rejects_female_product_null'] = (df_matches[
                                                                   'male_male_reason_rejecting_count_null'] + 1) * \
                                                              (df_matches[
                                                                   'female_female_rejection_count_null'] + 1)
    df_matches['male_rejects_female_product_null'] = np.log(np.log(df_matches['male_rejects_female_product_null']+ epsilon))


    df_matches['male_rejects_female_product_personality'] = (df_matches[
                                                                   'male_male_reason_rejecting_count_personality'] + 1) * \
                                                              (df_matches[
                                                                   'female_female_rejection_count_personality'] + 1)
    df_matches['male_rejects_female_product_personality'] = np.log(np.log(df_matches['male_rejects_female_product_personality']+ epsilon))


    df_matches['male_rejects_female_product_know_already'] = (df_matches[
                                                                   'male_male_reason_rejecting_count_know_already'] + 1) * \
                                                              (df_matches[
                                                                   'female_female_rejection_count_know_already'] + 1)
    df_matches['male_rejects_female_product_know_already'] = np.log(np.log(df_matches['male_rejects_female_product_know_already']+ epsilon))


    df_matches['male_rejects_female_product_too_religious'] = (df_matches[
                                                                   'male_male_reason_rejecting_count_too_religious'] + 1) * \
                                                              (df_matches[
                                                                   'female_female_rejection_count_too_religious'] + 1)
    df_matches['male_rejects_female_product_too_religious'] = np.log(np.log(df_matches['male_rejects_female_product_too_religious']+ epsilon))


    df_matches['male_rejects_female_product_age'] = (df_matches[
                                                                   'male_male_reason_rejecting_count_age'] + 1) * \
                                                              (df_matches[
                                                                   'female_female_rejection_count_age'] + 1)
    df_matches['male_rejects_female_product_age'] = np.log(np.log(df_matches['male_rejects_female_product_age']+ epsilon))

    df_matches['male_rejects_female_percentage_product'] = df_matches['male_percent_rejecter'] * df_matches[
        'female_percent_rejected']
    df_matches['female_rejects_male_percentage_product'] = df_matches['female_percent_rejecter'] * df_matches[
        'male_percent_rejected']

    return df_matches

def add_rejection_sums(df_members: pd.DataFrame, df_matches: pd.DataFrame) -> pd.DataFrame:
    # count a man rejects women
    male_count_rejecter = df_matches[df_matches['male_s'] == 'Declined'] \
        .groupby('male_id') \
        .size() \
        .reset_index(name='male_rejecter_count')

    df_members = df_members.merge(male_count_rejecter,
                                  left_on='id',
                                  right_on='male_id',
                                  how='left',
                                  suffixes=('', '_from_matches')  # Added suffixes
                                  )
    # count a man gets rejected by women
    male_count_rejected = df_matches[df_matches['female_s'] == 'Declined'] \
        .groupby('male_id') \
        .size() \
        .reset_index(name='male_rejected_count')
    df_members = df_members.merge(male_count_rejected,
                                  left_on='id',
                                  right_on='male_id',
                                  how='left',
                                  suffixes=('', '_from_matches')  # Added suffixes
                                  )
    # count a woman rejects men
    female_count_rejecter = df_matches[df_matches['female_s'] == 'Declined'] \
        .groupby('female_id') \
        .size() \
        .reset_index(name='female_rejecter_count')

    df_members = df_members.merge(female_count_rejecter,
                                  left_on='id',
                                  right_on='female_id',
                                  how='left',
                                  suffixes=('', '_from_matches')  # Added suffixes
                                  )
    # count a woman gets rejected by men
    female_count_rejected = df_matches[df_matches['male_s'] == 'Declined'] \
        .groupby('female_id') \
        .size() \
        .reset_index(name='female_rejected_count')
    df_members = df_members.merge(female_count_rejected,
                                  left_on='id',
                                  right_on='female_id',
                                  how='left',
                                  suffixes=('', '_from_matches')  # Added suffixes
                                  )
    df_members['rejecter_count'] = df_members['male_rejecter_count'].fillna(df_members['female_rejecter_count'])
    df_members['rejecter_count'].fillna(0, inplace=True)
    df_members['rejected_count'] = df_members['male_rejected_count'].fillna(df_members['female_rejected_count'])
    df_members['rejected_count'].fillna(0, inplace=True)
    df_members['total'] = df_members['rejecter_count'] + df_members['rejected_count']
    df_members['percent_rejecter'] = (df_members['rejecter_count'] / df_members['total']).round(2)
    df_members['percent_rejected'] = (df_members['rejected_count'] / df_members['total']).round(2)
    columns_to_drop = ['male_rejecter_count', 'female_rejecter_count', 'male_rejected_count', 'female_rejected_count',
                       'male_id', 'female_id', 'male_id_from_matches', 'female_id_from_matches']
    df_members.drop(columns=columns_to_drop, inplace=True)
    return df_members


def add_rejection_type_counts(df_members: pd.DataFrame, df_matches: pd.DataFrame) -> pd.DataFrame:
    df_matches['male_pr'] = df_matches['male_pr'].replace({None: 'None'})
    df_matches['female_pr'] = df_matches['female_pr'].replace({None: 'None'})
    df_matches['male_pr'] = df_matches['male_pr'].replace({'Not my physical look': 'Physical look'})
    df_matches['female_pr'] = df_matches['female_pr'].replace({'Not my physical look': 'Physical look'})

    male_pr_reasons = df_matches['male_pr'].unique()
    female_pr_reasons = df_matches['female_pr'].unique()

    # Repeating the pattern for male_pr reasons, with added suffixes

    # this counts number of times a man or woman rejects other people for a reason
    for reason in male_pr_reasons:
        column_suffix = reason.lower().replace(' ', '_')
        count_column_name = f'male_reason_rejecting_count_{column_suffix}'

        counts = df_matches[df_matches['male_pr'] == reason] \
            .groupby('male_id') \
            .size() \
            .reset_index(name=count_column_name)

        df_members = df_members.merge(counts,
                                      left_on='id',
                                      right_on='male_id',
                                      how='left',
                                      suffixes=('', '_from_matches') # Added suffixes
                                      )

        df_members[count_column_name] = df_members[count_column_name] + 1
        df_members[count_column_name] = df_members[count_column_name].fillna(0).astype(int)

    for reason in female_pr_reasons:
        column_suffix = reason.lower().replace(' ', '_')
        count_column_name = f'female_reason_rejecting_count_{column_suffix}'

        counts = df_matches[df_matches['female_pr'] == reason] \
            .groupby('female_id') \
            .size() \
            .reset_index(name=count_column_name)

        df_members = df_members.merge(counts,
                                      left_on='id',
                                      right_on='female_id',
                                      how='left',
                                      suffixes=('', '_from_matches')
                                      )  # Added suffixes
        df_members[count_column_name] = df_members[count_column_name] + 1
        df_members[count_column_name] = df_members[count_column_name].fillna(0).astype(int)


    # this counts number of times a man or woman is rejected for a reason
    for reason in male_pr_reasons:
        column_suffix = reason.lower().replace(' ', '_')
        count_column_name = f'female_rejection_count_{column_suffix}'

        counts = df_matches[df_matches['male_pr'] == reason] \
            .groupby('female_id') \
            .size() \
            .reset_index(name=count_column_name)

        df_members = df_members.merge(counts,
                                      left_on='id',
                                      right_on='female_id',
                                      how='left',
                                      suffixes=('', '_from_matches')
                                      )  # Added suffixes
        df_members[count_column_name] = df_members[count_column_name].fillna(0).astype(int)

    # Repeating the pattern for female_pr reasons, with added suffixes
    for reason in female_pr_reasons:
        column_suffix = reason.lower().replace(' ', '_')
        count_column_name = f'male_rejection_count_{column_suffix}'

        counts = df_matches[df_matches['female_pr'] == reason] \
            .groupby('male_id') \
            .size() \
            .reset_index(name=count_column_name)

        df_members = df_members.merge(counts,
                                      left_on='id',
                                      right_on='male_id',
                                      how='left',
                                      suffixes=('', '_from_matches')
                                      )  # Added suffixes
        df_members[count_column_name] = df_members[count_column_name].fillna(0).astype(int)

    # drop extra columns that were generated as a result of the suffixes
    df_members.drop(columns='male_id_from_matches', inplace=True)
    df_members.drop(columns='female_id_from_matches', inplace=True)

    # df_members = add_rejection_products(df_members)

    return df_members