import flet as ft
from jankenHand import JankenHand, Hand
from JankenFighter import JankenFighter

class JankenApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.jankenHand = None
        self.janken_fighter = JankenFighter()
        self.counter = {'win':0, 'lose':0, 'draw':0}
    
    def build(self):
        self.hand_button_rock = ft.FloatingActionButton(
            content=ft.Row(
                [ft.Text('グー')],
                alignment='center'
            ),
            on_click = self.rock_clicked
        )
        self.hand_button_scissors = ft.FloatingActionButton(
            content=ft.Row(
                [ft.Text('チョキ')],
                alignment='center',
            ),
            on_click = self.scissors_clicked
        )
        self.hand_button_paper = ft.FloatingActionButton(
            content=ft.Row(
                [ft.Text('パー')],
                alignment='center'
            ),
            on_click = self.paper_clicked
        )
        self.you_hand_name = ft.Text('')
        self.target_hand_name = ft.Text('')
        self.fight_result = ft.Text('')
        return ft.Column(
            width = 200,
            height = 200,
            controls = [
                ft.Row(
                    controls=[
                        self.hand_button_rock,
                        self.hand_button_scissors, 
                        self.hand_button_paper,
                    ]
                ),
                self.you_hand_name,
                self.target_hand_name,
                self.fight_result
            ]
        )

    def hand_clicked(self):
        target_hand = self.janken_fighter.doJanken(self.jankenHand.janken_hand_name)
        result = self.jankenHand.fight(target_hand)
        self.target_hand_name.value = '私の手:'+str(target_hand)
        if (result == 'win'):
            result_text = 'あなたの勝ち'
        elif (result == 'lose'):
            result_text = 'あなたの負け'
        else:
            result_text = '引き分け'
        self.counter[result] += 1
        self.fight_result.value = result_text+f"\n{self.counter['win']}勝{self.counter['lose']}敗{self.counter['draw']}引き分け"
        self.update()

    def rock_clicked(self, e):
        self.jankenHand = JankenHand(Hand.ROCK)
        self.you_hand_name.value = 'あなたの手:グー'
        self.hand_clicked()
        self.update()

    def scissors_clicked(self, e):
        self.jankenHand = JankenHand(Hand.SCISSORS)
        self.you_hand_name.value = 'あなたの手:チョキ'
        self.hand_clicked()
        self.update()

    def paper_clicked(self, e):
        self.jankenHand = JankenHand(Hand.PAPER)
        self.you_hand_name.value = 'あなたの手:パー' 
        self.hand_clicked()
        self.update()
