import csv
import os


def replace_first_line_in_csv(file_path, new_first_line):
    """
    Opens a CSV file, deletes its first line, and writes a new first line.

    Args:
        file_path (str): The path to the CSV file.
        new_first_line (list): A list of strings representing the new first line
                                (e.g., ['header1', 'header2', 'header3']).
    """
    try:
        # Read all lines from the CSV file, skipping the first one
        with open(file_path, "r", newline="") as infile:
            reader = csv.reader(line.replace("\0", "") for line in infile)
            header = next(reader, None)  # Skip the first line
            lines = list(reader)

        # Create a temporary file to write the modified content
        temp_file_path = file_path + ".tmp"
        with open(temp_file_path, "w", newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(new_first_line)  # Write the new first line
            writer.writerows(lines)  # Write the remaining lines

        # Replace the original file with the temporary file
        os.replace(temp_file_path, file_path)
        print(f"Successfully replaced the first line in '{file_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    member_file_path = os.path.join(
        script_dir, "raw_data", "YUAIMemberData17June2025.csv"
    )
    # member_file_path = "raw_data/YUAIMemberData17June2025.csv"
    member_new_header = [
        "Member_ID",
        "Country",
        "City",
        "State",
        "Gender",
        "Age",
        "Religious_orientation",
        "Ethnicity",
        "Cultural_Background",
        "baal_teshuva",
        "years_Orthodox_baal_teshuva",
        "Cohen",
        "convert_female",
        "parents_convert",
        "mother_maternal_grandmother_Jewish",
        "Family_religious_background",
        "Describe_family_religious_background",
        "Head_covering_female",
        "Kosher",
        "Dress_female",
        "Head_covering_male",
        "Frequency_of_Tefilah",
        "Frequency_of_shul_attendance_male",
        "Frequency_of_Torah_study_male",
        "Watching_TV",
        "Going_out_to_Movies",
        "Watching_Movies_at_home",
        "want_to_meet_someone_who_cover_hair",
        "want_to_meet_someone_who_wears_only_skirts",
        "Secular_education",
        "Emphasis_of_studies",
        "Jewish_education",
        "study_in_Israel",
        "Profession",
        "Job_description",
        "Eye_color",
        "Hair_color",
        "Height",
        "Body_type",
        "mental_physical_disability",
        "My_marriage_status",
        "how_long_married",
        "How_long_single",
        "times_divorced",
        "have_Jewish_Divorce",
        "have_civil_divorce",
        "have_children",
        "how_many",
        "number_live_with_you",
        "age_of_youngest",
        "want_additional_children",
        "Can_marry_Cohen",
        "Number_of_siblings",
        "Political_orientation",
        "Smoking_habits",
        "How_active_are_you",
        "Plan_to_aliya",
        "willing_to_relocate",
        "pet_person",
        "Pet_i_own",
        "Additional_pet_i_own",
        "native_language",
        "Languages_spoken",
        "Age_range_From",
        "Age_range_To",
        "Height_range_From",
        "Height_range_To",
        "Desired_marital_status",
        "Minimum_Education_level",
        "acceptable_for_match_to_have_children",
        "Acceptable_religious_orientation",
        "Acceptable_smoking_habits",
        "ok_dating_someone_with_disability",
        "Acceptable_aliyah_responses",
        "Acceptable_kosher_observance",
        "ok_dating_baal_teshuva",
        "Acceptable_places_to_live_Countries",
        "Acceptable_places_States",
        "family_relgious_background",
        "male_torah_study_female_sign_up",
        "want_covered_hair_male_sign_up",
        "want_only_wears_skirts",
        "Jewish_education_preference",
        "Body_Type_preference",
        "Preference_regarding_Ethnicity",
        "Preference_cultural_background",
        "My_Personality_Traits",
        "My_Personality_go_out_to",
        "Favorite_Music",
        "Physical_Activities_interests",
        "My_Favorite_Pastimes",
        "looking_for_in_a_person",
        "short_description_of_yourself",
        "looking_for_in_spouse",
        "community_work",
        "Introvert_Extravert",
        "Sensor_Intuitive",
        "Thinker_Feeler",
        "Judger_Perceiver",
        "Approved",
        "Dating_Status",
        "Colleges_universities",
        "community_work_2",
        "parents_convert_before_birth",
        "Elementary_school",
        "Location_I_grew_up",
        "Name_Secondary_School",
        "Name_seminaries",
        "Name_study_one_year",
        "Parent_shul",
        "Parent_location",
        "Parents_marital_status",
        "Complete_Incomplete",
        "Photo",
        "Site",
        "Profile_Last_modified_date",
        "Updated",
    ]
    replace_first_line_in_csv(member_file_path, member_new_header)

    matches_file_path = os.path.join(
        script_dir, "raw_data", "MatchesData_YU_CS_Deptv3.csv"
    )
    # matches_file_path = "raw_data/MatchesData_YU_CS_Deptv3.csv"
    matches_new_header = [
        "Match_ID",
        "Male_ID",
        "Female_ID",
        "Match_status_for_match",
        "Match_status_male",
        "Match_status_female",
        "Progress_report_male",
        "Progress_report_female",
    ]
    replace_first_line_in_csv(matches_file_path, matches_new_header)


if __name__ == "__main__":
    main()
