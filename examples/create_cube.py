import bpy

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Add a cube
bpy.ops.mesh.primitive_cube_add(size=2)

# Save the scene
bpy.ops.wm.save_as_mainfile(filepath="output.blend")
