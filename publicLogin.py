class Login():
                def __init__(self,driver):
                                self.driver=driver
                def login(self,usename,userpass):
                                driver=self.driver

 
                                driver.find_element_by_id("loginform-username").send_keys(usename)
                                driver.find_element_by_id("loginform-password").send_keys(userpass)
                                driver.find_element_by_name("login-button").click()

                def logout(self):
                                driver=self.driver
                                driver.find_element_by_xpath('//*[@id="w3"]/li[2]/form/button').click()
                                driver.quit()
                                
