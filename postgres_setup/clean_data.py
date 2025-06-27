import csv
import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
member_file_path = os.path.join(script_dir, "raw_data", "YUAIMemberData17June2025.csv")
temp_file_path = os.path.join(script_dir, "raw_data", "YUAIMemberData_temp.csv")

try:
    # Write clean data to new temp file
    with open(
        member_file_path, "r", encoding="utf-8", errors="ignore", newline=""
    ) as infile:

        cleaned_lines = (line.replace("\0", "") for line in infile)
        # Open the temporary file for writing
        with open(temp_file_path, "w", encoding="utf-8", newline="") as outfile:
            reader = csv.reader(cleaned_lines)
            writer = csv.writer(outfile)

            # Process row-by-row, which is memory efficient
            for row in reader:
                writer.writerow(row)
    shutil.move(temp_file_path, member_file_path)
    print("Complete")

except FileNotFoundError:
    print(f"\nError: The file was not found at {member_file_path}")

except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
    print("The original file has NOT been changed.")
