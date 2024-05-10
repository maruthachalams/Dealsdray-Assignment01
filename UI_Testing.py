##### S Maruthachalam - UI Testing - 10.05.2024 #####
import time
from datetime import datetime
import os
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.service import Service  
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.chrome.options import Options
from PIL import Image
import io



Urls = []
UrlCount = 1
for i in range(1,6):
    driver = webdriver.Firefox()
    driver.get("https://www.getcalley.com/page-sitemap.xml")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr['+str(i)+']/td[1]/a').click()
    time.sleep(5)
    urlTemp = driver.current_url
    Urls.append(urlTemp)
    driver.close()
    print("Number of URL collected from given website: ",str(UrlCount))
    UrlCount += 1

for URL in Urls:
    CntWkgDir = os.getcwd()
    ParameterSet = [['Firefox','Desktop',1920,1080,1366,768,1536,864],['Firefox','Mobile',360,640,414,896,375,667]]

    for Parameters in ParameterSet:
        i = 0
        for pn in range(2,5):
            pn = pn + i
            dirName =CntWkgDir+"/"+Parameters[0]+"/"+Parameters[1]+'/'+str(Parameters[pn])+'x'+str(Parameters[pn+1])
            i += 1
            if not os.path.exists(dirName):
                os.makedirs(dirName)
            opts = FirefoxOptions()    
            opts.add_argument("--width="+str(Parameters[pn]))
            opts.add_argument("--height="+str(Parameters[pn+1]))
            
            driver = Firefox(options=opts)
            driver.get(URL)
            time.sleep(2)
            now = datetime.now()
            FileName = now.strftime('%Y-%m-%d_%H-%M')
            driver.save_full_page_screenshot(dirName+'/'+str(FileName)+'.png')
            KeyName = Parameters[0]+'-'+Parameters[1]+'-'+str(Parameters[pn])+'x'+str(Parameters[pn+1])
            print("Completed parameter: ",KeyName)
            driver.close()
    
    ParameterSet = [['Chrome','Desktop',1920,1080,1366,768,1536,864],['Chrome','Mobile',360,640,414,896,375,667]]
    
    for Parameters in ParameterSet:
        i = 0
        for pn in range(2,5):
            pn = pn + i
            dirName =CntWkgDir+"/"+Parameters[0]+"/"+Parameters[1]+'/'+str(Parameters[pn])+'x'+str(Parameters[pn+1])
            i += 1
            if not os.path.exists(dirName):
                os.makedirs(dirName)
           
            
            driver = webdriver.Chrome()
            driver.set_window_size(Parameters[pn], Parameters[pn+1])
            driver.get(URL)
            time.sleep(5)
            
            now = datetime.now()
            FileName = now.strftime('%Y-%m-%d_%H-%M')
            
            driver.save_screenshot(dirName+'/'+str(FileName)+'.png')
           
            KeyName = Parameters[0]+'-'+Parameters[1]+'-'+str(Parameters[pn])+'x'+str(Parameters[pn+1])
            print("Completed parameter: ",KeyName)
            driver.close()
            