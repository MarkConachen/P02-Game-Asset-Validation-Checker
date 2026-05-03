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


# check bad name characters
def has_invalid_name(obj):
    invalid_chars = [" ", "-", ".", ":", ";"]

    for char in invalid_chars:
        if char in obj:
            return True

    return False


# check rotation and scale
def has_bad_transforms(obj):
    rotate = cmds.getAttr(obj + ".rotate")[0]
    scale = cmds.getAttr(obj + ".scale")[0]

    if rotate != (0, 0, 0):
        return True

    if scale != (1, 1, 1):
        return True

    return False


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

        # checkboxes
        self.name_checkbox = QtWidgets.QCheckBox("Check Names")
        self.name_checkbox.setChecked(True)

        self.transform_checkbox = QtWidgets.QCheckBox("Check Rotation and Scale")
        self.transform_checkbox.setChecked(True)

        # button
        self.validate_button = QtWidgets.QPushButton("Run Validation")

        # report box
        self.report_box = QtWidgets.QTextEdit()
        self.report_box.setReadOnly(True)
        self.report_box.setMinimumHeight(220)

    # layout
    def build_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)

        main_layout.addWidget(self.title_label)

        main_layout.addWidget(QtWidgets.QLabel("Validation Checks"))
        main_layout.addWidget(self.name_checkbox)
        main_layout.addWidget(self.transform_checkbox)

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

        total_issues = 0

        for obj in selection:
            add_report(self.report_box, "")
            add_report(self.report_box, "Object: " + obj)

            issues = 0

            # name checks (only if checkbox is on)
            if self.name_checkbox.isChecked():
                if has_default_name(obj):
                    add_report(self.report_box, "- Warning: Object has a default Maya name.")
                    issues += 1
                elif has_invalid_name(obj):
                    add_report(self.report_box, "- Warning: Object name contains invalid characters.")
                    issues += 1
                else:
                    add_report(self.report_box, "- Naming check passed.")

            # transform check (only if checkbox is on)
            if self.transform_checkbox.isChecked():
                if has_bad_transforms(obj):
                    add_report(self.report_box, "- Warning: Rotation or scale is not frozen.")
                    issues += 1
                else:
                    add_report(self.report_box, "- Transform check passed.")

            # result per object
            if issues == 0:
                add_report(self.report_box, "- Result: Asset passed current checks.")
            else:
                add_report(self.report_box, "- Result: " + str(issues) + " issue(s) found.")

            total_issues += issues

        add_report(self.report_box, "")
        add_report(self.report_box, "-------------------------")
        add_report(self.report_box, "Total issues found: " + str(total_issues))


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