# -*- coding: utf-8 -*-
"""
47-video
39-03-dars. PYTHON TASHQI KUTUBXONASI
            fuzzywuzzy MODULI
            wxPtyhon MODULI
Created on Thu Mar 21 15:00:55 2024

@author: Asadbek (devusta)
"""

# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # fuzzywuzzy - ikkita mattnni bir-biriga qanchalik 
#                # mos kelishini aniqlab beruvchi modul
# # fuzz - moduldagi obyekt
# # process - moduldagi obyekt
# # ratio() - fuzz obyektining metodi  
# # extract() - process obyektidagi o'xshash elementlarni qaytaruvchi metod
# # extractOne() - process obyektidagi bitta eng o'xshash elementni qaytaruvchi metod
# # wxPython - python yardamida grafik interfaceli 
#            # dasturlar yozishda ishlatiladigan modul
# # wxFormBuilder - turli interface formalarni yasash uchun dastur
# # face-recognation - yuzlarni tanish moduli
# =============================================================================


from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# =============================================================================
# # ikki so'z o'rtasidagi o'xshashlikning foizini topish
# print(fuzz.ratio('salom', 'assalom'))
# print(fuzz.ratio('tohir', 'taxir'))
# =============================================================================

# =============================================================================
# # Matnlar orasidagi 3 ta eng o'xshashlarini ajratib olish
# words = ["boyna", "o'yna", "hoyna", "oyna", "qayna", "turna", "qayda"]
# text = 'oyna'
# 
# matches = process.extract(text, words, limit=3)
# print(matches)
# =============================================================================

# =============================================================================
# # Matnlar orasidan eng o'xshashini topish
# words = ["boyna", "o'yna", "hoyna", "oyna", "qayna", "talaba", "turnfa", "qayda"]
# text = "talab"
# match = process.extractOne(text, words)
# print(match)
# =============================================================================

# wxPython moduli
# cod from https://python.sariq.dev/last-words/39-pip-pypi#wxpython
import wx
from googletrans import Translator

# =============================================================================
# # Kichik tarjima dastur interface
# tarjimon = Translator()
# 
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(parent=None, title="O'zbek-Ingliz Lug'ati")
#         panel = wx.Panel(self)
#         my_sizer = wx.BoxSizer(wx.VERTICAL)
#         self.text_ctrl = wx.TextCtrl(panel)
#         my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
#         
#         my_btn = wx.Button(panel, label="TARIMA")
#         my_btn.Bind(wx.EVT_BUTTON, self.on_press)
#         my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
#         
#         self.text_out = wx.TextCtrl(panel, style=wx.TE_READONLY)
#         my_sizer.Add(self.text_out, 0, wx.ALL | wx.EXPAND, 5)
#         panel.SetSizer(my_sizer)
#         self.Show()
#         
#     def on_press(self, event):
#         value = self.text_ctrl.GetValue()
#         if not value:
#             self.text_out.SetValue("So'z kiritmadingiz")
#         else:
#             tarjima = tarjimon.translate(value, src="uz", dest="en")
#             self.text_out.SetValue(tarjima.text.capitalize())
# 
# 
# if __name__ == "__main__":
#     app = wx.App()
#     frame = MyFrame()
#     app.MainLoop()
# =============================================================================















