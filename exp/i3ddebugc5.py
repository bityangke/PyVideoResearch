#!/usr/bin/env python
import sys
import pdb
import traceback
#sys.path.insert(0, '..')
sys.path.insert(0, '.')
from main import main
from bdb import BdbQuit
import os
os.nice(19)
import subprocess
subprocess.Popen('find ./exp/.. -iname "*.pyc" -delete'.split())

args = [
    '--name', __file__.split('/')[-1].split('.')[0],  # name is filename
    '--print-freq', '1',
    '--dataset', 'charadesrgbvideo',
    '--arch', 'aj_i3d',
    '--lr', '.25e-2',
    '--lr-decay-rate', '8',
    '--epochs', '20',
    '--memory-decay', '1.0',
    '--memory-size', '20',
    '--batch-size', '2',
    '--train-size', '1.0',
    '--temporal-weight', '0.0000001',
    '--temporalloss-weight', '1.2',
    '--window-smooth', '0',
    '--sigma', '300',
    '--val-size', '0.2',
    '--cache-dir', '/nfs.yoda/gsigurds/ai2/caches/',
    '--data', '/scratch/gsigurds/Charades_v1_rgb/',
    '--train-file', '/home/gsigurds/ai2/twostream/Charades_v1_train.csv',
    '--val-file', '/home/gsigurds/ai2/twostream/Charades_v1_test.csv',
    '--pretrained',
    #'--adjustment',
    '--balanceloss',
    '--nhidden', '3',
    #'--synchronous',
    '--originalloss-weight', '15',
    #'--videoloss',
    '--resume', '/nfs.yoda/gsigurds/charades_pretrained/aj_rgb_charades.pth',
    #'--resume', '/glusterfs/gsigurds/ai2/caches/' + __file__.split('/')[-1].split('.')[0] + '/model.pth.tar',
    #'--evaluate',
    '--workers', '4',
]
sys.argv.extend(args)
try:
    main()
except BdbQuit:
    sys.exit(1)
except Exception:
    traceback.print_exc()
    print ''
    pdb.post_mortem()
    sys.exit(1)
