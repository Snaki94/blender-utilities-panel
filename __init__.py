bl_info = {
    "name" : "Snaki Workflow Tools",
    "author" : "Snaki94",
    "description" : "..,",
    "blender" : (2, 83, 0),
    "version" : (0, 0, 2),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from .mainPanel import MainPanel
from .operators import RemoveDublicateMaterials_Operator
from .operators import AddTriangulateModifier_Operator

classes = (
    MainPanel,
    RemoveDublicateMaterials_Operator,
    AddTriangulateModifier_Operator,
)

register, unregister = bpy.utils.register_classes_factory(classes)