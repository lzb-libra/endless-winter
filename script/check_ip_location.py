import requests
import time

# 输入文件（每行一个 IP）
INPUT_FILE = 'ips.txt'

# 输出：所有 IP 的归属地信息，以及非中国 IP
OUTPUT_ALL = True  # 是否打印所有 IP 的归属地
OUTPUT_NON_CN = True  # 是否单独列出非中国（非 CN）的 IP

# IP 查询 API（免费，无需 key，但有速率限制）
API_URL = "http://ip-api.com/json/{}"

def query_ip_location(ip):
    try:
        url = API_URL.format(ip)
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get('status') == 'success':
            return {
                'ip': ip,
                'country': data.get('country', 'Unknown'),
                'countryCode': data.get('countryCode', '??'),
                'region': data.get('regionName', 'Unknown'),
                'city': data.get('city', 'Unknown'),
                'isp': data.get('isp', 'Unknown'),
                'is_cn': data.get('countryCode') == 'CN'
            }
        else:
            return {
                'ip': ip,
                'error': data.get('message', 'Unknown error'),
                'is_cn': False
            }
    except Exception as e:
        return {
            'ip': ip,
            'error': str(e),
            'is_cn': False
        }

def main():
    non_cn_ips = []

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        ips = [line.strip() for line in f if line.strip()]

    for idx, ip in enumerate(ips):
        print(f"\n[{idx+1}/{len(ips)}] 正在查询 IP: {ip}")
        info = query_ip_location(ip)
        if 'error' in info:
            print(f"❌ 查询失败: {ip}，错误：{info['error']}")
        else:
            country = info.get('country', 'Unknown')
            cc = info.get('countryCode', '??')
            region = info.get('region', 'Unknown')
            city = info.get('city', 'Unknown')
            isp = info.get('isp', 'Unknown')

            if OUTPUT_ALL:
                print(f"✅ IP: {ip}")
                print(f"   国家: {country} ({cc})")
                print(f"   地区: {region}")
                print(f"   城市: {city}")
                print(f"   运营商: {isp}")
                print(f"   是否中国: {'是' if info.get('is_cn') else '否'}")

            if not info.get('is_cn'):
                non_cn_ips.append(info)
        
        # 避免触发 API 速率限制（免费版约 45次/分钟）
        time.sleep(1)  # 每秒查询一个，安全且合规

    # 单独输出非中国 IP 列表
    if OUTPUT_NON_CN and non_cn_ips:
        print("\n" + "="*50)
        print("🔴 以下 IP **不属于中国大陆（非 CN）**：")
        print("="*50)
        for item in non_cn_ips:
            ip = item['ip']
            cc = item.get('countryCode', '??')
            country = item.get('country', 'Unknown')
            print(f"IP: {ip} → 国家: {country} ({cc})")

if __name__ == '__main__':
    main()