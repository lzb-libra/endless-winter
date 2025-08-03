import os, re, platform, requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def analyzingWebSite(name, url, save_dir):
    print(f'{name}\r\n')
    encodedName = quote(name)

    # 发送请求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url + encodedName + "/", headers=headers)

    if response.status_code == 200:
        # 解析 HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # # 解析故事
        analysisStory(soup)

        # # 解析来源
        analysisSource(soup)

        # # 解析技能
        analysisSkill(soup, save_dir)

        # 解析专武
        analysisSpecial(soup, save_dir)
        
    else:
        print("请求失败：", response.status_code)

# 解析故事
def analysisStory(soup):
    story_div = soup.find("div", id="basic-info")
    if story_div:
        inner_divs = story_div.find_all("div", recursive=False)
        second_div = inner_divs[1]
        story = second_div.find("p")
        story = story.decode_contents()
        story = re.sub(r"\s*\n\s*", "", story).strip()
        print(f'"story": "{story}",')
    else:
        print("没有找到故事信息")

# 解析来源
def analysisSource(soup):
    source_div = soup.find("div", id="sources")
    if source_div:
        inner_divs = source_div.find_all("div", recursive=False)
        second_div = inner_divs[1]

        li = second_div.find_all("li")
        sources = ''
        for item in li:
            sources += f'\"{item.get_text(strip=True)}\", '

        print(f'"source": [{sources[:-2]}],')
    else:
        print("没有找到获取来源信息")

# 解析技能
def analysisSkill(soup, save_dir):
    # 获取 id=skills 的 div
    skills_div = soup.find("div", id="skills")
    if skills_div:
        # 找到里面所有子 div
        inner_divs = skills_div.find_all("div")

        # 获取第二个 div（索引从 0 开始，所以是 [1]）
        second_div = inner_divs[1]

        finish_div = second_div.find_all("div")
        finish_div = finish_div[0]

        finish_div = finish_div.find_all("div")
        finish_div = finish_div[0]

        finish_div = finish_div.find_all("div", recursive=False)

        print("skill: {")

        tx_skills = finish_div[0]
        tx_skills = tx_skills.find_all("div", class_="row")
        for index, txSkill in enumerate(tx_skills):
            analysisSkillDetail(txSkill, "tx", index, save_dir)

        yz_skills = finish_div[1]
        yz_skills = yz_skills.find_all("div", class_="row")
        for index, yzSkill in enumerate(yz_skills):
            analysisSkillDetail(yzSkill, "yz", index, save_dir)

        print("},")
    else:
        print("没有找到技能信息")

def analysisSkillDetail(skill, type, index, save_dir):
    # print(skill.prettify())

    # 下载图片
    img = skill.find("img")
    download_img(img.get("src"), type + "_" + str(index + 1) + ".png", save_dir)

    # 获取名称
    label = skill.find("h5")
    skill_name = label.get_text(strip=True)
    
    desc = skill.find("p")
    skill_desc = desc.get_text("\n", strip=True).split("\n")[0]
    skill_desc = skill_desc.replace("\n", "").replace("\r", "")

    print(f'"{type}_{index+1}": {{ "label": "{skill_name}", "desc": "{skill_desc}" }},')
    # print('')

# 解析专武
def analysisSpecial(soup, save_dir):
    source_div = soup.find("div", id="special")
    if source_div:
        inner_divs = source_div.find_all("div", recursive=False)
        second_div = inner_divs[1]

        second_div = second_div.find_all("div", recursive=False)

        zw_data_div = second_div[0]
        zw_datum = zw_data_div.find_all("div", recursive=False)

        zw_tx_datum = ''
        zw_tx_data = zw_datum[0]
        zw_tx_data = zw_tx_data.find("tbody")
        zw_tx_data = zw_tx_data.find_all("tr", recursive=False)
        for item in zw_tx_data:
            data = item.find("td")
            zw_tx_datum += f'"{data.get_text(strip=True)}", '

        zw_yz_datum = ''
        zw_yz_data = zw_datum[1]
        zw_yz_data = zw_yz_data.find("tbody")
        zw_yz_data = zw_yz_data.find_all("tr", recursive=False)
        for item in zw_yz_data:
            data = item.find("td")
            zw_yz_datum += f'"{data.get_text(strip=True)}", '

        zw_detail = second_div[1]

        all_div = zw_detail.find_all("div", recursive=False)

        # 专武
        zw_div = all_div[0]
        zw_name = zw_div.find("h5")
        zw_img = zw_div.find("img")
        download_img(zw_img.get("src"), "zw.png", save_dir)

        # 专武-探险
        zw_tx_div = all_div[1]
        zw_tx_img = zw_tx_div.find("img")
        zw_tx_name = zw_tx_div.find("h5")
        zw_tx_desc = zw_tx_div.find("p")
        download_img(zw_tx_img.get("src"), "zw-tx.png", save_dir)

        # 专武-远征
        zw_yz_div = all_div[2]
        zw_yz_img = zw_yz_div.find("img")
        zw_yz_name = zw_yz_div.find("h5")
        zw_yz_desc = zw_yz_div.find("p")
        download_img(zw_yz_img.get("src"), "zw-yz.png", save_dir)

        print(f'"weapon": {{ "name": "{zw_name.get_text(strip=True)}", "data": [{zw_tx_datum} "", "", "", {zw_yz_datum[:-2]}], "tx": {{ "name": "{zw_tx_name.get_text(strip=True)}", "desc": "{zw_tx_desc.get_text(strip=True)}" }}, "yz": {{ "name": "{zw_yz_name.get_text(strip=True)}", "desc": "{zw_yz_desc.get_text(strip=True)}" }}}}')
    else:
        print("没有找到专武信息")

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
    else:
        print("下载失败:", response.status_code)

if __name__ == "__main__":
    save_dir = "D:/workstation/MyProjects/endless-winter/public/images/heros/"
    if platform.system() == "Darwin":
        save_dir = "/Users/lizhibao/workspace/projects/GitHub/endless-winter/public/images/heros/"

    heros = [
        {"name": "史密斯", "addr": "rare/ShiMiSi"},
        {"name": "尤金", "addr": "rare/YouJin"},
        {"name": "查理", "addr": "rare/ChaLi"},
        {"name": "克劳瑞斯", "addr": "rare/KeLaoRuiSi"},

        {"name": "谢尔盖", "addr": "epic/XieErGai"},
        {"name": "帕特里克", "addr": "epic/PaTeLiKe",},
        {"name": "凌霜", "addr": "epic/LingXue",},
        {"name": "卢姆·波根", 'addr': "epic/LuMuBoGen"},
        {"name": "杰西", 'addr': "epic/JieXi"},
        {"name": "巴希提", 'addr': "epic/BaXiTi"},
        {"name": "杰塞尔", 'addr': "epic/JieSaiEr"},
        {"name": "吉娜", 'addr': "epic/JiNa"},
        {"name": "书允", 'addr': "epic/ShuYun"},

        {"name": "赫罗尼莫", "addr": "lore/S1/HeLuoNiMo"},
        {"name": "娜塔莉亚", "addr": "lore/S1/NaTaLiYa"},
        {"name": "茉莉", "addr": "lore/S1/MoLi"},
        {"name": "津曼", "addr": "lore/S1/JingMan"},

        {"name": "弗林特", "addr": "lore/S2/FuLinTe"},
        {"name": "菲蘭德-2", "addr": "lore/S2/FeiLanDe"},
        {"name": "阿隆索", "addr": "lore/S2/ALongSuo"},

        {"name": "罗根", "addr": "lore/S3/LuoGen"},
        {"name": "米娅", "addr": "lore/S3/MiYa"},
        {"name": "格雷格", "addr": "lore/S3/GeLeiGe"},

        {"name": "阿赫摩斯", "addr": "lore/S4/AHeMoSi"},
        {"name": "玲奈", "addr": "lore/S4/LingNai"},
        {"name": "琳恩", "addr": "lore/S4/LinEn"},

        {"name": "赫克托", "addr": "lore/S5/HeKeTuo"},
        {"name": "诺拉", "addr": "lore/S5/NuoLa"},
        {"name": "格温", "addr": "lore/S5/GeWen"},

        {"name": "無名", "addr": "lore/S6/WuMing"},
        {"name": "芮妮", "addr": "lore/S6/RuiNi"},
        {"name": "韋恩-2", "addr": "lore/S6/WeiEn"},

        {"name": "艾迪絲", "addr": "lore/S7/AiDiSi"},
        {"name": "哥頓", "addr": "lore/S7/GeDun"},
        {"name": "布拉德利", "addr": "lore/S7/BuLaDeLi"},
    ]
    
    for item in heros:
        analyzingWebSite(
            item["name"], 
            "https://wjdrgl.centurygames.cn/heroes/",
            save_dir + item["addr"]
        )
        print("----------------------------------------------------------------------------------------------------------")
