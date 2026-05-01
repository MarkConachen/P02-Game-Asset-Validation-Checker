import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui


# get Maya main window
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


# helper to add text to report box
def add_report(report_box, message):
    report_box.append(message)


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

    # widgets
    def build_ui(self):
        self.title_label = QtWidgets.QLabel("GAME ASSET CHECKER")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)

        self.report_box = QtWidgets.QTextEdit()
        self.report_box.setReadOnly(True)
        self.report_box.setMinimumHeight(220)

    # layout
    def build_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(QtWidgets.QLabel("Validation Report"))
        main_layout.addWidget(self.report_box)


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