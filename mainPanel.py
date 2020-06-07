import bpy

class MainPanel(bpy.types.Panel):
    bl_idname = "MainPanel"
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

        rowTriangulate = layout.row()
        rowTriangulate.operator('object.add_triangulate_modifier', text="Add Triangulate")