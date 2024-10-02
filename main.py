from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        # Создаем вертикальный макет
        layout = BoxLayout(orientation='vertical')
        
        # Создаем текст
        self.label = Label(text="Привет! Нажми на кнопку.")
        layout.add_widget(self.label)
        
        # Создаем кнопку
        btn = Button(text="Нажми меня")
        btn.bind(on_press=self.on_button_press)
        layout.add_widget(btn)
        
        return layout

    def on_button_press(self, instance):
        # Меняем текст на метке при нажатии
        self.label.text = "Ты нажал на кнопку!"

# Запуск приложения
if __name__ == '__main__':
    MyApp().run()