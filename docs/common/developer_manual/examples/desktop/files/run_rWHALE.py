from agavepy.agave import Agave
ag = Agave.restore()
rWHALE = ag.apps.get(appId='rWhale-2.1.0') #



first_ID = 1

bpt = 2  # buildings per task
tpn = 1  # task per node

kind = 'KNL'
#kind = 'SKX'

if kind == 'KNL':
    nodes = 4
    ppn = 64
    #ppn = 10
    #queue = 'development'
    queue = 'normal'
elif 'SKX':
    nodes = 1
    ppn=48
    #ppn = 10
    queue = 'skx-dev'
    #queue = 'skx-normal'

jobdetails = {
	"name": f"RDT_{nodes*bpt*ppn*tpn}_{nodes}_{bpt}x{tpn}_{kind}_{first_ID}",
	"appId": "rWhale-2.1.0",
    # "rWhale-2.1.0"
    #"appId": "rWHALE_Adam-2.0.2",
	"maxRunTime": "00:20:00",
	"nodeCount": nodes,
    "processorsPerNode": nodes*ppn,
    "batchQueue": queue,
	"archive": True,
	"archiveSystem": "designsafe.storage.default",
	"parameters": {
        "buildingsCount": '20',
        "buildingsPerTask": f'{bpt}',
        "firstBuilding": f'{first_ID}'
    },
	"inputs": {
        "dataFiles": ["agave://designsafe.storage.default/UserName/input_data.zip",
                      "agave://designsafe.storage.default/UserName/CreateLauncherTasks.py"],
        "configFile": "agave://designsafe.storage.default/UserName/rWHALE_config.json"


		}
}
jobdetails




job = ag.jobs.submit(body=jobdetails)
job
