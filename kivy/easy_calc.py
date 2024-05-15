from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        input_layout = BoxLayout(orientation='horizontal', spacing=10)
        
        input1 = TextInput(text='Поле ввода 1', size_hint=(1, 0.2), input_type='number')
        input2 = TextInput(text='Поле ввода 2', size_hint=(1, 0.2), input_type='number')
        input_layout.add_widget(input1)
        input_layout.add_widget(input2)

        button_layout = BoxLayout(orientation='horizontal', spacing=10)
        
        def digit_convert(f, s):
            try:
                f = float(f)
                s = float(s)
                return f,s
            except:
                return "e","e"
        def plus(instance):
            num1, num2 = digit_convert(input1.text, input2.text)

            if num1 == "e":
                result = "Недопустимый ввод"
                self.button5.text = f'Результат: {result}'
                return

            result = num1 + num2
            self.button5.text = f'Результат: {result}'
            
        def minus(instance):
            num1, num2 = digit_convert(input1.text, input2.text)
            if num1 == "e":
                result = "Недопустимый ввод"
                self.button5.text = f'Результат: {result}'
                return

            result = num1 - num2
            self.button5.text = f'Результат: {result}'
            
        def multiply(instance):
            num1, num2 = digit_convert(input1.text, input2.text)
            if num1 == "e":
                result = "Недопустимый ввод"
                self.button5.text = f'Результат: {result}'
                return

            result = num1 * num2
            self.button5.text = f'Результат: {result}'
            
        def division(instance):
            num1, num2 = digit_convert(input1.text, input2.text)
            if num1 == "e":
                result = "Недопустимый ввод"
                self.button5.text = f'Результат: {result}'
                return

            if num2 == 0.0:
                result = "Деление на ноль невозможно"
                self.button5.text = f'Результат: {result}'
                returnсумму
            result = num1 / num2
            self.button5.text = f'Результат: {result}'
        button1 = Button(text='+', size_hint=(1, 0.2))
        button1.bind(on_press=plus)
        button2 = Button(text='-', size_hint=(1, 0.2))
        button2.bind(on_press=minus)
        button3 = Button(text='*', size_hint=(1, 0.2))
        button3.bind(on_press=multiply)
        button4 = Button(text='/', size_hint=(1, 0.2))
        button4.bind(on_press=division)
        self.button5 = Button(text='Результат: ')


        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        button_layout.add_widget(button3)
        button_layout.add_widget(button4)

        layout.add_widget(input_layout)
        layout.add_widget(self.button5)
        layout.add_widget(button_layout)
        

        return layout

if __name__ == '__main__':
    MyApp().run()
