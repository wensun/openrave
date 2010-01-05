#!/usr/bin/env python
# Copyright (C) 2009-2010 Rosen Diankov (rosen.diankov@gmail.com)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. 
from openravepy import *
from numpy import *
from optparse import OptionParser

ghandle = None
def itemselectioncb(link,pos,org,env):
    global ghandle
    print 'in python: body ',link.GetParent().GetName(),':',link.GetName(),'at',reshape(pos,(3))
    ghandle = env.plot3(points=pos,pointsize=25.0,colors=array((1,0,0)))
    return 0

def run():
    parser = OptionParser(description='Shows how to attach a callback to a viewer to perform functions.')
    parser.add_option('--scene',
                      action="store",type='string',dest='scene',default='data/lab1.env.xml',
                      help='OpenRAVE scene to load')
    parser.add_option('--viewer',
                      action="store",type='string',dest='viewer',default='qtcoin',
                      help='Viewer to load')
    (options, args) = parser.parse_args()

    env = Environment()
    env.Load(options.scene)
    env.SetViewer(options.viewer)
    handle = env.GetViewer().RegisterCallback(Viewer.ViewerEvents.ItemSelection,lambda link,pos,org: itemselectioncb(link,pos,org,env))
    if handle is None:
        print 'failed to register handle'
        sys.exit(1)

    while(True):
        cmd = raw_input('In selection mode, click anywhere on the viewer. Enter command (q-quit): ')
        if cmd == 'q':
            break
    handle = None
    env.Destroy() # done with the environment

if __name__=='__main__':
    run()