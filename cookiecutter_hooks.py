import os
import re

def validate_pipeline(pipeline):
    valid_pipelines = ["rna", "multi"]
    if pipeline.lower() not in valid_pipelines:
        return False, f"Invalid pipeline option. Please choose one of: {', '.join(valid_pipelines)}"
    return True, "Pipeline validation successful."

def validate_raw_data_folder(raw_data_folder):
    if not os.path.isdir(raw_data_folder):
        return False, "Raw data folder doesn't exist."
    
    # Check if there are subfolders
    subfolders = [f for f in os.listdir(raw_data_folder) if os.path.isdir(os.path.join(raw_data_folder, f))]
    if not subfolders:
        return False, "Raw data folder must contain subfolders."

    # Check if there are files with ".fastq.gz" suffix in each subfolder
    for subfolder in subfolders:
        files = os.listdir(os.path.join(raw_data_folder, subfolder))
        fastq_files = [f for f in files if f.endswith('.fastq.gz')]
        if not fastq_files:
            return False, f"No '.fastq.gz' files found in subfolder '{subfolder}'."

    return True, "Validation successful."

hooks = {
    "pre_gen_project": [validate_pipeline, validate_raw_data_folder]
}

