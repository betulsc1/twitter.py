from twitterUserInfo import username, password
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import tweepy
import spacy
import nltk
import pandas

class Twitter:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.username = username
        self.password = password
    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input")
        usernameInput.send_keys(self.username)
        ılerıbutton = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div").click()
        time.sleep(2)
        passwordInput = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        passwordInput.send_keys(self.password)
        btnSubmit = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]")
        btnSubmit.click()
        time.sleep(2)
    def search(self, hashtag):
        searchInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
        searchInput.click()
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        list = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]")
        time.sleep(2)
        print("count"+ str(len(list)))


        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 3:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter+=1
            
            list = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]")
            time.sleep(2)
            print("count"+ str(len(list)))


  
            

twitter = Twitter(username,password)
twitter.signIn()
twitter.search("python")



