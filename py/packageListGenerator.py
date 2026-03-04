import os
import json

def generate_package_json(target_folder, output_file):
    # This list will hold all the paths
    contents = []

    # Standardize the target folder name for the JSON header
    folder_name = os.path.basename(target_folder.rstrip('/\\')) or target_folder

    for root, dirs, files in os.walk(target_folder):
        # Add directories to the list
        for name in dirs:
            rel_path = os.path.relpath(os.path.join(root, name), target_folder)
            contents.append(rel_path.replace("\\", "/")) # Use forward slashes for JSON consistency

        # Add files to the list
        for name in files:
            rel_path = os.path.relpath(os.path.join(root, name), target_folder)
            contents.append(rel_path.replace("\\", "/"))

    # Construct the final dictionary based on your template
    data = {
        "package": {
            "folder": folder_name,
            "packageContents": sorted(contents) # Sorted looks much cleaner in JSON
        }
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(f"Done! Created {output_file} with {len(contents)} items.")

# --- Settings ---
target = "packages\LegacyConsoleEdition\_package"
output = "manifest.json"

# Create the folder if it doesn't exist (for testing)
if not os.path.exists(target):
    os.makedirs(target)

generate_package_json(target, output)