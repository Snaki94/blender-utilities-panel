bl_info = {
    "name" : "CleanDublicateMaterials",
    "author" : "Snaki94",
    "description" : "Clean dublicate materials from object",
    "blender" : (2, 82, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from . remove_mublicate_materials_op import RemoveDublicateMaterials_Operator
from . datablocks_pannel import Datablocks_Pannel

classes = (RemoveDublicateMaterials_Operator, Datablocks_Pannel)

register, unregister = bpy.utils.register_classes_factory(classes)