# Importing libraries:
import sys
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
import pymongo

# Importing local modules:
from ui.Window import Ui_MainWindow
from modules import mongodb_CRUD


class MainWindow(QMainWindow, Ui_MainWindow):
    """Class for the Main window"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

        self.all_mongodb_results = []

    def populate_table(self, data):
        """Add data to table"""

        self.tableWidget.setRowCount(0)  # Clear table
        self.tableWidget.setRowCount(len(data))  # Set number of rows to length of data
        row = 0
        for record in data:
            for col in range(0, 5):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(record[col])))
            row += 1

    def display_results(self):
        """Display query results to UI"""

        self.label_total_results.setText(str(len(self.all_mongodb_results)))

        table_data = []

        for row in self.all_mongodb_results:
            table_data.append(
                [
                    row["_id"],
                    row["meta-title"],
                    row["meta-site-name"],
                    len(row["urlsfound"]),
                    row["imported"],
                ]
            )

        limit_results = self.checkBox.isChecked()
        limit_value = self.spinBox.value()

        # Populate table depending on limit settings
        if limit_results:
            self.populate_table(table_data[0:limit_value])
        else:
            self.populate_table(table_data)

    def check_query(self):
        """Check if query field is empty.
        This will prevent searching if text field is empty
        while we are changing Combo boxes for filtering"""

        query = self.textEdit_query.toPlainText()
        if len(query) == 0:
            pass
        else:
            self.search_MongoDB()

    def search_MongoDB(self):
        """Find query matches in the database"""

        all_results = []

        query = self.textEdit_query.toPlainText()
        imported = self.comboBox_imported.currentText()
        links = self.comboBox_links_found.currentText()

        if not query:
            messagebox = QMessageBox(self)
            messagebox.setIcon(QMessageBox.Information)
            messagebox.setText("Please enter your query term")
            messagebox.setWindowTitle("Empty query")
            messagebox.show()
            return

        # Construct dictionary with parameters for querying
        query_parameters = {}  # Empty dictionary
        # dictionary_name[key] = value
        query_parameters["$text"] = {"$search": query}  # New addquery

        if imported != "Show all":
            query_parameters["imported"] = imported  # Add filter "imported" into dict

        if links != "Show all":  # Add filter Links found into dict
            query_parameters["urlsfound"] = (
                {"$exists": True, "$not": {"$size": 0}}
                if links == "Yes"
                else {"$exists": True, "$size": 0}
            )

        print(f"Dictionary for query: {query_parameters}")
        # Search database for matches
        self.all_mongodb_results = mongodb_CRUD.find_matches(query_parameters)

        # None as return value means an error occured
        if self.all_mongodb_results == None:
            messagebox = QMessageBox(self)
            messagebox.setIcon(QMessageBox.Information)
            messagebox.setText("Error Connecting to database      ")
            messagebox.setWindowTitle("Server Error")
            messagebox.show()
            return

        self.display_results()

    def connectSignalsSlots(self):
        """Signal-slots connections"""

        # If Search button is pressed
        self.pushButton_search.clicked.connect(self.search_MongoDB)

        # If spin box value changes
        self.spinBox.valueChanged.connect(self.display_results)

        # If checkbox state is changed
        self.checkBox.stateChanged.connect(self.display_results)

        # If combobox value changes
        self.comboBox_imported.currentIndexChanged.connect(self.check_query)
        self.comboBox_links_found.currentIndexChanged.connect(self.check_query)


if __name__ == "__main__":
    from PyQt5 import QtWidgets

    # Create PyQt5 app
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()

    # Create the instance of our MainWindow
    win = MainWindow()
    win.show()
    # Start the app
    sys.exit(app.exec())
