import requests
from lxml import html

baseurl = "https://you.ctrip.com/"

response = requests.get(baseurl)
tree = html.fromstring(response.content)

# 使用XPath选择器
state_area = tree.xpath("//div[@class='city-selector-tab'][2]//div[@class='city-selector-tab-main-city']")


citys={}

# 打印选中的元素的文本内容
for area in state_area:
    base_area = area.xpath(".//div[@class='city-selector-tab-main-city-title']")
    ss_area = area.xpath(".//a")

    ss_city = base_area[0].text_content().strip()
    citys[ss_city] = []
    # 打印链接和文本
    for link in ss_area:
        url = link.get('href')  # 获取 href 属性
        link_text = link.text_content().strip()  # 获取链接文本
        citys[ss_city].append({ "城市": link_text,"url": url.replace("place","sight")})
        print(f"链接: {url}, 文本: {link_text}")

print(citys)
