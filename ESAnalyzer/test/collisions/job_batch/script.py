#!/usr/bin/python                                                                                                                                                                                                                 

#nRUN = 245192
#nRUN = "MinBias"
nRUN = "XX"
nRUNcut = 245204

import os
currentDir = os.getcwd()
print 'currentDir = %s' %(currentDir)
subDir = currentDir+"/JOB_%s" %(nRUN)
print 'subDir = %s' %(subDir)

outLancia = open('%s/lancia_%s.sh' %(currentDir, nRUN),'w');

num = 0
plusNum = 10000
while num < 2500000:
#for num in range(0,2000):  #to iterate between 10 to 20                                                                                                                                                                          
    outScript = open('%s/bjob_%d.sh' %(subDir, num),'w');
    outScript.write('#!/bin/bash \n');
    outScript.write('cd %s \n' %(subDir));
    outScript.write('export SCRAM_ARCH=slc6_amd64_gcc481 \n');
    outScript.write('eval `scramv1 ru -sh` \n');
    #outScript.write('cd - \n');
    outScript.write('cmsMkdir /store/user/amartell/Commissioning2015/ExpressPhysics/ES_run%s/histo2 \n' %(nRUN));
#    outScript.write('cmsMkdir /store/user/amartell/Commissioning2015/MinimumBias/ES_run%s/histo \n' %(nRUN));
    outScript.write('pwd \n ')
    outScript.write('./../xTimingSensor_All_temp  %s %d %d %d \n' %( nRUN, num, num+plusNum, nRUNcut) );
    outScript.write('cmsStage coll_timing_Run%s_%d_%d-%d.root /store/user/amartell/Commissioning2015/ExpressPhysics/ES_run%s/histo2/' %(nRUN, nRUNcut, num, num+plusNum, nRUN));
 #   outScript.write('cmsStage coll_timing_Run%s_%d-%d.root /store/user/amartell/Commissioning2015/MinimumBias/ES_run%s/histo' %(nRUN, num, num+10000, nRUN));
    outScript.write( '\n ' );
    os.system('chmod 777 %s/bjob_%d.sh' %(subDir, num));
    outLancia.write(' bsub -cwd %s -q cmscaf1nd %s/bjob_%d.sh \n' %(subDir, subDir, num));
    num += plusNum


