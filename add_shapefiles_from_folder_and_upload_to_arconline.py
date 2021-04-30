# Use this code in arcgis pro to batch import all shapefiles in a project folder and upload to arcgis online

import arcpy
import glob
import os

# get the current map document
aprx = arcpy.mp.ArcGISProject("CURRENT")

# get the data frame
m = aprx.listMaps("Map")[0]

# IMPORTANT!!! paste folder path within the single quote. LEAVE THE r in front!!!!
path = r'REPLACE THIS: COPY AND PASTE THE FOLDER PATH AS TEXT (right click the address bar)'

# changes the os directory using the full path name
os.chdir(path)

# store current working directory
folder_dir = os.getcwd()

# find and store all files with .shp ending
shps = glob.glob(folder_dir + '\*.shp')

for shp_path in shps:
  m.addDataFromPath(shp_path)

aprx.save()

arcpy.SignInToPortal('https://www.arcgis.com', 'REPLACE THIS: USER_NAME', 'REPLACE THIS: USER_PASSWORD')

# Set output file names
# where to store the ssd files
outdir = r"REPLACE THIS: LOCATION TO STORE THE .SSD FILES"

# what to name it once published
service = "REPLACE THIS: NAME OF FEATURE LAYER"

sddraft_filename = service + ".sddraft"
sddraft_output_filename = os.path.join(outdir, sddraft_filename)

# Reference map to publish
# get the current map document
aprx = arcpy.mp.ArcGISProject("CURRENT")

# get the data frame
m = aprx.listMaps("Map")[0]

# Create FeatureSharingDraft and set service properties
sharing_draft = m.getWebLayerSharingDraft("HOSTING_SERVER", "FEATURE", service)

# sharing_draft.allow_exporting = True
sharing_draft.allowExporting = True

sharing_draft.portalFolder = "REPLACE THIS: NAME OF FOLDER ON ACRONLINE TO SAVE THE FEATURE LAYER"

sharing_draft.summary = "REPLACE THIS: INITIAL SUMMARY OF THE FEATURE LAYER"

sharing_draft.tags = "REPLACE THIS: TAGS SEPARATED BY COMMAS"

sharing_draft.description = "REPLACE THIS: DETAILED DESCRIPTION OF THE FEATURE LAYER"

sharing_draft.credits = "REPLACE THIS: CREDITS (ATTRIBUTIONS)"

sharing_draft.useLimitations = "REPLACE THIS: TERMS OF USE"

# Create Service Definition Draft file
sharing_draft.exportToSDDraft(sddraft_output_filename)

# Stage Service
sd_filename = service + ".sd"
sd_output_filename = os.path.join(outdir, sd_filename)
arcpy.StageService_server(sddraft_output_filename, sd_output_filename)

# Share to portal
print("Uploading Service Definition...")
arcpy.UploadServiceDefinition_server(sd_output_filename, "My Hosted Services")

print("Successfully Uploaded service.")

'''
STILL TO DO
Change sharing permission on AGOL
Change thumbnail for feature layer (hosted)
Check dates are correct and change if necessary
Click Export Data in Settings
'''
