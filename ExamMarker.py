# Prompt the user to enter the file path for the answer key
answer_key_path = input("Enter the path to the answer key file: ")

# Read in the answer key from a file
with open(answer_key_path) as f:
    answer_key_lines = [line.strip() for line in f]

# Split each line into the answer and its point value and create a dictionary
answer_key = {}
for line in answer_key_lines:
    answer, point_value = line.split(",")
    answer_key[answer] = int(point_value)

# Prompt the user to enter the directory containing the student response files
directory_path = input("Enter the path to the directory containing the student response files: ")

# Loop through each file in the directory and calculate the score for each one
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        # Read in the student responses from the file
        filepath = os.path.join(directory_path, filename)
        with open(filepath) as f:
            student_responses = [line.strip() for line in f]

        # Compare the student responses to the answer key and calculate the percentage score
        total_score = 0
        max_score = sum(answer_key.values())
        for response in student_responses:
            if response in answer_key:
                total_score += answer_key[response]

        percentage_score = (total_score / max_score) * 100

        # Generate a report for each student response file
        print(f"Score for {filename}: {total_score} out of {max_score} ({percentage_score:.2f}%)")

