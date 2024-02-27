import kivy
from kivmob import KivMob
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.core.audio import SoundLoader
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image



KV = """
ScreenManager:
    
    Screen:
        name: "scr1" 
        BoxLayout:
            orientation:'vertical'
            # size_hint_y: None
            # height:dp(48)
            spacing:'23dp'
            # background_color: (0,1,0,1) 

            canvas.before:   
                    
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    source:"pex5.jpg" 
                    # radius:[30] 

            Label:
                text: ""
                
                size_hint: (1,0.16)   
            Label:
                text: "SHALOM ALECHEM"
                bold:'True'
                # background_color: (1,1,0,1)
                color: "yellow"
                font_size: '25dp'
                font_name: 'LoveRabbitPersonalUse-lgRaZ.ttf'
                size_hint: (1,0.16)   

            FloatLayout:
            
                spacing:'23dp'
          
                
                MDRoundFlatButton:
                    text: 'DONATE TO KABBALAH CENTER'
                                    
                    text_color: "red"
                    pos_hint: {'x':0.04 , 'y':0.01 } 
                    bold:'True'
                    on_release: root.current = "scr2"  
                MDRoundFlatButton:
                    text: 'ARTICLES AND NEWS'
                                       
                    text_color: "red"
                    pos_hint: {'x':0.77 , 'y':0.01 } 
                    bold:'True'
                    on_release: root.current = "scr2"  
                      
            MDRoundFlatButton:
                text: 'KABBALAH CENTER INTERNATIONAL Live streams'
                size_hint: (1,1.4)                   
                text_color: "white"
                bold:'True'
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.kabbalah.com/en/events/streams/')  
            MDRoundFlatButton:
                text: 'KABBALISTIC MEDITATION'
                size_hint: (1,1.4)                   
                text_color: "white"
                bold:'True'
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.kabbalah.com/en/online-courses/lessons/72-names-13-heaven-on-earth/')  
            MDRoundFlatButton:
                text: 'KABBALAH CENTER INTERNATIONAL UPCOMING EVENTS & CLASSES'
                size_hint: (1,1.4)                   
                text_color: "white"
                bold:'True'
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.kabbalah.com/en/events/')  
            
            MDRoundFlatButton:
                text: 'KABBALAH CENTER INTERNATIONAL ONLINE STORE'
                size_hint: (1,1.4)                   
                text_color: "white"
                bold:'True'
                on_release:
                    import webbrowser
                    webbrowser.open('https://store.kabbalah.com/')  
            MDRoundFlatButton:
                text: 'ONLINE ZOHAR'
                size_hint: (1,1.4)  
                font_size: '20dp'                 
                text_color: "red"
                bold:'True'
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.zohar.com/zohar')  
            MDRoundFlatButton:
                text: 'ONLINE TORAH'
                size_hint: (1,1.4)                   
                text_color: "red"
                font_size: '20dp' 
                bold:'True'
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.chabad.org/parshah/otherparshas_cdo/aid/9175/jewish/All-Parshahs.htm')  

            Label:
                text: ""
               
                font_size: '5dp'
                
    Screen:
        name: "scr2" 
        FloatLayout:
            # orientation:'vertical'
            # size_hint_y: None
            # height:dp(48)
            # spacing:'23dp'
            background_color: (0,1,0,1) 

            canvas.before:   
                    
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    source:"pex4.jpg" 
                    # radius:[30] 
                                
            Label:
                text: "DONATE TO KABBALAH CENTER LAGOS"
                font_size: '25dp'
                pos_hint: {'x':0.05 , 'y':0.3 } 
        
            Label:
                text: "ACC. Name: Shlomo and Shlomo Consult \\nBank Name: Access Bank \\nAccount Number: 1225959863"
                      
                bold:'True'
                color: "yellow"
                font_size: '20dp'
                pos_hint: {'x':0.05 , 'y':0.18 } 
                
            # Label:
            #     text: ""
            #     font_size: '25dp'
            #     pos_hint: {'x':0.05 , 'y':0.1 } 

           
                    
            MDRoundFlatIconButton:
                text: "DONATE TO KABBALAH CENTER INTERNATIONAL"
                style: "elevated"
                icon: "android"
                text_color: "white"
                pos_hint: {"center_x": .5, "center_y": .4}
                # pos_hint: {'x':0.05 , 'y':0.1 } 
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.kabbalah.com/en/giving/')  



            MDRoundFlatIconButton:
                text: "Back To Main Page"
                style: "elevated"
                icon: "android"
                text_color: "white"
                pos_hint: {"center_x": .5, "center_y": .1}
                on_release: root.current = "scr1" 
      


"""


class MyCarTestApp(MDApp):

    def build(self):
       
    
        return Builder.load_string(KV)


    def on_start(self):
        
        pass

        

if __name__ == "__main__":
    MyCarTestApp().run()
