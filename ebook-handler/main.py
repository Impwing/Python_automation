import os
import threading
import time
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from ebookhandler import Bookshelf

WIDTH = 256
HEIGHT = 512
KINDLE_PATH = "/Volumes/Kindle/"
KINDLE_DISABLED = True


class Gui:
    def __init__(self, guiItems):
        self.guiItems = guiItems

    def setLabelText(self, id, text):
        self.guiItems[id].text = text

    def getGuiItem(self, id):
        return self.guiItems[id]


class EbookHandler(Widget):
    def __init__(self, **kwargs):
        super(EbookHandler, self).__init__(**kwargs)
        self.kindleDisabled = True
        self.bookshelf = Bookshelf()
        self.bookshelf.setup()
        self.gui = Gui(self.ids)
        self.setup()
        if self.kindleDisabled:
            self.pollThread = threading.Thread(target=self.pollDevice, daemon=True)
            self.pollThread.start()

    def findKindle(self):
        if os.path.isdir(KINDLE_PATH):
            self.kindleDisabled = False
            return "Kindle Connected"
        else:
            self.kindleDisabled = True
            return "No Kindle Detected"

    def pollDevice(self):
        while True:
            self.findKindle()
            time.sleep(2)
            self.setup()
        return False

    def sort(self):
        self.bookshelf.sort()
        self.setup()

    #def list(self):
        #self.bookshelf.list()

    def transfer(self):
        self.bookshelf.toKindle()

    def setup(self):
        self.__setGui__()
        self.__setButtons__()

    def __setGui__(self):
        self.gui.setLabelText('title', "Ebook Handler")
        self.gui.setLabelText('bookshelf_count', "Bookshelf: " + str(self.bookshelf.numberOfBooksInShelf()))
        self.gui.setLabelText('connected', self.findKindle())
        self.gui.setLabelText('stored_count', "To Move: " + str(self.bookshelf.numberOfBooksToMove()))

    def __setButtons__(self):
        self.gui.getGuiItem('sort').on_press = self.sort
        self.gui.getGuiItem('to_kindle').disabled = self.kindleDisabled
        self.gui.getGuiItem('to_kindle').on_press = self.transfer
        #self.gui.getGuiItem('list').on_press = self.list


class EbookHandlerApp(App):
    title = 'Ebook Handler'

    def build(self):
        Window.clearcolor = get_color_from_hex("#262626")
        Window.size = (WIDTH, HEIGHT)
        return EbookHandler()


if __name__ == '__main__':
    EbookHandlerApp().run()
