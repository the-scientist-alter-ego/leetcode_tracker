from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")

list_minions = ['moi', 'Leon','Duang','Jiuxin','Zhatangmian','Zmy','Ack','Tim','Tansy','FangWenxuan','Charlotte','Popo','番一番']
list_urls = ['https://leetcode-cn.com/u/si-yue-16/','https://leetcode.com/leonsy5222/','https://leetcode-cn.com/u/duangyy/','https://leetcode-cn.com/u/rui-809/',
'https://leetcode-cn.com/u/zha-tang-mian-you-bing/','https://leetcode.com/onezmy/','https://leetcode-cn.com/u/real_vegetable_chicken/','https://leetcode.com/mingxuanche/',
            'https://leetcode.com/glooooria/','https://leetcode.com/FangWenxuan/','https://leetcode.com/charlilili/','https://leetcode-cn.com/u/eno_z/',
            'https://leetcode.com/yachialice/']
list_targets = ['d2','d3','d1','d1','d1','d1','w4','w4','w4','w5','w5','w10']
for i in range(len(list_urls)):
    print(list_minions[i])
for i in range(len(list_urls)):
    driver.get(list_urls[i])
    time.sleep(3)
    bs = BeautifulSoup(driver.page_source,'html.parser')
#     print(list_minions[i])
    if '-cn' in list_urls[i]:
        all_badges = bs.find_all('div', attrs={'class': 'css-1u1fy0h-CardTitle e1c4m4sz4'})
        all_badges
        if len(all_badges) == 3:
            count = int(all_badges[1].b.text)
        else:
            count = int(all_badges[0].b.text)
#         count
#         count = int(bs.find('div', attrs={'class': 'css-1u1fy0h-CardTitle e1c4m4sz4'}).b.text)
        print(count)
    else:
        try:
            count = int(bs.find('div', attrs={'class': 'total-solved-count__2El1 css-57pydk'}).text)
            print(count)
        except:
            pass
