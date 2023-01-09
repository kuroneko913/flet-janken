import flet as ft
from janken import JankenApp

def main(page: ft.Page):
    page.title = "JankenApp"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 250        # window's width is 200 px
    page.window_height = 200       # window's height is 200 px
    page.window_resizable = False  # window is not resizable
    page.update()

    # create application instance
    janken = JankenApp()

    # add application's root control to the page
    page.add(janken)

ft.app(target=main)