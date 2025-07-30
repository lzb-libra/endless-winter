import os
import requests
from bs4 import BeautifulSoup

def analyzingWebSite(url):
    # 发送请求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # 解析 HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # 获取 id=skills 的 div
        skills_div = soup.find("div", id="skills")

        # 找到里面所有子 div
        inner_divs = skills_div.find_all("div")

        # 获取第二个 div（索引从 0 开始，所以是 [1]）
        second_div = inner_divs[1]

        finish_div = second_div.find_all("div")
        finish_div = finish_div[0]

        finish_div = finish_div.find_all("div")
        finish_div = finish_div[0]
        # print(finish_div.prettify())

        finish_div = finish_div.find_all("div", recursive=False)
        for (index, item) in enumerate(finish_div):
            print(f"索引 {index}:", item.prettify())

        # print("TX--------------------------------")
        # tx_skills = finish_div[0]
        # tx_skills = tx_skills.find_all("div", class_="row")
        # for txSkill in tx_skills:
        #     print(txSkill.prettify())

        #     # 下载图片
        #     img = txSkill.find("img")
        #     download_img(img.get("src"))

        #     # 获取名称
        #     label = txSkill.find("h5")
        #     print(label.get_text(strip=True))
            
        #     desc = txSkill.find("p")
        #     print(desc.get_text(strip=True))

        # print("YZ--------------------------------")
        # yz_skills = finish_div[1]
        # yz_skills = yz_skills.find_all("div", class_="row", recursive=False)
        # for yzSkill in yz_skills:
        #     # print(yzSkill.prettify())

        #     # 下载图片
        #     img = yzSkill.find("img")
        #     download_img(img.get("src"))

        #     # 获取名称
        #     label = yzSkill.find("h5")
        #     print(label.get_text(strip=True))
            
        #     desc = yzSkill.find("p")
        #     print(desc.get_text(strip=True))
    else:
        print("请求失败：", response.status_code)

def download_img(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # 保存到本地文件
        file_name = os.path.basename(url)  # 自动取文件名
        with open(file_name, "wb") as f:
            for chunk in response.iter_content(1024):  # 分块写入
                f.write(chunk)
        # print(f"下载完成: {file_name}")
    else:
        print("下载失败:", response.status_code)

def upload_file(token, file_path):
    url = 'http://192.168.183.61:3000/api/v1/files/'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, headers=headers, files=files)
    return response.json()


if __name__ == "__main__":
    analyzingWebSite("https://wjdrgl.centurygames.cn/heroes/%e5%b0%a4%e9%87%91/")
