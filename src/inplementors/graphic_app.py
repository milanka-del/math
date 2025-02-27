from src.core import random_primer, check_answer, calculate
import dearpygui.dearpygui as dpg
import time
from src.inplementors.text_points import Text_Points


class GUI:
    def __init__(self):
        self.example = str(random_primer())
        self.answer = calculate(self.example)
        self.player_board = Text_Points()
        self.name_player = ' '

    def save_game(self):
        self.player_board.save()
        print('save')


    def update_example(self):
        self.example = str(random_primer())
        self.answer = calculate(self.example)
        dpg.set_value(item='text_area', value=self.example)

    def check_user_answer(self):
        user_answer = dpg.get_value(item='answer_input')
        result = check_answer(user_answer, self.answer)
        if result == True:
            dpg.add_text(default_value='correct', parent='main', tag='_')
            self.player_board.plus_points(self.name_player)
        else:
            dpg.add_text(default_value='not correct', parent='main', tag='_')
            self.player_board.minus_points(self.name_player)
        self.update_example()
        print(self.player_board.get_points(self.name_player))
        time.sleep(2)
        dpg.delete_item('_')

    def login(self):
        self.player_board.load()
        for name_player in self.player_board.points_board:
            dpg.add_text(self.player_board.points_board, parent='leaders')
        self.name_player = dpg.get_value(item='input_name')
        dpg.set_value(item='name_player', value=self.name_player)
        dpg.delete_item('login_group')
        dpg.show_item('app_group')
        self.player_board.add_player(self.name_player)


    def start(self):
        dpg.create_context()
        dpg.create_viewport(width=300, height=300, title="proga")
        # with dpg.font_registry():
        #     with dpg.font('./fonts/P95-CYR-Regular.otf', size=14, tag='a'):
        #         dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

        with dpg.window(tag='main'):
            with dpg.tab_bar():
                with dpg.tab(label='General'):
                    with dpg.group(tag='login_group'):
                        dpg.add_text('input name:')
                        dpg.add_input_text(tag='input_name')
                        dpg.add_button(label='start', callback=self.login)

                    with dpg.group(tag='app_group'):
                        dpg.add_text(tag='name_player')
                        dpg.add_text(tag='text_area', default_value=self.example)
                        dpg.add_input_float(tag='answer_input')
                        dpg.add_button(label="check", callback=self.check_user_answer)
                        dpg.add_button(label='save', callback=self.save_game)
                        dpg.hide_item(item='app_group')

                with dpg.tab(label='leaders', tag='leaders'):
                        dpg.add_text(default_value='list of records')


        dpg.setup_dearpygui()
        dpg.set_primary_window(window="main", value=True)
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

def graphic_version():
    t = GUI()
    t.start()
