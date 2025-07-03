import os
import sys

mlip_path  = "/home/king/MTP/MLIP/mlip-2-master/bin"

os.mkdir('A-ready')
os.chdir('A-ready')
os.system('cp ../new.cfg .')
os.system('cp ../mlip.ini .')
os.system('cp ../pot.mtp .')
os.system('%s/mlp calc-grade pot.mtp new.cfg new.cfg temp.cfg --als-filename=A-state.als' % mlip_path)
os.system('echo "Step A clear"')
os.chdir('../')

os.mkdir('B-relax')
os.chdir('B-relax')
os.system('cp ../mlip.ini .')
os.system('cp ../new.cfg .')
os.system('cp ../pot.mtp .')
os.system('cp ../A-ready/A-state.als .')
os.system('%s/mlp relax mlip.ini --cfg-filename=new.cfg --iteration-limit=1 --save-relaxed=relaxed.cfg > relax-output.txt' % mlip_path )
os.system('cat B-preselected.cfg* > ../B-preselected.cfg')
os.system('echo "Step B clear"')
os.chdir('../')

os.mkdir('C-select')
os.chdir('C-select')
os.system('cp ../pot.mtp .')
os.system('cp ../train.cfg .')
os.system('cp ../B-preselected.cfg .')
os.system('%s/mlp select-add pot.mtp train.cfg B-preselected.cfg C-selected.cfg > select-output.txt' % mlip_path)
os.system('cp C-selected.cfg ../C-selected.cfg')
os.chdir('../')
job_chk = int(os.popen('grep -c BEGIN C-selected.cfg').read())
if job_chk == 0:
    os.system('echo "------------------------------------------------------------"')
    os.system('echo "   No more selected configurations. Iterations are finished!"')
    os.system('echo "------------------------------------------------------------"')
    exit()
os.system('echo "---------------------------------------------------------------"')
os.system('echo "    %s configurations are selected. Iterations are continued..."' % job_chk )
os.system('echo "---------------------------------------------------------------"')
os.system('echo "Step C clear"')


