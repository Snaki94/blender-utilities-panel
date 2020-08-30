bl_info = {
    "name" : "Workflow Tools",
    "author" : "Snaki94, Zuorion",
    "description" : "Workflow Tools",
    "blender" : (2, 83, 0),
    "version" : (0, 0, 2),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from .mainPanel import VIEW3D_PT_workflowtools
from .operators import RemoveDublicateMaterials_Operator
from .operators import RemoveAllMaterials_Operator
from .operators import AddTriangulateModifier_Operator
from .operators import RemoveAllUnusedMaterials_Operator
#from .prefs import *

from bpy.props import IntProperty, FloatProperty, BoolProperty, EnumProperty, StringProperty
import rna_keymap_ui
from bpy.types import AddonPreferences



def addmenu_callback(self, context):
    self.layout.operator("object.remove_dublicate_materials")
    self.layout.operator("object.remove_all_materials")

def get_hotkey_entry_item(km, kmi_name):
    for i, km_item in enumerate(km.keymap_items):
        if km.keymap_items.keys()[i] == kmi_name:
            return km_item
    return None

panels = (
        VIEW3D_PT_workflowtools,
        )


def update_panel(self, context):
    message = "WorkflowTools: Updating Panel locations has failed"
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels:
            panel.bl_category = context.preferences.addons[__name__].preferences.category
            bpy.utils.register_class(panel)

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass

class Prefs(AddonPreferences):
    bl_idname = __name__
    
    category: StringProperty(
        name="Tab Category",
        description="Choose a name for the category of the panel",
        default="Edit",
        update=update_panel
        )
    
    def addtomenuupdate(self, context):
        if self.addtomenu:
            bpy.types.MATERIAL_MT_context_menu.append(addmenu_callback)
        else:
            bpy.types.MATERIAL_MT_context_menu.remove(addmenu_callback)
        return
    
    addtomenu: BoolProperty(
        name="Materials menu",
        description="Show operators in material specials menu",
        default=False,
        update=addtomenuupdate
    )
    
    def draw(self, context):
        layout = self.layout
        wm = bpy.context.window_manager
        
        row = layout.row()
        col = row.column()
        col.label(text="Tab Category:")
        col.prop(self, "category", text="")
        
        row = layout.row()
        row.prop(self, "addtomenu", text="Material Operators")
        
        box = layout.box()
        split = box.split()
        col = split.column()
        col.label(text='Hotkey')
        col.separator()
        kc = wm.keyconfigs.user
        km = kc.keymaps['Object Mode']
        #bpy.ops.object.add_triangulate_modifier()
        kmi = get_hotkey_entry_item(km, 'object.add_triangulate_modifier')
        col.context_pointer_set("keymap", km)
        rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
        
        #bpy.types.VIEW3D_MT_object.remove(addmenu_callback)


addon_keymaps = []

classes = (
    VIEW3D_PT_workflowtools,
    RemoveDublicateMaterials_Operator,
    RemoveAllMaterials_Operator,
    AddTriangulateModifier_Operator,
    RemoveAllUnusedMaterials_Operator,
    Prefs
    )

def register():
    from bpy.utils import register_class
    
    for cls in classes:
        register_class(cls)
        
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        # As Ctrl Alt Shift + T
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode')
        kmi = km.keymap_items.new('object.add_triangulate_modifier', 'T', 'PRESS', ctrl=True, alt=True, shift=True)
        kmi.active = False        
        addon_keymaps.append((km, kmi))
    update_panel(None, bpy.context)

def unregister():
    from bpy.utils import unregister_class
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    for cls in reversed(classes):
        unregister_class(cls)
