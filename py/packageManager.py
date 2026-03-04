import hyperionX as hyperionX
import json
import os
import subprocess

packageInstallPath = 'C:/HyperionPackages'

def __main__():
    ## Extract and open the file, aseell as get the metapackage info
    hyperionX.extractPackage()
    with open('temp/metapackage.json', 'r', encoding='utf-8') as file:
        metapackage = json.load(file)

    ## load the package metadata
    with open(f'temp/{metapackage["metaPath"]}', 'r', encoding='utf-8') as metafile:
        meta = json.load(metafile) 
    

    ## install the packagefile to the packages folder
    subprocess.run([f"temp\{metapackage["entrypoint"]}", f"temp\_package", f"{packageInstallPath}\{metapackage["name"]}"])
    hyperionX.cleanupPackage()

    with open(f"{packageInstallPath}/packages.jsonl", 'r', encoding='utf-8') as packageList:
        pcl = json.load(packageList)
        newPackage = metapackage["packageDetails"]

    pcl["packages"].update(newPackage)
    
    with open(f"{packageInstallPath}/packages.jsonl", 'w', encoding='utf-8') as packageList:
        json.dump(pcl, packageList, indent=4)
    

__main__()
