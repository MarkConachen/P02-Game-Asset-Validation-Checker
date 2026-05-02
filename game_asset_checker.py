import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui


# get Maya main window
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# get selected transform objects
def get_selection():
    return cmds.ls(selection=True, type="transform")


# helper to add text to report box
def add_report(report_box, message):
    report_box.append(message)


# check default maya names
def has_default_name(obj):
    default_names = ("pCube", "pSphere", "pCylinder", "pPlane", "polySurface")
    return obj.startswith(default_names)


# UI class
class GameAssetCheckerUI(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_window()):
        super(GameAssetCheckerUI, self).__init__(parent)

        self.setWindowTitle("Game Asset Checker")
        self.setMinimumWidth(400)

        # remove the question mark button
        self.setWindowFlags(
            self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint
        )

        # build UI
        self.build_ui()
        self.build_layout()
        self.connect_ui()

    # widgets
    def build_ui(self):
        self.title_label = QtWidgets.QLabel("GAME ASSET CHECKER")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.validate_button = QtWidgets.QPushButton("Run Validation")

        self.report_box = QtWidgets.QTextEdit()
        self.report_box.setReadOnly(True)
        self.report_box.setMinimumHeight(220)

    # layout
    def build_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.validate_button)
        main_layout.addWidget(QtWidgets.QLabel("Validation Report"))
        main_layout.addWidget(self.report_box)

    # connect buttons
    def connect_ui(self):
        self.validate_button.clicked.connect(self.run_validation)

    # run validation
    def run_validation(self, *args):
        self.report_box.clear()

        selection = get_selection()

        if not selection:
            add_report(self.report_box, "No objects selected.")
            cmds.warning("No objects selected.")
            return

        add_report(self.report_box, "VALIDATION REPORT")
        add_report(self.report_box, "-------------------------")

        for obj in selection:
            add_report(self.report_box, "")
            add_report(self.report_box, "Object: " + obj)

            if has_default_name(obj):
                add_report(self.report_box, "- Warning: Object has a default Maya name.")
            else:
                add_report(self.report_box, "- Naming check passed.")


# show window
def show_window():
    global asset_checker_ui

    try:
        asset_checker_ui.close()
        asset_checker_ui.deleteLater()
    except:
        pass

    asset_checker_ui = GameAssetCheckerUI()
    asset_checker_ui.show()


# run the tool
if __name__ == "__main__":
    show_window()