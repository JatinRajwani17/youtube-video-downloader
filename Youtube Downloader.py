from pytube import YouTube
from functools import partial
from kivymd.uix.relativelayout import MDRelativeLayout
import re

from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (400,600)
class MyApp(MDApp):

    def getLinkInfo(self,event,layout):
        self.link = self.linkinput.text
        self.checklink = re.match("^https://www.youtube.com/.*",self.link)
        print(self.checklink)

        if(self.checklink):
            print("Valid Link")
            self.errorLabel.text=""
            self.errorLabel.pos_hint={"center_x":0.5,"center_y":20}

            try:
                self.errorLabel.text = ""
                self.errorLabel.pos_hint = {"center_x": 0.5, "center_y": 20}

                self.yt = YouTube(self.link)

                self.title = str(self.yt.title)
                self.views = str(self.yt.views)
                self.length = str(self.yt.length)

                self.titleLabel.text = "Title : " + self.title
                self.titleLabel.pos_hint = {"center_x": 0.5, "center_y": 0.4}

                self.viewsLabel.text = "Views : " + self.views
                self.viewsLabel.pos_hint = {"center_x": 0.5, "center_y": 0.35}

                self.lengthLabel.text = "Length : " + self.length
                self.lengthLabel.pos_hint = {"center_x": 0.5, "center_y": 0.30}

                self.downloadButton.text = "Download"
                self.downloadButton.pos_hint = {"center_x": 0.5, "center_y": 0.15}
                self.downloadButton.size_hint = (0.3, 0.1)

                print("TITLE : " + self.title)
                print("VIEWS : " + self.views)
                print("LENGTH : " + self.length)

            except:
                self.errorLabel.text = "Network or Unknown Error"
                self.errorLabel.pos_hint = {"center_x": 0.5, "center_y": 0.3}
        else:
            self.errorLabel.text="Invalid or Empty Link"
            self.errorLabel.pos_hint={"center_x":0.5,"center_y":0.3}

    def download(self,event,layout):
        self.ys = self.yt.streams.get_highest_resolution()
          # Check if only one stream is filtered
        print("Downloading")
          # Get the single stream object
        self.ys.download("D:")  # Download the selected stream
        print("DOWNLOAD COMPLETE")

    def build(self):
        layout = MDRelativeLayout(md_bg_color = [248/255,200/255,220/255])

        self.image = Image(source="images/bg-remove1.png",size_hint=(0.5,0.5),
                           pos_hint={"center_x":0.5,"center_y":0.90} )

        self.youtubelink = Label(text="Please Enter The Youtube Link To Download",
                                 pos_hint={"center_x":0.5,"center_y":0.75},
                                 size_hint=(1,1),font_size=20,color=(1,0,0))

        self.linkinput = TextInput(text="",pos_hint={"center_x":0.5,"center_y":0.65},
                                   size_hint=(1,None),height=48,font_size=29,
                                   foreground_color=(0,0.5,0),
                                   font_name="Comic")

        self.linkbutton = Button(text="Get Link",pos_hint={"center_x":0.5,"center_y":0.5},
                                 size_hint=(0.2,0.1),font_name="Comic",font_size=24,
                                 background_color=[0,1,0])

        self.linkbutton.bind(on_press= partial(self.getLinkInfo,layout))

        self.titleLabel = Label(text="",pos_hint={"center_x":0.5,"center_y":20},
                                size_hint=(1,1),font_size=20)
        self.viewsLabel = Label(text="", pos_hint={"center_x": 0.5, "center_y": 20},
                                size_hint=(1, 1), font_size=20)
        self.lengthLabel = Label(text="", pos_hint={"center_x": 0.5, "center_y": 20},
                                size_hint=(1, 1), font_size=20)

        self.downloadButton = Button(pos_hint={"center_x":0.5,"center_y":20},
                                     size_hint=(0.2,0.1),size=(75,75),font_name="Comic",
                                     bold=True,font_size=24,
                                     background_color=(0,1,0))

        self.downloadButton.bind(on_press=partial(self.download,layout))

        self.errorLabel = Label(text="",pos_hint={"center_x":0.5,"center_y":20},
                                size_hint=(1,1),font_size=20,color=(1,0,0))

        layout.add_widget(self.image)
        layout.add_widget(self.youtubelink)
        layout.add_widget(self.linkinput)
        layout.add_widget(self.linkbutton)
        layout.add_widget(self.titleLabel)
        layout.add_widget(self.viewsLabel)
        layout.add_widget(self.lengthLabel)
        layout.add_widget(self.downloadButton)
        layout.add_widget(self.errorLabel)

        return layout
if __name__=="__main__":
    MyApp().run()
