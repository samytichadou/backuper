import bpy, os, shutil

from .addon_prefs import get_addon_preferences


def find_version(filedir, pattern):
    version_list = []
    for filename in os.listdir(filedir):
        if pattern in filename:
            filename_noext = os.path.splitext(filename)[0]
            version_list.append(int(filename_noext.split(pattern)[1]))
    if version_list:
        version = str(max(version_list) + 1).zfill(5)
    else:
        version = "0".zfill(5)
    return version


def save_backup(prefix, suffix, backup_folder):
    if not bpy.data.filepath:
        return False

    #construct filepath
    old_filepath = bpy.data.filepath
    old_filedir = os.path.dirname(old_filepath)
    old_filename = os.path.splitext(os.path.basename(old_filepath))[0]

    #filedir
    if backup_folder:
        filedir = os.path.join(old_filedir, backup_folder)
        if not os.path.isdir(filedir):
            os.mkdir(filedir)
    else:
        filedir = old_filedir

    #filename
    if prefix:
        if prefix.endswith("_"):
            new_filename = prefix + old_filename
        else:
            new_filename = prefix + "_" + old_filename
    if suffix:
        if suffix.startswith("_"):
            new_filename += suffix
        else:
            new_filename += "_" + suffix
    new_filename += "_"

    #version number
    version = find_version(filedir, new_filename)

    new_filename += version

    new_filename += ".blend"

    #filepath
    new_filepath = os.path.join(filedir, new_filename)

    #save
    bpy.ops.wm.save_mainfile(filepath=old_filepath)

    #copy backup file
    shutil.copy2(old_filepath, new_filepath)

    return True


class BCKP_OT_create_backup(bpy.types.Operator):
    """Create a Backup File"""
    bl_idname = "bckp.create_backup"
    bl_label = "Save Backup"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return bpy.data.filepath

    def execute(self, context):
        prefs = get_addon_preferences()

        if save_backup(prefs.prefix, prefs.suffix, prefs.custom_folder):
            print("Backuper --- Backup Done")
        else:
            print("Backuper --- Backup Failed")

        return {'FINISHED'}


# register
##################################

def register():
    bpy.utils.register_class(BCKP_OT_create_backup)

def unregister():
    bpy.utils.unregister_class(BCKP_OT_create_backup)
