from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETRE = 1.60934


class MilesToKilometreApp(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        value = self.get_valid_miles(text)
        self.update_result(value)

    @staticmethod
    def get_valid_miles(text):
        try:
            return float(text)
        except ValueError:
            return 0.0

    def update_result(self, miles):
        self.output_km = str(miles * MILES_TO_KILOMETRE)

    def handle_increment(self, text, change):
        value = self.get_valid_miles(text) + change
        self.root.ids.input_miles.text = str(value)


MilesToKilometreApp().run()
