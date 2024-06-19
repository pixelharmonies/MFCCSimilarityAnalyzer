
# MFCCSimilarityAnalyzer

## Description

MFCCSimilarityAnalyzer is a Python-based tool designed to analyze and compare music tracks based on their Mel-Frequency Cepstral Coefficients (MFCC). This project helps you determine the similarity between various audio tracks, ensuring diversity and uniqueness in your music catalog. Ideal for musicians, producers, and audio engineers who want to avoid redundancy and maintain a diverse collection of tracks.

## Features

- **MFCC Analysis:** Extracts and computes the MFCCs of audio tracks for detailed comparison.
- **Similarity Measurement:** Calculates the Euclidean distance between the MFCCs of different tracks to quantify their similarity.
- **Categorization:** Classifies tracks into "Very Similar," "Moderately Similar," and "Distinct" based on their MFCC distances.
- **Data Visualization:** Provides a clear and concise CSV output of the similarity analysis for further inspection and decision-making.

## Requirements

- Python 3.x
- numpy<2
- scipy
- librosa
- pandas

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/pixelharmonies/MFCCSimilarityAnalyzer.git
   ```
2. Navigate to the project directory:
   ```sh
   cd MFCCSimilarityAnalyzer
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Place your WAV files in the designated folder (e.g., `wav_files`).
2. Run the analysis script:
   ```sh
   python analyze_similarity.py
   ```
3. Check the generated CSV file (`wav_file_similarity_comparison.csv`) for the similarity analysis results.

## Example

```sh
python analyze_similarity.py
```

## Output

The script generates a CSV file with the following columns:
- **File Pair:** The pair of compared audio tracks.
- **MFCC Distance:** The calculated distance indicating the level of similarity.

## Contribution

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, please contact [Gary] at [github@pixelharmonies.com].
