# This is where evrything is imported, where the main game loop runs, and where events are checked for. 
# Nothing yet to be placed.
import arcade
arcade.open_window(2000,900,'drawing example')
# This is a background color until we mess with sprites ->
arcade.set_background_color(arcade.color.CHARCOAL)
arcade.start_render()
# drawing goes here
# seperator. needs adjustments
arcade.draw_lrtb_rectangle_filled(850,1050, 900,0,arcade.csscolor.BLACK)
# drawing ends here
arcade.finish_render()
arcade.run()