from ast import While
from random import randint
from telnetlib import Telnet
from tokenize import Name
from click import confirm
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import NoSuchElementException
import os
import geckodriver_autoinstaller
import time
import pyperclip
import numpy as np
import random
from selenium.webdriver.support.ui import WebDriverWait


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import fnmatch

# geckodriver_autoinstaller.install() 

class connection():

    def __init__(self):
        # self.get_ip_port()
        self.continue_following=False
        self.continue_like=False
        pass

    # def get_ip_port(self):
    #     myProxy = "154.236.184.70:1976"
    #     self.ip,self.port=myProxy.split(':')


    def set_init(self):

        # profile = FirefoxProfile(r'tor-browser-linux64-11.0.14_en-US/tor-browser_en-US/Browser/TorBrowser/Data/Browser/profile.default')
        profile = webdriver.FirefoxProfile()
        # profile.set_preference('network.proxy.type', 1)
        # profile.set_preference('network.proxy.socks', self.ip)
        # profile.set_preference('network.proxy.http', self.ip)
        # profile.set_preference('network.proxy.http_port', int(self.port))
        # profile.set_preference('network.proxy.socks_port', int(self.port))
        # profile.set_preference('network.proxy.ssl_port', int(self.port))
        # profile.set_preference('network.proxy.https', self.ip)
        # profile.set_preference('network.proxy.https_port', int(self.port))
        # profile.set_preference("network.proxy.socks_remote_dns", False)

        profile.update_preferences()
        self.driver = webdriver.Firefox(firefox_profile= profile)
        self.driver.set_window_position(600, 1500)
        self.driver.set_window_size(900, 600)
        # self.driver.set_window_position(0, 0)
        # self.driver.set_window_size(600, 400)
        return self.driver

    def get_url(self,url):

        self.driver.get(url)

    def set_login_pams(self,user_name,password):

        eror=False
        i=0
        link = None
        while not link:
            try:
                
                
                mail_web = eval("self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')".format(i))
                mail_web.send_keys(user_name)
                print('User Name Successfully')
                break
            except NoSuchElementException:
                print('Cant Find User Nmae in Web Retry','-'*10,i)
                i+=1
                time.sleep(2)
                if i>50:
                    break
        while not link:
            try:
                
                mail_web = eval("self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')".format(i))
                mail_web.send_keys(password)
                print('password Successfully')
                break
            except NoSuchElementException:
                print('Cant Find Password in Web Retry','-'*10,i)
                i+=1
                time.sleep(2)
                if i>50:
                    break

        while not link:
            try:
                sign_up_btn=eval("self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div')".format(i+4))
                sign_up_btn.click()
                print('Login Successfully')
                break
            except NoSuchElementException:
                print('Cant Find Sign up btn in Web Retry','-'*10,i)
                i+=1
                time.sleep(1)


        while not link:
            try:
                sign_up_btn=eval("self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/section/div/button')".format(i+4))
                sign_up_btn.click()
                print('Login Successfully')
                break
            except NoSuchElementException:
                print('Cant Find Sign up btn in Web Retry','-'*10,i)
                i+=1
                time.sleep(1)

        while not link:
            try:
                sign_up_btn=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')".format(i+4))
                sign_up_btn.click()
                print('Login Successfully')
                break
            except NoSuchElementException:
                print('Cant Find Sign up btn in Web Retry','-'*10,i)
                i+=1
                time.sleep(1)

    def search(self,parm,click=True):
        i=0
        link=None
        while not link:
            try:
                sign_up_btn=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input')")
                sign_up_btn.send_keys(parm)
                print('search Successfully')
                break
            except NoSuchElementException:
                print('Cant Find Search btn in Web Retry','-'*10,i)
                i+=1
                time.sleep(1)
                if i >10:
                    break
        if click:
            self.click_search()

    def click_search(self):
        i=0
        link=None
        while not link:
            try:
                sign_up_btn=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div')")
                sign_up_btn.click()
                print('search Successfully')
                break
            except NoSuchElementException:
                print('Cant Find Search btn in Web Retry','-'*10,i)
                i+=1
                time.sleep(1)
                if i>10:
                    break
    def clear_search(self):

        i=0
        link=None
        while not link:
            try:
                clear_search = WebDriverWait(
                    self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]")))
                clear_search.click()             
                # sign_up_btn=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[1]')")
                # sign_up_btn.click()
                clear_search = WebDriverWait(
                    self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[2]")))

                # sign_up_btn=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[2]')")
                clear_search.click()
                print('Clear Search')
                break
            except NoSuchElementException:
                print('Cant Find Clear Search btn in Web Retry','-'*10,i)
                i+=1
                time.sleep(1)
                if i>10:
                    break
    def follow(self):
        i=0
        link=None
        while not link:
            try:
                fllow_btn = WebDriverWait(
                    self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div/div")))
                fllow_btn.click()                
                # sign_up_btn=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div/div')")
                # sign_up_btn.click()
                print('follow Successfully')
                break
            except NoSuchElementException:
                print('Cant Find follow btn in Web Retry','-'*10,i)
                i+=1
                time.sleep(1)             
                if i>10:
                    self.clear_search()
                    break     

    def click_follow(self):

        i=0
        link=None
        while not link:
            time.sleep(2)
            try:
                click_follow=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button')")
                if click_follow.text == 'Follow':
                    click_follow.click()
                    print('click follow Successfully')
                else :
                    try:
                        # /html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button
                        click_follow=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')")
                        if click_follow.text == 'Follow':
                            click_follow.click() 
                            print('click follow Successfully')  
                    except:
                        print('asd')
                        pass
   
                
                time.sleep(2)
                self.clear_search()
                time.sleep(2)
                break
            except NoSuchElementException:
                print('Cant Find follow btn in Web Retry','-'*10,i)
                i+=1
                time.sleep(1)             
                if i>10:
                    self.clear_search()
                    break 

    def followrs_page(self):

        i=0
        link=None
        while not link:
            try:
                sign_up_btn=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div')")
                sign_up_btn.click()
                print('followrs_page Successfully')
                break
            except NoSuchElementException:
                print('Cant Find followrs_page in Web Retry','-'*10,i)
                i+=1
                time.sleep(1)             
                if i>10:
                    break     

    def get_follower_minipage_names(self,count,page_name):
        
        with open('followers-{}.txt'.format(page_name), 'w') as f:
            f.write('Get followers from page {}!'.format(page_name))


        time.sleep(5)
        i=0
        link=None
        # while not link:
            # try:
        for mem in range(2,count):
                print('mem',mem)
                try:
                    try:
                        user_address=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{}]/div/div[1]/div/div/a')".format(mem))
                    except:
                        user_address=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a')".format(mem))

                    user = user_address.get_attribute('href')
                    user=user.split("/")[3]
                    with open('followers-{}.txt'.format(page_name), 'a') as file:
                        file.write(user + '\n')
                # sign_up_btn.click()
                        print('write Successfully',user)

                except:
                    try:
                        pop_up_window = WebDriverWait(
                            self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]")))
                        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
                        time.sleep(5)
                    except:
                        break


    def get_follower_from_page(self,page_name,count):

        self.search(page_name)
        self.followrs_page()
        # self.follow()
        self.get_follower_minipage_names(count,page_name)


    def wait_press(self,function,path,text=None,path_name='Not set'):
        i=0
        link = None
        while not link:
            try:
                sign_up_btn=eval("self.driver.find_element_by_xpath('{}')".format(path))
                if text:
                    eval('sign_up_btn.{}({})'.format(function,text))
                else:
                    eval('sign_up_btn.{}()'.format(function))
                print('Login Successfully')
                break
            except NoSuchElementException:
                print('Cant Find {} in Web Retry'.format(path_name),'-'*10)
                i+=1
                time.sleep(1)


    def ret_driver(self):
        return self.driver


    def follow_with_list(self,list):

        for user in list:
            if self.continue_following:
                self.search(user)

                self.click_follow()
            else:
                break
            # time.sleep(10)



    def scroll_page(self,inv_count):
        
        self.driver.execute_script("window.scrollTo(0,{})".format(inv_count*250))

    def like(self,count):
        i=0
        link = None
        inv_count=0
        while self.continue_like and count>0:
        
            # try:
                like=self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/section/div[1]/div[3]/div[1]/div/article[3]/div/div[3]/div/div/section[1]/span[1]/button')
                like.click()
                inv_count+=1
                self.scroll_page(inv_count)
                count-=1

            # except:
            #     print('cant like')
            #     if i>10:
            #         break

    def click_user(self):

        i=0
        link=None
        while not link:
            time.sleep(2)
            try:
                click_follow=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[9]/div/div/div[2]')")
                if click_follow.text == 'Follow':
                    click_follow.click()
                    print('click follow Successfully')
                else :
                    try:
                        # /html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button
                        click_follow=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')")
                        if click_follow.text == 'Follow':
                            click_follow.click() 
                            print('click follow Successfully')  
                    except:
                        print('asd')
                        pass
            except NoSuchElementException:
                print('Cant Find follow btn in Web Retry','-'*10,i)
                i+=1
                time.sleep(1)             
                # if i>10:
                #     self.clear_search()
                #     break 
    
    def click_head(self):
        i=0
        link=None
        while not link:
            time.sleep(2)
            try:
                click_follow=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[9]/div/div/div[2]')")
                if click_follow.text == 'Follow':
                    click_follow.click()
                    print('click follow Successfully')
                else :
                    try:
                        # /html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button
                        click_follow=eval("self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')")
                        if click_follow.text == 'Follow':
                            click_follow.click() 
                            print('click follow Successfully')  
                    except:
                        print('asd')
                        pass
            except NoSuchElementException:
                print('Cant Find follow btn in Web Retry','-'*10,i)
                i+=1
                time.sleep(1)             
                if i>10:
                    self.clear_search()
                    break 
# /html/body/div[1]/div/span[2]/div/span/div/div   main mini page


    def get_user(self):
        self.name=[]
        i=0
        link=None
        while not link:
            time.sleep(2)
            for count in range(2,100):
                self.name=[]
                try:
                    print(count)
                    click_follow=self.driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/div/div[{}]/div/div/div[2]/div[1]/div/span'.format(count))
                    name_=click_follow.text
                    if name_[0]=='+':
                        self.name.append(name_)
                        print(name_)
                except:
                    print('pass')
                if self.name!=[]:
                    self.save()
            


    def save(self):
        with open('phones.txt', 'a+') as f:
            f.write(str(self.name))
                

#/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/div/div[4]/div/div/div[2]/div[1]   users
# /html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/div/div[5]/div/div/div[2]/div[1]/div



if __name__=='__main__':
    init=True
    get_users=False
    follow_with_text=False

    if init:
        conn_insta=connection()
        conn_insta.set_init()
        insta_login_url='https://web.whatsapp.com/'
        conn_insta.get_url(insta_login_url)
        # conn_insta.set_login_pams('milad_1245678','milad123456')
        conn_insta.click_user()
        conn_insta.get_user()

    while True:
        a=1
        pass
    # if get_users:
    #     conn_insta.get_follower_from_page('dr.ronakeshghi',1000)
    
    # follow_obj=following()

    # if follow_with_text:
    #     user_list = follow_obj.user_files()
    # # print(user_list[1])
    # if init and follow_with_text:
    #     conn_insta.follow_with_list(user_list)
# /html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[9]/div/div/div[2]

# /html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/section/div[1]/div[3]/div[1]/div/article[3]/div/div[3]/div/div/section[1]/span[1]/button

# /html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/section/div[1]/div[3]/div[1]/div/article[3]/div/div[3]/div/div/section[1]/span[1]/button




