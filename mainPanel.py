import bpy

class MainPanel(bpy.types.Panel):
    bl_idname = "MainPanel"
    bl_label = "Main Panel"
    bl_category = "Tool"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row01 = layout.row()
        row01.operator('object.remove_dublicate_materials', text="Remove Dublicate Materials")
        row02 = layout.row()
        row02.operator('object.add_triangulate_modifier', text="Add Triangulate")