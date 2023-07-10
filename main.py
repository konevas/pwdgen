from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, NumericProperty
from kivy.core.clipboard import Clipboard
from kivymd.toast import toast
import kivymd
from pwdgen import get_pwd


class RootWidget(MDScreen):
    PWD_MAX_LEN = 999
    key = StringProperty('')
    pwd_len = NumericProperty(8)

    def generate_pwd(self):
        pwd = ''.join(get_pwd(self.key, pwd_len=self.pwd_len))
        Clipboard.copy(pwd)
        toast('Text copied', duration=3)
        self.ids.resultLabel.text = pwd

    def set_key(self, instance, text):
        self.key = text
        if self.key and self.pwd_len:
            self.ids.gen_button.disabled = False
        else:
            self.ids.gen_button.disabled = True

    def set_len(self, instance, text: str):
        if not text.isdecimal():
            instance.text = text[:-1]
            return
        self.pwd_len = int(text) if text else 0
        if self.pwd_len > self.PWD_MAX_LEN:
            self.pwd_len = self.PWD_MAX_LEN
            instance.text = str(self.PWD_MAX_LEN)
        if self.key and self.pwd_len:
            self.ids.gen_button.disabled = False
        else:
            self.ids.gen_button.disabled = True


class PwdgenApp(MDApp):
    def build(self):
        self.screen = RootWidget()
        return self.screen


if __name__ == '__main__':
    PwdgenApp(kv_file='main.kv').run()
