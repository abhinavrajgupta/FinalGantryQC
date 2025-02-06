<div align="center">
  <h1>Wirebond Detection and Silicon Module Analysis Repository</h1>
  <p>This repository seamlessly combines advanced wirebond detection and silicon module analysis for images captured from the OGP machine, offering a comprehensive solution for precise wirebonding optimization.</p>
</div>

---

## Getting Started

### Prerequisites
Please note that setting up a new Conda environment is required to run these scripts. The Conda environment configuration is provided in the **environment.yml** file. Additionally, please ensure you have an **Ubuntu Linux System** to run this program; otherwise, you might encounter numerous PackageNotFound errors.

### Installation
#### Cloning the repository:
     git clone https://github.com/abhinavrajgupta/FinalGantryQC
#### Working Directory:
     cd FinalGantryQC
#### Setting up the environment:
     conda env create -f environment.yml
#### Activating the environment:
     conda activate detectenv

### Adding Modules and Imgaes
The code in this repository is structured to specify paths for uploading images. Ensure that you place your upload module in the appropriate directory to maintain compatibility with the codebase. The path format follows this structure: 
######  current_directory/Modules/(Upload_Module_Here)
        mkdir Modules
#### Upload your Images here
##### [For Example you will upload M15 in the Modules file such that the path is structured as Modules/M15/(images and text file here)]

## How It Works
### 1. Upload Images:
  - Place your OGP-captured images in the specified directory.
### 2. Run the Detection Script:
  - Execute the detection script to infer wirebond characteristics from the images.
### 3. Data Analysis Script:
  - Run the analysis script to generate histograms, comprehensive summary table, and tornado plots of the inference results.

## Usage:
### 1. Run Detection Script:
     python merge_detect.py
### 2. Generate Analysis:
###### Before running this script, please open **analyze_results.py** and update your current directory as base directory in the first function.
     python analyze_results.py

## Results:
### 1. Detection1 Results: Images with labels for Wirebonds saved at:
    ../Modules/Module_Name/Reusltswirebond
### 2. Detection Results: Images with labels for mercedes benz intersection saved at:
    ../Modules/Module_Name/ReusltsArrowPlots
### 3. Histogram: Visual representation of key detection metrics saved at:
    ../Modules/Module_Name/Reusltswirebond/Histogram.jpg
### 4. Summary Table: Comprehensive insights into wirebond detection results saved at:
    ../Modules/Module_Name/Reusltswirebond/Summary_Table.csv
### 5. Tornado Plots: Visual representation of offset of individual holes in a silicon module:
    ../Modules/Module_Name/ReusltsArrowPlots/ArrowPlot.jpg
    
## Contributing
#### Contributions are welcome! Feel free to fork the repository and submit pull requests.










<br><br><br> <!-- This will create a gap -->
<br><br><br> <!-- This will create a gap -->





