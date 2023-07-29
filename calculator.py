import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather Check")
        self.setMinimumSize(300, 300)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Введіть назву міста")

        self.weather_label = QLabel()

        self.weather_button = QPushButton("Перевірити погоду")
        self.weather_button.clicked.connect(self.get_weather)

        layout.addSpacing(200)
        layout.addWidget(self.city_input)

        layout.addWidget(self.weather_label)
        layout.addWidget(self.weather_button)

        # Завантажуємо зображення і встановлюємо як фон
        pixmap = QPixmap("pogoda.jpg")
        pixmap = pixmap.scaled(500, 500)  # Змінюємо розмір зображення на 500x500 пікселів
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)  # Збільшуємо масштаб, щоб зображення заповнило фон

        # Розширюємо виджет QLabel до 500x500 пікселів
        background_label.setFixedSize(350, 350)

        self.setLayout(layout)

    def get_weather(self):
        city = self.city_input.text()
        api_key = "c836eecb19fcb7b4704e0073eced8527"  # Ваш API-ключ OpenWeatherMap
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]

            self.weather_label.setText(f"Температура: {temperature}°C\nОпис: {description}")
        else:
            self.weather_label.setText("Не вдалося отримати погоду для даного міста.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
