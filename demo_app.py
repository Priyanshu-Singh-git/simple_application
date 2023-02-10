from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
import random, functools

class Kivy_UI(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 4
        self.rnd_no = random.randint(1,10)
        # random image generation
        self.src_tuple = ("magnetar.jpg", "meteor.jpg", "multiverse.jpg", "blackhole.png", "nebula.jfif",
                         "oortcloud.jpg", "quasar.jfif", "asteroid.jpg", "neutronstar.webp", "wormhole.jpg")

        # removing the extensions
        self.src_name_tuple = (x.replace(".jpg","") for x in self.src_tuple)
        self.src_name_tuple = (x.replace(".png","") for x in self.src_name_tuple)
        self.src_name_tuple =(x.replace(".webp","") for x in self.src_name_tuple)
        self.src_name_tuple = tuple((x.replace(".jfif", "") for x in self.src_name_tuple))
        for i in self.src_name_tuple:
            print(i)

        self.img = Image(
            source =self.src_tuple[self.rnd_no-1],
            size_hint=(4.75,4.75)
        )
        self.add_widget(self.img)
        self.label = Label(
            text="what is this?",
            font_size=25

        )
        self.add_widget(self.label)
        self.txt = TextInput(
            text="", font_size=25)
        self.add_widget(self.txt)
        self.bttn = Button(
            text="Submit",
            font_size=25,
            background_color=(0.23,20,10,1),
            color=(0.1,0.1,0.1,1)
        )
        # binding the function with button
        self.bttn.bind(on_press=self.call_back)
        self.add_widget(self.bttn)
        self.ppup=Popup(
            title="Popup",
            size_hint=(0.7,0.4),
            content = Label(
                text=""
            )
        )

    def call_back(self,elem):
        # self.ppup.content.text="this is "+self.txt.text
        ######################################################
        # modifying the text input returned value
        ######################################################
        self.txt.text=self.txt.text.lower()
        if self.txt.text.isalpha() == True:

            print("it is alphabet")
            self.modified_text_n=self.txt.text
            print(self.modified_text_n)
        else:
            print("it is not alphabhet")
            self.modified_text=list(c for c in self.txt.text if c.isalpha())
            self.modified_text_n= functools.reduce(t:=lambda x,y:x+y,self.modified_text)
            print(self.modified_text_n)
        ###############################################################
        # comparing the values of text input and provided tuple
        ###############################################################
        if self.modified_text_n == self.src_name_tuple[self.rnd_no-1]:
            self.ppup.content.text = "Hurray!!\nYou Gave a right answer\nthis was a " + self.src_name_tuple[self.rnd_no - 1]
            self.ppup.open()

            self.update_img()


        else:
            self.ppup.content.text = "OOps!!\nYou Gave Wrong answer\nthis was a " + self.src_name_tuple[self.rnd_no - 1]
            self.ppup.open()
            self.update_img()


    def update_img(self):
        self.rnd_no=random.randint(1,10)
        self.img.source=self.src_tuple[self.rnd_no-1]
        self.txt.text = " "


class DemoAppApp(App):


    def build(self):
        self.title = "Astro-Quiz"
        self.icon = "icon.webp"

        a = Kivy_UI()
        return a


if __name__ == "__main__":
    d_a=DemoAppApp()
    d_a.run()