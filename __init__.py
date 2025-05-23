# Dev reload
if "bpy" in locals():
    import sys
    print("Reloading Tracking Toolkit Modules")
    prefix = __package__ + "."
    for name in sys.modules.copy():
        if name.startswith(prefix):
            print(f"Reloading {name}")
            del sys.modules[name]

import bpy

from .tracking_toolkit.operators import (
    CreateRefsOperator,
    ResetTrackersOperator,
    ReloadTrackersOperator,
    ToggleActiveOperator,
    ToggleCalibrationOperator,
    ToggleRecordOperator
)
from .tracking_toolkit.properties import (
    OVRContext,
    OVRTracker,
    OVRTarget,
    OVRTransform,
    Preferences
)
from .tracking_toolkit.ui import PANEL_UL_TrackerList, OpenVRPanel
from .tracking_toolkit.tracking import stop_recording, stop_preview


def register():
    print("Loading Tracking Toolkit")

    # Props
    bpy.utils.register_class(Preferences)
    bpy.utils.register_class(OVRTransform)
    bpy.utils.register_class(OVRTarget)
    bpy.utils.register_class(OVRTracker)
    bpy.utils.register_class(OVRContext)

    # Operators
    bpy.utils.register_class(ToggleCalibrationOperator)
    bpy.utils.register_class(ResetTrackersOperator)
    bpy.utils.register_class(ToggleActiveOperator)
    bpy.utils.register_class(CreateRefsOperator)
    bpy.utils.register_class(ReloadTrackersOperator)
    bpy.utils.register_class(ToggleRecordOperator)

    # Contexts
    bpy.types.Scene.OVRContext = bpy.props.PointerProperty(type=OVRContext)

    # UI
    bpy.utils.register_class(PANEL_UL_TrackerList)
    bpy.utils.register_class(OpenVRPanel)


def unregister():
    print("Unloading Tracking Toolkit...")

    stop_preview()

    # UI
    bpy.utils.unregister_class(PANEL_UL_TrackerList)
    bpy.utils.unregister_class(OpenVRPanel)

    # Contexts
    del bpy.types.Scene.OVRContext

    # Classes
    bpy.utils.unregister_class(ToggleRecordOperator)
    bpy.utils.unregister_class(ReloadTrackersOperator)
    bpy.utils.unregister_class(CreateRefsOperator)
    bpy.utils.unregister_class(ToggleActiveOperator)
    bpy.utils.unregister_class(ResetTrackersOperator)
    bpy.utils.unregister_class(ToggleCalibrationOperator)

    # Props
    bpy.utils.unregister_class(OVRContext)
    bpy.utils.unregister_class(OVRTracker)
    bpy.utils.unregister_class(OVRTarget)
    bpy.utils.unregister_class(OVRTransform)
    bpy.utils.unregister_class(Preferences)

    print("Unloaded Tracking Toolkit")


if __name__ == "__main__":
    register()
