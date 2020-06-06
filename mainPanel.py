import bpy

class MainPanel(bpy.types.Panel):
    bl_idname = "MainPanel"
    bl_label = "Main Panel"
    bl_category = "Tool"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('view.romove_dublicate_materials', text="Remove Dublicate Materials")