import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class MedicalCostApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Medical Cost Prediction')
        layout = QVBoxLayout()  

        self.label = QLabel('Enter your medical data:')
        layout.addWidget(self.label)  

        self.input_data = QLineEdit(self)
        layout.addWidget(self.input_data)

        self.predict_button = QPushButton('Predict Cost', self)
        self.predict_button.clicked.connect(self.predict_cost)
        layout.addWidget(self.predict_button)

        self.setLayout(layout)
        self.show()  

    def predict_cost(self):
        # Here, you will call your model to predict the cost based on input data.
        input_value = self.input_data.text()
        if not input_value:
            QMessageBox.warning(self, 'Input Error', 'Please enter valid data!')
            return
        try:
            # You would replace this with the actual prediction logic.
            predicted_cost = float(input_value) * 100  # Dummy calculation
            QMessageBox.information(self, 'Predicted Cost', f'Estimated Medical Cost: ${predicted_cost:.2f}')
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter a numeric value!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MedicalCostApp()
    sys.exit(app.exec_())