import polars as pl
import numpy as np
from faker import Faker

# Set a seed for reproducibility
np.random.seed(42)

# Function to generate random data for different data types
def generate_data(no_of_rows):
    fake = Faker()
    data = {
            'full_name': [fake.name() for _ in range(no_of_rows)],
            'email': [fake.email() for _ in range(no_of_rows)],
            'phone_number': [fake.phone_number() for _ in range(no_of_rows)],
            'date_of_birth': [fake.date_of_birth(minimum_age=18, maximum_age=65) for _ in range(no_of_rows)],
            'address': [fake.address() for _ in range(no_of_rows)],
            'city': [fake.city() for _ in range(no_of_rows)],
            'country': [fake.country() for _ in range(no_of_rows)],
            'citizenship': [fake.country() for _ in range(no_of_rows)],
            'resume_filename': [f"resume_{fake.uuid4()}.pdf" for _ in range(no_of_rows)],
            'additional_files': [f"{fake.random_int(0, 3)}_additional_files" for _ in range(no_of_rows)],
            'industry': [fake.job() for _ in range(no_of_rows)],
            'designation': [fake.job() for _ in range(no_of_rows)],
            'years_of_experience': [fake.random_int(0, 40) for _ in range(no_of_rows)],
            'gender': [fake.random_element(['Male', 'Female', 'Non-binary', 'Prefer not to say']) for _ in range(no_of_rows)],
            'religion': [fake.random_element(['Christianity', 'Islam', 'Hinduism', 'Buddhism', 'Judaism', 'Other', 'None', 'Prefer not to say']) for _ in range(no_of_rows)],
            'sexuality': [fake.random_element(['Heterosexual', 'Homosexual', 'Bisexual', 'Other', 'Prefer not to say']) for _ in range(no_of_rows)],
            'military_service': [fake.random_element(['Yes', 'No', 'Prefer not to say']) for _ in range(no_of_rows)],
            'criminal_record': [fake.random_element(['Yes', 'No', 'Prefer not to say']) for _ in range(no_of_rows)],
            'legal_work_authorization': [fake.random_element(['Yes', 'No', 'Requires sponsorship']) for _ in range(no_of_rows)]
            }
    return data

# # Create a DataFrame with 200 unique columns
# columns = []
# data_types = ['date_col', 'string_col', 'integer_col', 'float_col', 'boolean_col']

# for _ in range(40):  # 5 data types x 40 columns each = 200 columns
#     for data_type in data_types:
#         columns.append(data_type)

# # Shuffle the columns to ensure randomness
# np.random.shuffle(columns)

# Generate random data
data = generate_data(1000000)

# Create DataFrame
df = pl.DataFrame(data)
print(df.head())

# Save DataFrame to CSV and PARQUET
df.write_csv('all_candidates.csv', separator = ',')
df.write_parquet('all_candidates.parquet')