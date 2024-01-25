import bpy

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Add a cube
bpy.ops.mesh.primitive_cube_add(size=2)

# Set up rendering settings
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = "image.png"

# Render the scene
bpy.ops.render.render(write_still=True)
