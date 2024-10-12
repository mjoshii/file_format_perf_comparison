import json
from faker import Faker
import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Function to generate random data for a single candidate
def generate_candidate_data(fake):
    return {
        'id': str(fake.uuid4()),
        'full_name': fake.name(),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat(),
        'address': fake.address(),
        'city': fake.city(),
        'country': fake.country(),
        'citizenship': fake.country(),
        'resume_filename': f"resume_{fake.uuid4()}.pdf",
        'additional_files': f"{fake.random_int(0, 3)}_additional_files",
        'industry': fake.job(),
        'designation': fake.job(),
        'years_of_experience': fake.random_int(0, 40),
        'gender': fake.random_element(['Male', 'Female', 'Non-binary', 'Prefer not to say']),
        'religion': fake.random_element(['Christianity', 'Islam', 'Hinduism', 'Buddhism', 'Judaism', 'Other', 'None', 'Prefer not to say']),
        'sexuality': fake.random_element(['Heterosexual', 'Homosexual', 'Bisexual', 'Other', 'Prefer not to say']),
        'military_service': fake.random_element(['Yes', 'No', 'Prefer not to say']),
        'criminal_record': fake.random_element(['Yes', 'No', 'Prefer not to say']),
        'legal_work_authorization': fake.random_element(['Yes', 'No', 'Requires sponsorship']),
    }

# Function to generate and save candidate data as a single JSON file
def generate_and_save_candidates(num_candidates):
    fake = Faker()
    all_candidates = []

    for i in range(num_candidates):
        candidate_data = generate_candidate_data(fake)
        all_candidates.append(candidate_data)
        
        if (i + 1) % 10000 == 0:
            print(f"Generated {i + 1} candidate records")

    filename = 'all_candidates.json'
    with open(filename, 'w') as f:
        json.dump(all_candidates, f, indent=2)

    print(f"All {num_candidates} candidate records have been generated and saved to {filename}")

# Generate and save 1,000,000 candidate records in a single JSON file
generate_and_save_candidates(1000000)