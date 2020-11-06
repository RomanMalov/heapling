import utility.CEvent as cevent
import pygame

# change CApp into
class CApp(cevent.CEvent):

    def __init__(self):
        self._running = True
        pygame.init()

    def on_init(self)->bool:
        return True

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        print("Goodbye")
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
            self.on_loop()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = CApp()
    theApp.on_execute()