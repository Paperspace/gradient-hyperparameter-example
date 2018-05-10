import paperspace
paperspace.config.PAPERSPACE_API_KEY = '...'

gpuTypes = ['P5000', 'K80']
epochs = [0,10]
n=0

for gpuType in gpuTypes:
  for ep in epochs:
    print "job " + str(n)
    n=n+1
    runcmd = 'python main.py --epochs ' + str(ep)
    paperspace.jobs.create({'command': runcmd, 'project': 'myproject', 'machineType': gpuType, 'container': 'paperspace/pytorch'}, no_logging=True)
