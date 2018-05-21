from selenium import webdriver
import os
import threading
import time
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chess.uci
import chess

stockfish = chess.uci.popen_engine("C:/Users/ze239/Downloads/stockfish-9-win/stockfish-9-win/Windows/stockfish_9_x64.exe")
info_handler = chess.uci.InfoHandler()
stockfish.info_handlers.append(info_handler)
stockfish.uci()
stockfish.position(chess.Board())
stockfish.go(movetime=2000)
info_handler.info["score"][1]

# screenWidth, screenHeight = pyautogui.size()
# pyautogui.PAUSE = 1
# pyautogui.FAILSAFE = True
#
# def enter():
#     pyautogui.typewrite(['enter'])
#
# def changeStock():
#     pyautogui.click(x = 601, y = 280)
#     pyautogui.click(x=601, y=280)

#
# # pyautogui.click(x = 601, y = 280)
# # pyautogui.click(x = 601, y = 280)
# # pyautogui.typewrite("position startpos")
# # enter()
#
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.get("https://www.chess.com/login_and_go?returnUrl=https%3A//www.chess.com/live")
# login = driver.find_element_by_id("username")
# login.click()
# login.send_keys("imabotlegit")
# login2 = driver.find_element_by_id("password")
# login2.click()
# login2.send_keys("ima1993bot")
# button = driver.find_element_by_id("login")
# button.click()
# pyautogui.moveTo(x = 300, y = 25)
# pyautogui.dragTo(1349, 25, .2, button='left')
#
#
# try:
#     start = driver.find_element_by_class_name("play-button-component_0")
#     start.click()
# except:
#     start2 = driver.find_element_by_class_name("btn btn-large btn-new-game btn-primary")
#     start2.click()
# start = driver.find_element_by_class_name("play-button-component_0")
# start.click()