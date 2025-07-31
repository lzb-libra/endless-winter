import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def analyzingWebSite(name, url, save_dir):
    print(f'{name}')
    encodedName = quote(name)

    # 发送请求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url + encodedName + "/", headers=headers)

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

        finish_div = finish_div.find_all("div", recursive=False)

        # print("TX--------------------------------\r\n")
        tx_skills = finish_div[0]
        tx_skills = tx_skills.find_all("div", class_="row")
        for index, txSkill in enumerate(tx_skills):
            analysisSkill(txSkill, "tx", index, save_dir)

        # print("YZ--------------------------------\r\n")
        yz_skills = finish_div[1]
        yz_skills = yz_skills.find_all("div", class_="row")
        for index, yzSkill in enumerate(yz_skills):
            analysisSkill(yzSkill, "yz", index, save_dir)
    else:
        print("请求失败：", response.status_code)

def analysisSkill(skill, type, index, save_dir):
    # print(skill.prettify())

    # 下载图片
    img = skill.find("img")
    download_img(img.get("src"), type + "_" + str(index + 1) + ".png", save_dir)

    # 获取名称
    label = skill.find("h5")
    skill_name = label.get_text(strip=True)
    # print(skill_name)
    
    desc = skill.find("p")
    skill_desc = desc.get_text("\n", strip=True).split("\n")[0]
    skill_desc = skill_desc.replace("\n", "").replace("\r", "")
    # print(skill_desc)

    print(f'{type}_{index+1}: {{ label: "{skill_name}", desc: "{skill_desc}" }},')
    # print('')

def download_img(url, file_name, save_dir):
    # 创建目录（如果不存在）
    os.makedirs(save_dir, exist_ok=True)

    # 拼接完整路径
    file_path = os.path.join(save_dir, file_name)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # 保存到本地文件
        with open(file_path, "wb") as f:
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
    analyzingWebSite(
        "布拉德利", 
        "https://wjdrgl.centurygames.cn/heroes/",
        "D:/workstation/MyProjects/endless-winter/public/images/heros/lore/S7/BuLaDeLi"
    )
