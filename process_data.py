import os
import glob
import subprocess
from google.colab import drive

drive.mount('/content/drive')

output_dir = "/content/drive/My Drive/machine_vision/data/processed/train/"
os.makedirs(output_dir, exist_ok=True)

# Define paths
input_dir = "/content/drive/My Drive/machine_vision/data/train/"
stats_file = "/content/drive/My Drive/machine_vision/data/stats.json"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Find all files matching the pattern
input_files = glob.glob(os.path.join(input_dir, "*.tfrecord.GZIP"))

# Iterate over all files and preprocess them
for input_file in input_files:
    output_file = os.path.join(output_dir, os.path.basename(input_file))

    # Check if the file already exists in the output directory
    if os.path.exists(output_file):
        print(f"Skipping {input_file} as it already exists in the processed folder.")
        continue

    command = [
        "python3.9", "/content/drive/My Drive/machine_vision/preprocess_tfrecords.py",
        "--dataset_stats", stats_file,
        "--output_dir", output_dir,
        input_file
    ]
    print(f"Processing {input_file}...")
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error processing {input_file}: {result.stderr}")
    else:
        print(f"Successfully processed {input_file}")

# Verify output
print("Preprocessing complete. Processed files saved to:", output_dir)
