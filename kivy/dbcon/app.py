from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from db import Connection
from main import add, edit_last, start


class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        start()
        main_screen = Screen(name='main')
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        button1 = Button(text='Просмотреть')
        button1.bind(on_press=self.view_students)
        button2 = Button(text='Добавить')
        button2.bind(on_press=self.add_student_screen)
        button3 = Button(text='Изменить последнего')
        button3.bind(on_press=lambda _: edit_last("Иван Иванович"))

        button_layout = BoxLayout(orientation='vertical', spacing=10)
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        button_layout.add_widget(button3)

        main_layout.add_widget(button_layout)
        main_screen.add_widget(main_layout)
        self.screen_manager.add_widget(main_screen)

        self.view_screen = Screen(name='view')
        self.screen_manager.add_widget(self.view_screen)
        self.add_screen = Screen(name='add_student')
        self.screen_manager.add_widget(self.add_screen)

        return self.screen_manager

    def view_students(self, instance):
        conn = Connection()

        students = conn.get_all()
        
        view_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        self.view_screen.clear_widgets()

        for count, student in enumerate(students):
            view_layout.add_widget(Label(text=f'{student.name}'))
            if count == 9:
                break
        back_button = Button(text='Назад')
        back_button.bind(on_press=self.back_to_main)
        view_layout.add_widget(back_button)

        self.view_screen.add_widget(view_layout)
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'view'

        
    def add_student_screen(self, instance):
        add_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.view_screen.clear_widgets()

        input_field = TextInput(hint_text='Введите имя студента')

        create_button = Button(text='Создать')
        create_button.bind(on_press=lambda _: add(input_field.text))
        back_button = Button(text="Назад")
        back_button.bind(on_press=self.back_to_main)

        add_layout.add_widget(input_field)
        add_layout.add_widget(create_button)
        add_layout.add_widget(back_button)

        self.add_screen.add_widget(add_layout)

        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'add_student'
        

    def back_to_main(self, instance):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'main'
        
if __name__ == '__main__':
    MyApp().run()
