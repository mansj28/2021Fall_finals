"""
Project Name: Crime Data Analysis across the years in the states of USA
Designed By:
    1. Manasi Joshi
    2. Shruti Deekshitula
Description:
    Crime analysis has become an essential tool in law enforcement to enhance public safety, identify emerging trends,
    allocate resources, and plan crime-prevention strategies. Understanding the crime rate and factors that majorly
    influence crimes has become an important aspect to curb the crimes, therefore we will be focusing on the
    below-mentioned analysis and hypotheses to identify the significant factors that, in our view, are reasons for
    crimes across the US and factors that lead to changes in crimes rates every year.
Pre-requisite Installations:
    1. Install these libraries in your cloned project via PyCharm:
        1. pandas
Acceptable Input:
    1. final_crime_data.csv - data for states in the US for years between 2006 - 2019
    2. state_pop.csv -
Acceptable Output:
    1. Hypothesis 1 - TRUE or FALSE
    2. Hypothesis 2 - TRUE or FALSE
    3. Hypothesis 3 - TRUE or FALSE
    4. Various visualizations
Database sources and processing:

Crime Data -
    Downloaded the data from https://crime-data-explorer.fr.cloud.gov/pages/downloads for the states that are present on
    this site for years between 2006 - 2019. The data files are downloaded in the zip format for each state-year
    combination. Since the datafile for analyzing the crimes was not readily available we performed the data
    pre-processing. This included unzipping the files, merging the csv files for each state-year combination folder as
    there were several csv files per state-year zipped folder. We processed the data for only the required fields and
    thus merged. Later, to have a consolidated datafile for every state and years the data was present for we appended
    each merged datafile.

    Note: The main method in "data_preprocessing.py" is executed once and need not be executed again as the final file
    is generated and ready for use.
    As the downloaded zipped files are large in size we have not included them in the git folder. After performing
    all the data processing a consolidated datafile was generated which is the main "final_crime_data.csv". We have
    used this across our all analysis and hypothesis.



Direction to run the program:
    1. Ensure 'final_crime_data.csv' in the 'final_datasets' folder.
    2. Run each cell in the 'visualizations.ipynb' file to visualize the hypothesis.
"""
import pandas as pd
import glob
import zipfile

def get_files(path: str) -> list:
    """
    Returns a list of all the downloaded files for each state.
    :param path: String with path to the pre processing data files
    :return: List of files present in the given path folder

    >>> get_files("test\\preprocess_test_data\\*")
    ['test\\\preprocess_test_data\\\Alabama', 'test\\\preprocess_test_data\\\Arizona']
    """
    # path = "C:\\Users\\dshru\\Desktop\\PR ProjecT data\\*\\*"
    files = glob.glob(path, recursive=True)
    return files


def get_unique_folders(path: str) -> list:
    """
    Returns a list of all folders  present in the given path after unqizp of the folders
    :param path: String input for the path to retrieve folder inside the path folder for states year-wise
    :return: List with names of the "state_abbreviation-year" folders to identify each state and year
    >>> get_unique_folders("test\\preprocess_test_data_unzipped\\*")
    ['AL-2006', 'AL-2007', 'NM-2009', 'NM-2018', 'NM-2019']
    """

    files = glob.glob(path, recursive=True)
    state_year = [file[-7:] for file in files]
    return state_year


def create_merged(f_path: str, f_name: str)-> pd.DataFrame:
    """
    Returns a final dataframe after reading the data for each required csv file of all the csv files present in each
    "state-year" folder to merge the data into one single dataframe. Read the datafiles and process each dataframe with
    easy to understand fields.
    :param f_path: String of the folder path which contains all the "state-year" folders
    :param f_name: String of the folder name to read required datafiles
    :return: Merged dataframe with fields from each datafile of the provided "state-year" folder
    >>> create_merged("test\\preprocess_test_data_unzipped","\\AL-2006") # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
          incident_id  ...                                          race_desc
    0        36591519  ...                                              White
    1        36595364  ...                                              White
    2        36595364  ...                                              White
    3        36595364  ...                                              White
    4        36595364  ...                                              White
    ...           ...  ...                                                ...
    1617     36610094  ...  Asian, Native Hawaiian, or Other Pacific Islander
    1618     36598341  ...  Asian, Native Hawaiian, or Other Pacific Islander
    1619     36607118  ...  Asian, Native Hawaiian, or Other Pacific Islander
    1620     36612864  ...  Asian, Native Hawaiian, or Other Pacific Islander
    1621     36606048  ...                   American Indian or Alaska Native
    <BLANKLINE>
    [1622 rows x 12 columns]
    """
    # for all states with years between 2008 - 2016
    if f_name[-4:] not in ['2017', '2018', '2019']:
        cde_df = pd.read_csv(f_path+f_name+r"\\cde_agencies.csv",
                             usecols=['agency_id', 'state_abbr'])

        areestee_df = pd.read_csv(f_path+f_name+r"\\nibrs_arrestee.csv", usecols=['arrestee_id', 'incident_id',
                      'race_id', 'age_num', 'sex_code', 'offense_type_id', 'arrest_type_id'])

        aresstee_weapon_df = pd.read_csv(f_path+f_name+r"\\nibrs_arrestee_weapon.csv", usecols=['arrestee_id',
                             'nibrs_arrestee_weapon_id', 'weapon_id'])

        incident_df = pd.read_csv(f_path+f_name+r"\\nibrs_incident.csv", usecols=['nibrs_month_id', 'incident_id',
                      'agency_id'])

        month_df = pd.read_csv(f_path+f_name+r"\\nibrs_month.csv", usecols=['nibrs_month_id', 'agency_id',
                   'month_num', 'data_year'])

        offense_df = pd.read_csv(f_path+f_name+r"\\nibrs_offense.csv", usecols=['offense_id', 'incident_id',
                     'offense_type_id'])

        offense_type_df = pd.read_csv(f_path+f_name+r"\\nibrs_offense_type.csv", usecols=['offense_type_id',
                          'crime_against'])

        weapon_type_df = pd.read_csv(f_path+f_name+r"\\nibrs_weapon_type.csv", usecols=['weapon_id', 'weapon_name'])

        ref_race_df = pd.read_csv(f_path+f_name+r"\\ref_race.csv", usecols=['race_id', 'race_desc'])

    # for all states with years between 2017 - 2019
    elif folder[-4:] in ['2017', '2018', '2019']:
        cde_df = pd.read_csv(f_path+f_name+r"\\agencies.csv", usecols=['AGENCY_ID', 'STATE_ABBR'])
        cde_df.columns = cde_df.columns.str.strip().str.lower()

        areestee_df = pd.read_csv(f_path+f_name+r"\\nibrs_arrestee.csv", usecols=['arrestee_id'.upper(), 'incident_id'.upper(),
                      'race_id'.upper(), 'age_num'.upper(), 'sex_code'.upper(), 'offense_type_id'.upper(), 'arrest_type_id'.upper()])
        areestee_df.columns = areestee_df.columns.str.strip().str.lower()

        aresstee_weapon_df = pd.read_csv(f_path+f_name+r"\\nibrs_arrestee_weapon.csv", usecols=['arrestee_id'.upper(),
                             'nibrs_arrestee_weapon_id'.upper(), 'weapon_id'.upper()])
        aresstee_weapon_df.columns = aresstee_weapon_df.columns.str.strip().str.lower()

        incident_df = pd.read_csv(f_path+f_name+r"\\nibrs_incident.csv", usecols=['nibrs_month_id'.upper(),
                      'incident_id'.upper(), 'agency_id'.upper()])
        incident_df.columns = incident_df.columns.str.strip().str.lower()

        month_df = pd.read_csv(f_path+f_name+r"\\nibrs_month.csv", usecols=['nibrs_month_id'.upper(),
                   'agency_id'.upper(), 'month_num'.upper(), 'data_year'.upper()])
        month_df.columns = month_df.columns.str.strip().str.lower()

        offense_df = pd.read_csv(f_path+f_name+r"\\nibrs_offense.csv", usecols=['offense_id'.upper(),
                     'incident_id'.upper(), 'offense_type_id'.upper()])
        offense_df.columns = offense_df.columns.str.strip().str.lower()

        offense_type_df = pd.read_csv(f_path+f_name+r"\\nibrs_offense_type.csv", usecols=['offense_type_id'.upper(),
                          'crime_against'.upper()])
        offense_type_df.columns = offense_type_df.columns.str.strip().str.lower()

        weapon_type_df = pd.read_csv(f_path+f_name+r"\\nibrs_weapon_type.csv", usecols=['weapon_id'.upper(),
                         'weapon_name'.upper()])
        weapon_type_df.columns = weapon_type_df.columns.str.strip().str.lower()

        ref_race_df = pd.read_csv(f_path+f_name+r"\\ref_race.csv", usecols=['race_id'.upper(), 'race_desc'.upper()])
        ref_race_df.columns = ref_race_df.columns.str.strip().str.lower()

    # merge each dataframe for having a final dataframe with required columns for further analysis
    df = pd.merge(incident_df, month_df, left_on='nibrs_month_id', right_on='nibrs_month_id')
    df.drop(['agency_id_x', 'nibrs_month_id'], axis=1, inplace=True)
    df.rename(columns={'agency_id_y' : 'agency_id'}, inplace=True)

    df = pd.merge(df, cde_df, left_on='agency_id', right_on='agency_id')
    df.drop(['agency_id'], axis=1, inplace=True)

    df = pd.merge(df, offense_df,left_on='incident_id', right_on='incident_id', how='outer')
    df = pd.merge(df, offense_type_df, left_on='offense_type_id', right_on='offense_type_id')
    df.drop(['offense_id', 'offense_type_id'], axis=1, inplace=True)

    df = pd.merge(df, areestee_df, left_on='incident_id', right_on='incident_id')

    df = pd.merge(df, aresstee_weapon_df, left_on='arrestee_id', right_on='arrestee_id')
    df.drop(['nibrs_arrestee_weapon_id'], axis=1, inplace=True)

    df = pd.merge(df, weapon_type_df, left_on='weapon_id', right_on='weapon_id')
    df.drop(['weapon_id'], axis=1, inplace=True)

    df = pd.merge(df, ref_race_df, left_on='race_id', right_on='race_id')
    df.drop(['race_id'], axis=1, inplace=True)

    df = df[~df['incident_id'].isna()]
    df = df[~df['incident_id'].isna()]
    df = df[['incident_id', 'data_year', 'state_abbr', 'month_num', 'crime_against',
             'arrestee_id', 'arrest_type_id', 'offense_type_id', 'age_num',
             'sex_code', 'weapon_name', 'race_desc']]

    return df


def write_csv(state_df_write: pd.DataFrame, folder_name: str) -> None:
    """
    Writes the dataframe to a csv file
    :param state_df_write: Merged dataframe for each "state-year" folder
    :param folder_name:
    :return: None

    >>> state_df_test = create_merged(r"test\\preprocess_test_data_unzipped","\\AL-2007")
    >>> write_csv(state_df_test,"AL-2007")
    """
    state_df_write.to_csv(r"process_datasets\merged_files\\" + folder_name + ".csv", index=False)

    return None


def append_merged_files(f_data: pd.DataFrame, to_merge: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a final dataframe of the merged dataframes for all states across the years
    :param f_data: Dataframe to append the other dataframes
    :param to_merge: Merged dataframe to be appended
    :return: Final dataframe after all merged dataframes are appended
    >>> df_AL = create_merged(r"test\\preprocess_test_data_unzipped", "\\AL-2006")
    >>> df_NM = create_merged(r"test\\preprocess_test_data_unzipped", "\\AL-2006")
    >>> new_df = append_merged_files(df_AL, df_NM)
    >>> new_df # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
            incident_id  ...                                          race_desc
    0        36591519  ...                                              White
    1        36595364  ...                                              White
    2        36595364  ...                                              White
    3        36595364  ...                                              White
    4        36595364  ...                                              White
    ...           ...  ...                                                ...
    1617     36610094  ...  Asian, Native Hawaiian, or Other Pacific Islander
    1618     36598341  ...  Asian, Native Hawaiian, or Other Pacific Islander
    1619     36607118  ...  Asian, Native Hawaiian, or Other Pacific Islander
    1620     36612864  ...  Asian, Native Hawaiian, or Other Pacific Islander
    1621     36606048  ...                   American Indian or Alaska Native
    <BLANKLINE>
    [3244 rows x 12 columns]
    """
    f_data = f_data.append(to_merge)

    return f_data


if __name__ == "__main__":

    path = r"process_datasets\pre_processing_data\*"
    data_files = get_files(path)

    for file in data_files[:]:
        with zipfile.ZipFile(str(file), "r") as zip_ref:
            print(str(file)[-11:-4])
            path = r"pre_processing_data\\" + str(file)[-11:-4]
            zip_ref.extractall(r"pre_processing_data\\" + str(file)[-11:-4])

    path1 = r"process_datasets\pre_processing_data_unzipped\*"
    unique_folders = get_unique_folders(path1)

    folder = "AL-2007"
    unzip_path = r"process_datasets\\pre_processing_data_unzipped\\"
    for folder in unique_folders:
        state_df = create_merged(unzip_path, folder)
        write_csv(state_df, folder)

    # append all the files after merge
    files = glob.glob(r"merged_files\\*", recursive=True)
    df = pd.read_csv(files[0])
    for f in files[1:]:
        new_df = pd.read_csv(f)
        df = append_merged_files(df, new_df)

    # write the processed file to .csv for analyzing the hypothesis further
    df.to_csv(r"final_datasets\\dataset_final.csv", index=False)



