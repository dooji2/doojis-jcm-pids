import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QLabel,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer
from mainui import Ui_MainWindow
from mainui import InfoBar, InfoBarPosition, StateToolTip
from qfluentwidgets.components.widgets.state_tool_tip import StateToolTip
from qfluentwidgets import (
    CaptionLabel,
    CheckBox,
    LineEdit,
    PushButton,
    StateToolTip,
    SwitchButton,
    TabBar,
    InfoBar,
    InfoBarIcon,
    InfoBarPosition,
    ImageLabel,
)


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.last_tab_index = 0

        warning_msg = QMessageBox(self)
        warning_msg.setIcon(QMessageBox.Warning)
        warning_msg.setWindowTitle("Warning")
        warning_msg.setText("This program is still in early development.")
        warning_msg.setInformativeText(
            "Developed by Dooji for use with JCM by LX86\n\n"
            "Please use with caution and report any issues or suggestions."
        )
        warning_msg.setStandardButtons(QMessageBox.Ok)
        warning_msg.exec_()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedSize(1036, 520)

        self.ui.new.clicked.connect(self.create_new_file)

        self.state_tooltip = StateToolTip("", "", parent=self)
        self.state_tooltip.hide()

        self.ui.TabBar.tabAddRequested.connect(self.create_new_template)

        self.ui.TabBar.tabCloseRequested.connect(self.close_tab_requested)

        self.ui.TabBar.currentChanged.connect(self.update_template_details)

        self.ui.save.clicked.connect(self.save_changes)

        self.ui.load.clicked.connect(self.load_file)

        self.connect_signals()

        self.json_data = {"pids_images": []}
        self.current_file_name = None

        self.disable_buttons()

    def disable_buttons(self):
        self.ui.save.setEnabled(False)
        self.ui.TabBar.setEnabled(False)

        self.ui.line1t.setEnabled(False)
        self.ui.line2t.setEnabled(False)
        self.ui.line3t.setEnabled(False)
        self.ui.line4t.setEnabled(False)
        self.ui.tempin.setEnabled(False)
        self.ui.backin.setEnabled(False)
        self.ui.colorin.setEnabled(False)
        self.ui.checkweather.setEnabled(False)
        self.ui.checkclock.setEnabled(False)

    def enable_buttons(self):
        self.ui.save.setEnabled(True)
        self.ui.load.setEnabled(True)
        self.ui.TabBar.setEnabled(True)

        self.ui.line1t.setEnabled(True)
        self.ui.line2t.setEnabled(True)
        self.ui.line3t.setEnabled(True)
        self.ui.line4t.setEnabled(True)
        self.ui.tempin.setEnabled(True)
        self.ui.backin.setEnabled(True)
        self.ui.colorin.setEnabled(True)
        self.ui.checkweather.setEnabled(True)
        self.ui.checkclock.setEnabled(True)

    def connect_signals(self):
        self.ui.line1t.checkedChanged.connect(
            lambda: self.handle_checked_changed(self.ui.line1t)
        )
        self.ui.line2t.checkedChanged.connect(
            lambda: self.handle_checked_changed(self.ui.line2t)
        )
        self.ui.line3t.checkedChanged.connect(
            lambda: self.handle_checked_changed(self.ui.line3t)
        )
        self.ui.line4t.checkedChanged.connect(
            lambda: self.handle_checked_changed(self.ui.line4t)
        )
        self.ui.checkweather.stateChanged.connect(self.handle_weather_state_changed)
        self.ui.checkclock.stateChanged.connect(self.handle_clock_state_changed)

    def handle_checked_changed(self, checkbox):
        if not self.current_file_name:
            return

        template = self.get_current_template()
        if template:
            background_path = template["background"]
            self.load_and_display_image(
                self.current_file_name, background_path, 600, 193
            )
        else:
            print("No template selected.")

    def handle_weather_state_changed(self, state):
        if not self.current_file_name:
            return

        template = self.get_current_template()
        if template:
            background_path = template["background"]
            self.load_and_display_image(
                self.current_file_name, background_path, 600, 193
            )
        else:
            print("No template selected.")

    def handle_clock_state_changed(self, state):
        if not self.current_file_name:
            return

        template = self.get_current_template()
        if template:
            background_path = template["background"]
            self.load_and_display_image(
                self.current_file_name, background_path, 600, 193
            )
        else:
            print("No template selected.")

    def get_current_template(self):
        current_tab_index = self.ui.TabBar.currentIndex()
        if current_tab_index >= 0 and current_tab_index < len(
            self.json_data["pids_images"]
        ):
            return self.json_data["pids_images"][current_tab_index]
        else:
            return None

    def create_new_template(self):
        if not self.json_data:
            self.create_new_file()
        else:
            new_template = {
                "id": "NewTemplate",
                "showWeather": False,
                "showClock": False,
                "hideRow": [False, False, False, False],
                "background": "",
                "color": "000000",
            }

            self.json_data["pids_images"].append(new_template)

            tab = QWidget()
            tab.setObjectName(new_template["id"])

            self.add_widgets_to_tab(tab, new_template)

            self.ui.TabBar.addTab(tab, new_template["id"])

            self.update_widget_data(new_template, tab)

            success_info_bar = InfoBar.success(
                "Success",
                "Created a new template!",
                position=InfoBarPosition.TOP_RIGHT,
                parent=self,
            )
            success_info_bar.show()

    def create_new_file(self):
        file_dialog = QFileDialog()
        file_name, _ = file_dialog.getSaveFileName(
            self, "Create New File", "", "JSON Files (*.json)"
        )

        if not file_name:
            error_info_bar = InfoBar.error(
                "Error",
                "Action canceled!",
                position=InfoBarPosition.TOP_RIGHT,
                parent=self,
            )
            error_info_bar.show()
            return

        self.current_file_name = file_name

        new_template = {
            "id": "NewTemplate",
            "showWeather": False,
            "showClock": False,
            "hideRow": [False, False, False, False],
            "background": "",
            "color": "000000",
        }

        self.json_data["pids_images"].append(new_template)

        tab = QWidget()
        tab.setObjectName(new_template["id"])

        self.add_widgets_to_tab(tab, new_template)

        self.ui.TabBar.addTab(tab, new_template["id"])

        success_info_bar = InfoBar.success(
            "Success",
            "Created a new file!",
            position=InfoBarPosition.TOP_RIGHT,
            parent=self,
        )
        success_info_bar.show()

        self.enable_buttons()

    def load_file(self):
        if self.json_data["pids_images"] and self.is_unsaved_changes():
            result = self.show_unsaved_changes_prompt()
            if result == QMessageBox.Save:
                self.save_changes()

        file_dialog = QFileDialog()
        file_name, _ = file_dialog.getOpenFileName(
            self, "Load File", "", "JSON Files (*.json)"
        )

        if not file_name:
            return

        with open(file_name, "r") as file:
            self.json_data = json.load(file)

        self.current_file_name = file_name

        while self.ui.TabBar.count() > 0:
            self.ui.TabBar.removeTab(0)

        for template in self.json_data["pids_images"]:
            tab = QWidget()
            tab.setObjectName(template["id"])
            self.add_widgets_to_tab(tab, template)
            self.ui.TabBar.addTab(tab, template["id"])

        if self.ui.TabBar.count() > 0:
            self.ui.TabBar.setCurrentIndex(0)

        success_info_bar = InfoBar.success(
            "Success", "Loaded a file!", position=InfoBarPosition.TOP_RIGHT, parent=self
        )
        success_info_bar.show()

        self.enable_buttons()

        background_path = self.json_data["pids_images"][0]["background"]

    def add_widgets_to_tab(self, tab, template):
        background_image_label = ImageLabel(tab)
        background_image_label.setGeometry(600, 70, 400, 400)

        background_file_name = os.path.join(
            os.path.dirname(self.current_file_name),
            template["background"].split(":")[-1],
        )

        background_image_label.setPixmap(QPixmap(background_file_name))

        pixmap = QPixmap(background_file_name)
        if pixmap.isNull():
            print("")

        else:
            window_width = self.width()
            window_height = self.height()

            image_width = pixmap.width()
            image_height = pixmap.height()

            x_position = (window_width - image_width) // 2
            y_position = (window_height - image_height) // 2

            x_position = max(0, x_position)
            y_position = max(0, y_position)

            background_image_label.setGeometry(
                x_position, y_position, image_width, image_height
            )
            background_image_label.setVisible(True)

        template_name_label = QLabel(f"Template Name: {template['id']}")
        show_weather_label = QLabel(f"Show Weather: {template['showWeather']}")
        show_clock_label = QLabel(f"Show Clock: {template['showClock']}")
        hide_row_labels = [
            QLabel(f"Hide Row {i+1}: {template['hideRow'][i]}")
            for i in range(len(template["hideRow"]))
        ]
        background_label = QLabel(f"Background: {template['background']}")
        color_label = QLabel(f"Color: {template['color']}")

        layout = QVBoxLayout()
        layout.addWidget(template_name_label)
        layout.addWidget(show_weather_label)
        layout.addWidget(show_clock_label)
        layout.addStretch(1)
        layout.addWidget(color_label)

        for hide_row_label in hide_row_labels:
            layout.addWidget(hide_row_label)

        tab.setLayout(layout)

        self.update_widget_data(template, tab)

    def update_template_details(self, index):
        template = self.json_data["pids_images"][index]

        current_tab_index = self.ui.TabBar.currentIndex()

        if current_tab_index >= 0 and current_tab_index < len(self.ui.TabBar.items):
            current_tab = self.ui.TabBar.items[current_tab_index]

            current_tab_widget = current_tab

            background_file_name = os.path.join(
                os.path.dirname(self.current_file_name),
                template["background"].split(":")[-1],
            )

            self.ui.line1t.setChecked(not template["hideRow"][0])
            self.ui.line2t.setChecked(not template["hideRow"][1])
            self.ui.line3t.setChecked(not template["hideRow"][2])
            self.ui.line4t.setChecked(not template["hideRow"][3])

            self.ui.checkweather.setChecked(template["showWeather"])
            self.ui.checkclock.setChecked(template["showClock"])

            self.ui.tempin.setText(template["id"])
            self.ui.backin.setText(template["background"])
            self.ui.colorin.setText(template["color"])

            self.update_widget_data(template, current_tab_widget)

            image_window = getattr(self, "image_window", None)
            if image_window is None:
                self.load_and_display_image(
                    self.current_file_name, template["background"], 600, 193
                )
            else:
                self.load_and_display_image(
                    self.current_file_name, template["background"], 600, 193
                )

    def load_and_display_image(
        self, json_file_path, background_path, x_position, y_position
    ):
        if not background_path:
            return

        full_path = os.path.join(
            os.path.dirname(json_file_path), background_path.split(":")[-1]
        )

        if not os.path.exists(full_path):
            print(f"File does not exist at path: {full_path}")
            return

        pixmap = QPixmap(full_path)
        if not pixmap.isNull():
            if not hasattr(self, "overlay_image_label"):
                self.overlay_image_label = QLabel(self)
                self.overlay_image_label.setGeometry(
                    x_position, y_position, self.width(), self.height()
                )
            else:
                self.overlay_image_label.setGeometry(
                    x_position,
                    y_position,
                    self.overlay_image_label.width(),
                    self.overlay_image_label.height(),
                )

            window_width = self.width()
            image_width = int(window_width * 0.4)
            image_height = int(image_width * pixmap.height() / pixmap.width())

            self.overlay_image_label.setPixmap(pixmap.scaled(image_width, image_height))
            self.overlay_image_label.setVisible(True)
            self.overlay_image_label.raise_()

            x_position = max(0, min(x_position, self.width() - image_width))
            y_position = max(0, min(y_position, self.height() - image_height))
            self.overlay_image_label.setGeometry(
                x_position, y_position, image_width, image_height
            )

            other_images = [
                "line1.png",
                "line2.png",
                "line3.png",
                "line4.png",
                "weather.png",
                "clock.png",
            ]
            for i, image_path in enumerate(other_images):
                if i < 4:
                    if self.ui.__dict__[f"line{i + 1}t"].isChecked():
                        other_image_label = QLabel(self)
                        other_image_label.setGeometry(
                            x_position, y_position, image_width, image_height
                        )
                        other_image_label.setPixmap(
                            QPixmap(image_path).scaled(image_width, image_height)
                        )
                        other_image_label.setVisible(True)
                        other_image_label.raise_()
                elif i == 4:
                    if self.ui.checkweather.isChecked():
                        other_image_label = QLabel(self)
                        other_image_label.setGeometry(
                            x_position, y_position, image_width, image_height
                        )
                        other_image_label.setPixmap(
                            QPixmap(image_path).scaled(image_width, image_height)
                        )
                        other_image_label.setVisible(True)
                        other_image_label.raise_()
                elif i == 5:
                    if self.ui.checkclock.isChecked():
                        other_image_label = QLabel(self)
                        other_image_label.setGeometry(
                            x_position, y_position, image_width, image_height
                        )
                        other_image_label.setPixmap(
                            QPixmap(image_path).scaled(image_width, image_height)
                        )
                        other_image_label.setVisible(True)
                        other_image_label.raise_()
        else:
            return

    def update_widget_data(self, template, tab):
        for i in range(4):
            hide_row_label_name = f"Hide Row {i+1}"

    def save_changes(self):
        current_tab_index = self.ui.TabBar.currentIndex()

        current_template = self.json_data["pids_images"][current_tab_index]

        current_template["hideRow"] = [
            self.ui.line1t.isChecked(),
            self.ui.line2t.isChecked(),
            self.ui.line3t.isChecked(),
            self.ui.line4t.isChecked(),
        ]
        current_template["showWeather"] = self.ui.checkweather.isChecked()
        current_template["showClock"] = self.ui.checkclock.isChecked()

        current_template["id"] = self.ui.tempin.text()
        current_template["background"] = self.ui.backin.text()
        current_template["color"] = self.ui.colorin.text()

        if self.current_file_name:
            reply = QMessageBox.question(
                self,
                "Confirm Save",
                f"Do you really want to save changes to '{self.current_file_name}'?",
                QMessageBox.Yes | QMessageBox.Cancel,
                QMessageBox.Yes,
            )
            if reply == QMessageBox.Yes:
                with open(self.current_file_name, "w") as file:
                    json.dump(self.json_data, file, indent=4)

                success_info_bar = InfoBar.success(
                    "Success",
                    "Saved successfully!",
                    position=InfoBarPosition.TOP_RIGHT,
                    parent=self,
                )
                success_info_bar.show()

    def close_tab_requested(self, index):
        template = self.json_data["pids_images"][index]

        reply = QMessageBox.question(
            self,
            "Confirm Close",
            f"Do you really want to close the tab and delete the template '{template['id']}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.ui.TabBar.removeTab(index)
            del self.json_data["pids_images"][index]

            self.save_changes()

    def is_unsaved_changes(self):
        return self.current_file_name and self.ui.TabBar.count() > 0

    def show_unsaved_changes_prompt(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("There are unsaved changes. Do you want to save them?")
        msg_box.setStandardButtons(
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        msg_box.setDefaultButton(QMessageBox.Save)
        result = msg_box.exec_()
        return result

    def resizeEvent(self, event):
        window_width = self.width()
        window_height = self.height()

        if hasattr(self, "overlay_image_label"):
            pixmap = self.overlay_image_label.pixmap()
            if not pixmap.isNull():
                image_width = int(window_width * 0.6)
                image_height = int(image_width * pixmap.height() / pixmap.width())

                x_position = (window_width - image_width) // 2
                y_position = (window_height - image_height) // 2

                self.overlay_image_label.setGeometry(
                    x_position, y_position, image_width, image_height
                )

        super().resizeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()

    sys.exit(app.exec_())
