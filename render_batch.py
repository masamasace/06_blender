from pathlib import Path
import bpy
import itertools

devices = bpy.context.preferences.addons['cycles'].preferences.devices
if devices is not None:
    for i, device in enumerate(devices):
        print("Device {}: {}".format(i, device.name))
else:
    print("No devices found.")

# 利用するデバイスを全てOFFに初期設定
devices = bpy.context.preferences.addons['cycles'].preferences.devices
for device in devices:
    device.use = False

# GPUを指定
devices[0].use = True

# レンダリング設定
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.device = 'GPU'

# ファイルの読み込み
bpy.ops.wm.open_mainfile(filepath=str(Path("street_model.blend").resolve()))
scene = bpy.context.scene
camera = bpy.data.objects['Camera']

# resolution tuple and z location tuple
resolutions = [(1920, 1080), (2560, 1440), (3840, 2160), (6144, 3072), (3072, 1536), (1536, 768)]
z_locations = [1, 3, 5]

for resolution, z_location in itertools.product(resolutions, z_locations):

    scene.render.resolution_x = resolution[0]
    scene.render.resolution_y = resolution[1]

    # print tranfrom location of all the keyframes
    for fcurve in camera.animation_data.action.fcurves:
        if fcurve.data_path == "location":
            for keyframe_point in fcurve.keyframe_points:
                print(keyframe_point.co)

    # update the camera location by changing  keyframe_point.co
    for fcurve in camera.animation_data.action.fcurves:
        if fcurve.data_path == "location" and fcurve.array_index == 2:
            for keyframe_point in fcurve.keyframe_points:
                keyframe_point.co[1] = z_location

    for fcurve in camera.animation_data.action.fcurves:
        if fcurve.data_path == "location":
            for keyframe_point in fcurve.keyframe_points:
                print(keyframe_point.co)

    # check camera location
    bpy.context.scene.frame_set(0)
    bpy.context.view_layer.update()

    scene.render.filepath = str(Path("output").resolve()) + "/{}x{}_h{}_".format(resolution[0], resolution[1], z_location)
    scene.render.image_settings.file_format = 'PNG'
    bpy.ops.render.render(write_still=True, animation=True)


