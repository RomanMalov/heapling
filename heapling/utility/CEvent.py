import pygame
from pygame.locals import *
import sys


class CEvent():

    def on_input_focus(self):
        print(sys._getframe().f_code.co_name)

    def on_input_blur(self):
        print(sys._getframe().f_code.co_name)

    def on_key_down(self, event):
        print(sys._getframe().f_code.co_name)
        print(event)

    def on_key_up(self, event):
        print(sys._getframe().f_code.co_name)

    def on_mouse_focus(self):
        print(sys._getframe().f_code.co_name)

    def on_mouse_blur(self):
        print(sys._getframe().f_code.co_name)

    def on_mouse_move(self, event):
        print(sys._getframe().f_code.co_name)

    def on_mouse_wheel(self, event):
        print(sys._getframe().f_code.co_name)

    def on_lbutton_up(self, event):
        print(sys._getframe().f_code.co_name)

    def on_lbutton_down(self, event):
        print(sys._getframe().f_code.co_name)

    def on_rbutton_up(self, event):
        print(sys._getframe().f_code.co_name)

    def on_rbutton_down(self, event):
        print(sys._getframe().f_code.co_name)

    def on_mbutton_up(self, event):
        print(sys._getframe().f_code.co_name)

    def on_mbutton_down(self, event):
        print(sys._getframe().f_code.co_name)

    def on_minimize(self):
        print(sys._getframe().f_code.co_name)

    def on_restore(self):
        print(sys._getframe().f_code.co_name)

    def on_resize(self, event):
        print(sys._getframe().f_code.co_name)

    def on_expose(self):
        print(sys._getframe().f_code.co_name)

    def on_exit(self):
        print(sys._getframe().f_code.co_name)
        self._running = False

    def on_user(self, event):
        print(sys._getframe().f_code.co_name)

    # def on_joy_axis(self, event):
    #     pass
    #
    # def on_joybutton_up(self, event):
    #     pass
    #
    # def on_joybutton_down(self, event):
    #     pass
    #
    # def on_joy_hat(self, event):
    #     pass
    #
    # def on_joy_ball(self, event):
    #     pass

    def on_event(self, event):
        if event.type == QUIT:
            self.on_exit()

        elif event.type >= USEREVENT:
            self.on_user(event)

        elif event.type == VIDEOEXPOSE:
            self.on_expose()

        elif event.type == VIDEORESIZE:
            self.on_resize(event)

        elif event.type == KEYUP:
            self.on_key_up(event)

        elif event.type == KEYDOWN:
            self.on_key_down(event)

        elif event.type == MOUSEMOTION:
            self.on_mouse_move(event)

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self.on_lbutton_up(event)
            elif event.button == 2:
                self.on_mbutton_up(event)
            elif event.button == 3:
                self.on_rbutton_up(event)

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.on_lbutton_down(event)
            elif event.button == 2:
                self.on_mbutton_down(event)
            elif event.button == 3:
                self.on_rbutton_down(event)

        elif event.type == ACTIVEEVENT:
            if event.state == 1:
                if event.gain:
                    self.on_mouse_focus()
                else:
                    self.on_mouse_blur()
            elif event.state == 2:
                if event.gain:
                    self.on_input_focus()
                else:
                    self.on_input_blur()
            elif event.state == 4:
                if event.gain:
                    self.on_restore()
                else:
                    self.on_minimize()


if __name__ == "__main__":
    event = CEvent()