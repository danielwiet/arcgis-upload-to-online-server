# arcgis-upload-to-online-server

Load code into Python window in ArcGis Pro (untested for ArcGis Desktop)

This code imports all shapefiles from a project folder, signs into ArcGis Online (user input credentials) creates a service definition draft with saved summary, description, terms of use, and tags, and uploads the service definition 

Replace strings that begin with 'Replace this'

Keep strings otherwise

If shapefiles load but error prevents the upload to the online server, exit ArcGis Pro, delete the project folder and restart from scratch

There is a known bug regarding service_draft.allowExporting, resulting in the value not reflecting on the server. It will have to be manually toggled in the settings
