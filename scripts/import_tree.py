import os,subprocess,json


fileChooser=hou.ui.selectFile(
    #start_directory="C:\Users\david\Dropbox\Assets\NodeRepos",
    start_directory=hou.getenv('REPO'),
    title="Node importer",
    pattern="*.nd",
    chooser_mode=hou.fileChooserMode.Read
)

if fileChooser!='':
    jsonFile=fileChooser.replace('.nd','.json')

    exportInfo=json.loads(open(jsonFile,'r').read())
    parentPath=exportInfo['parentPath']

    container=hou.node(parentPath)

    if container:
        container.loadItemsFromFile(fileChooser)
        hou.ui.setStatusMessage("File loaded",hou.severityType.ImportantMessage)
    else:
        container=hou.node(hou.ui.selectNode(title="pick a container node for your tree"))
        container.loadItemsFromFile(fileChooser)
        hou.ui.setStatusMessage("File loaded",hou.severityType.ImportantMessage)