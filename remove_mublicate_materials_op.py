import bpy

class RemoveDublicateMaterials_Operator(bpy.types.Operator):
    bl_idname = "view.romove_dublicate_materials"
    bl_label = "Remove Dublicate Materials"
    bl_description = "Remove dublicate materials from the object"

    def execute(sel, context):
        mat_list = [x.material.name for x in bpy.context.object.material_slots]
        remove_slots = []
        
        bpy.ops.object.mode_set(mode='OBJECT')

        for s in bpy.context.object.material_slots:
             if s.material.name[-3:].isnumeric():
                 if s.material.name[:-4] in mat_list:
                     index_clean = mat_list.index(s.material.name[:-4])
                     index_wrong = mat_list.index(s.material.name)
                     print(index_wrong, index_clean)
                     faces = [x for x in bpy.context.object.data.polygons if x.material_index == index_wrong]

                     for f in faces:
                         f.material_index = index_clean
                     remove_slots.append(s.name)
        for s in remove_slots:
            if s in [x.name for x in bpy.context.object.material_slots]:
                print('removing slot %s' % s)
                bpy.context.object.active_material_index = [x.material.name for x in bpy.context.object.material_slots].index(s)
                bpy.ops.object.material_slot_remove()


        return {'FINISHED'}