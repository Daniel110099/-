"""
自動建立所有需要的資料夾
執行一次即可
"""
import os

# 專案根目錄（目前所在位置）
根目錄 = "."

# 需要建立的資料夾列表
資料夾列表 = [
    "資料集/訓練/螺絲",
    "資料集/訓練/螺帽",
    "資料集/訓練/墊片",
    "資料集/訓練/彈簧",
    "資料集/訓練/釘子",
    "資料集/訓練/華司",
    "暫存_未知圖片",
]

print("="*50)
print("📁 建立資料夾結構")
print("="*50)

for 資料夾 in 資料夾列表:
    完整路徑 = os.path.join(根目錄, 資料夾)
    if not os.path.exists(完整路徑):
        os.makedirs(完整路徑)
        print(f"✅ 已建立：{資料夾}")
    else:
        print(f"⏭️ 已存在：{資料夾}")

print("\n" + "="*50)
print("📂 資料夾結構：")
print("="*50)

# 顯示目錄樹
def 顯示目錄樹(路徑, 縮排=""):
    if os.path.isdir(路徑):
        print(f"{縮排}📁 {os.path.basename(路徑)}/")
        for 項目 in sorted(os.listdir(路徑)):
            if not 項目.startswith('.'):
                顯示目錄樹(os.path.join(路徑, 項目), 縮排 + "    ")

顯示目錄樹("資料集")
顯示目錄樹("暫存_未知圖片")

print("\n✅ 資料夾建立完成！")
print("\n下一步：")
print("  1. 將五金零件照片放入對應資料夾")
print("  2. 執行 python 訓練模型.py")
print("  3. 執行 python 自我學習辨識.py")
