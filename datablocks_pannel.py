import bpy

class Datablocks_Pannel(bpy.types.Panel):
    bl_idname = "Datablocks_Panel"
    bl_label = "Datablocks"
    bl_category = "Tool"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('view.romove_dublicate_materials', text="Remove Dublicate Materials")