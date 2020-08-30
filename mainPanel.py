import bpy

class VIEW3D_PT_workflowtools(bpy.types.Panel):
    bl_label = "Main Panel"
    bl_category = "Tool"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        rowDublicateMat = layout.row()
        rowDublicateMat.operator('object.remove_dublicate_materials', text="Remove Dublicate Materials")
        
        rowRemoveAll = layout.row()
        rowRemoveAll.operator('object.remove_all_materials', text="Remove All Materials")

        rowRemoveUnused = layout.row()
        rowRemoveUnused.operator('object.remove_unused_materials', text="Remove Unslot Materials")

        rowTriangulate = layout.row()
        rowTriangulate.operator('object.add_triangulate_modifier', text="Add Triangulate")