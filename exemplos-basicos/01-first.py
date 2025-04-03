from pyray import *
init_window(800, 450, "Tela em branco")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_text("Primeira tela Raylib", 190, 200, 20, VIOLET)
    end_drawing()
close_window()