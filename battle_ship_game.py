# This is where evrything is imported, where the main game loop runs, and where events are checked for. 
# Nothing yet to be placed.
import arcade
arcade.open_window(1900,900,'drawing example')
# This is a background color until we mess with sprites ->
arcade.set_background_color(arcade.color.CHARCOAL)
arcade.start_render()
# drawing goes here
# seperator. needs adjustments
for i in range(19):
    arcade.draw_line((i * 100), 0,(i * 100), 900, arcade.csscolor.BLACK)
for i in range(9):
    arcade.draw_line(0, (i * 100),1900, (i * 100), arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(900,1000, 900,0,arcade.csscolor.BLACK)
# drawing ends here
arcade.finish_render()
arcade.run()

