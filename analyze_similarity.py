import numpy as np
import scipy.io.wavfile as wav
import os
import librosa
import pandas as pd

# Function to calculate MFCCs of a given wav file
def calculate_mfcc(file_path):
    y, sr = librosa.load(file_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return mfcc.mean(axis=1)

# Function to compare MFCCs of two files
def compare_files(file1, file2):
    mfcc1 = calculate_mfcc(file1)
    mfcc2 = calculate_mfcc(file2)
    distance = np.linalg.norm(mfcc1 - mfcc2)
    return distance

# Folder path (replace with your folder path)
folder_path = 'path_to_your_wav_files'

# List of all wav files in the folder
wav_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]

# Dictionary to store the comparison results
comparison_results = {}

# Compare each file with every other file
for i, file1 in enumerate(wav_files):
    for j, file2 in enumerate(wav_files):
        if i < j:
            distance = compare_files(os.path.join(folder_path, file1), os.path.join(folder_path, file2))
            comparison_results[(file1, file2)] = distance

# Convert the results to a DataFrame for better readability
comparison_df = pd.DataFrame.from_dict(comparison_results, orient='index', columns=['MFCC Distance'])
comparison_df.reset_index(inplace=True)
comparison_df.rename(columns={'index': 'File Pair'}, inplace=True)

# Save the results to a CSV file
comparison_df.to_csv('wav_file_similarity_comparison.csv', index=False)

print("Analysis complete. Results saved to wav_file_similarity_comparison.csv")
