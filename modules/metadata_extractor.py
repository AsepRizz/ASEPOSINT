import subprocess

def extract_metadata(file_path):
    result = f"Metadata extraction results for: {file_path}\n\n"
    
    try:
        # Using exiftool for metadata extraction
        output = subprocess.check_output(["exiftool", file_path], text=True)
        result += output
    except subprocess.CalledProcessError as e:
        result += f"Error during metadata extraction: {e.output}\n"
    except FileNotFoundError:
        result += "exiftool not installed. Please run install.sh\n"
    
    return result
