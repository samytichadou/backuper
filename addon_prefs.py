import bpy, os

addon_name = os.path.basename(os.path.dirname(__file__))

class BCKP_PF_addon_prefs(bpy.types.AddonPreferences):
    bl_idname = addon_name

    prefix : bpy.props.StringProperty(name='Prefix',
        description='Backup Prefix, skipped if empty')

    suffix : bpy.props.StringProperty(name='Suffix',
        description='Backup Suffix, skipped if empty')

    custom_folder : bpy.props.StringProperty(name='Custom Folder Name',
        description='Custom Backup Folder Name, skipped if empty')

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "prefix")
        layout.prop(self, "suffix")

# get addon preferences
def get_addon_preferences():
    addon = bpy.context.preferences.addons.get(addon_name)
    return getattr(addon, "preferences", None)


# register
##################################

def register():
    bpy.utils.register_class(BCKP_PF_addon_prefs)

def unregister():
    bpy.utils.unregister_class(BCKP_PF_addon_prefs)
