import os
import sys
import numpy as np
import pydrake

r = pydrake.rbtree.RigidBodyTree()

fname = os.path.join(pydrake.getDrakePath(), "examples/kuka_iiwa_arm/models/iiwa14/iiwa14_simplified_collision.urdf")

urdfString = open(fname, 'r').read()
packageMap = pydrake.rbtree.PackageMap()

baseDir = os.path.dirname(fname)
floatingBaseType = pydrake.rbtree.kRollPitchYaw
weldFrame = None
rbt = pydrake.rbtree.RigidBodyTree()

pydrake.rbtree.AddModelInstanceFromUrdfStringSearchingInRosPackages(
    urdfString,
    packageMap,
    baseDir,
    floatingBaseType,
    weldFrame,
    rbt)

kinsol = rbt.doKinematics(np.zeros((7,1)), np.zeros((7,1)))
