import arcade 
import classes 

arcade.open_window(800, 700, 'Pong Mini-Game')
arcade.set_background_color(arcade.color.WHITE)


arcade.start_render()

arcade.draw_xywh_rectangle_filled(100, 300, 400, 100, arcade.color.BLUE)

arcade.finish_render()

arcade.run()

