import os,subprocess,json,getpass
from datetime import datetime


selectedNodes=kwargs['items']
parentNode=selectedNodes[0].parent()

exportInfo={}
exportInfo['numNodes']=len(selectedNodes)
exportInfo['parentPath']=parentNode.path()
exportInfo['parentType']=parentNode.type().category().name()
exportInfo['user']=getpass.getuser()
exportInfo['date']=datetime.now()



fileChooser=hou.ui.selectFile(
    start_directory=hou.getenv('REPO'),
    title="Node exporter",
    pattern="*.nd",
    default_value="myTree.nd",
    chooser_mode=hou.fileChooserMode.Write
)

export=True

if fileChooser!='':

    if os.path.isfile(fileChooser):
        if hou.ui.displayMessage("Overwrite File ?",('Yes','No',))==1:
            export=False


    if export:
        parentNode.saveItemsToFile(selectedNodes,fileChooser)
        #hou.ui.displayMessage("File exported")

        jsonFile=fileChooser.replace('.nd','.json')
        jsonContents=json.dumps(exportInfo,indent=4,default=str,sort_keys=True)
        open(jsonFile,'w').write(jsonContents)

        hou.ui.setStatusMessage("File exported",hou.severityType.ImportantMessage)
