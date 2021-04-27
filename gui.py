import bpy


def draw_bckp_menu(self, context):

    layout = self.layout

    layout.operator("bckp.create_backup")
    layout.separator()


# register
##################################

def register():
    bpy.types.TOPBAR_MT_file.prepend(draw_bckp_menu)

def unregister():
    bpy.types.TOPBAR_MT_file.remove(draw_bckp_menu)
