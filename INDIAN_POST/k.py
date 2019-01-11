from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request as request
from time import sleep
import re
from PIL import Image
import os
import cv2
import pyautogui


folder1 = '/home/z3r0/Desktop/CAPTCHA/Scraping/INDIAN_POST/CAPTCHA/'
folder2 = '/home/z3r0/Desktop/CAPTCHA/Scraping/INDIAN_POST/CAPTCHA_WITH_DESCPRIPTION/'
folder3 ='/home/z3r0/Desktop/CAPTCHA/Scraping/INDIAN_POST/WEBPAGE/'

ID = "ctl00_SPWebPartManager1_g_aa197fec_b38c_41a8_b14e_a11722636b37_ctl00_imgCaptcha"
ID1 = "ctl00_SPWebPartManager1_g_aa197fec_b38c_41a8_b14e_a11722636b37_ctl00_imgMathCaptcha"
text = "ctl00_SPWebPartManager1_g_aa197fec_b38c_41a8_b14e_a11722636b37_ctl00_lblCaptcha"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.indiapost.gov.in')



def do(i):
	sleep(1)
	srcc = ''
	try:
		srcc = browser.find_element_by_id(ID1).get_attribute('src')
	# elif 'displayed' in (browser.find_element_by_id(text).text):
	except:
		srcc = browser.find_element_by_id(ID).get_attribute('src')
	if 'displayed' in browser.find_element_by_id(text).text:
		request.urlretrieve(srcc, folder1 + '{}.aspx'.format(str(i)))
	else:
		request.urlretrieve(srcc, folder1 + '{}.png'.format(str(i)))
	if(i==0):
		s = pyautogui.screenshot(region = (233,457,272,56))
	else:
		s = pyautogui.screenshot(region = (234,674,319,54))
	s.save(folder2+'{}.png'.format(str(i)))
	with open(folder3 + "{}.html".format(str(i)), "w") as f:
		f.write(browser.page_source)
	browser.find_element_by_id('ctl00_SPWebPartManager1_g_aa197fec_b38c_41a8_b14e_a11722636b37_ctl00_imgbtnCaptcha').click()

for j in range(1000):
	do(j)