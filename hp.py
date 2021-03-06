import paperspace
paperspace.config.PAPERSPACE_API_KEY = '...'

gpuTypes = ['P5000', 'V100']
epochs = [10,100,500]
n=0

for gpuType in gpuTypes:
  for ep in epochs:
    print "job " + str(n)
    n=n+1
    runcmd = 'python main.py --epochs ' + str(ep)
    paperspace.jobs.create({'workspace': 'main.py' ,'command': runcmd, 'project': 'myproject', 'machineType': gpuType, 'container': 'paperspace/pytorch'}, no_logging=True)
