import requests
import re

# 这里的 ID 你可以换成任何公开的网易云歌单 ID
TARGET_PLAYLIST_ID = "8458697789"
OUTPUT_FILE = "filtered_songs.txt"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://music.163.com/"
}


def contains_chinese(text):
    """判断字符串是否包含中文字符"""
    return re.search(r'[\u4e00-\u9fff]', text) is not None


def get_track_ids(playlist_id):
    """获取歌单内所有歌曲的 ID 列表"""
    url = f"https://music.163.com/api/v6/playlist/detail?id={playlist_id}&n=1000"
    try:
        res = requests.get(url, headers=HEADERS).json()
        return [str(item["id"]) for item in res["playlist"]["trackIds"]]
    except:
        return []


def get_batch_details(ids):
    """批量获取歌曲详情"""
    url = "https://music.163.com/api/song/detail"
    params = {"ids": "[" + ",".join(ids) + "]"}
    try:
        return requests.get(url, headers=HEADERS, params=params).json().get("songs", [])
    except:
        return []


def run():
    print(f"正在处理歌单: {TARGET_PLAYLIST_ID}...")
    track_ids = get_track_ids(TARGET_PLAYLIST_ID)

    all_songs = []
    batch_size = 100
    for i in range(0, len(track_ids), batch_size):
        batch = track_ids[i:i + batch_size]
        songs = get_batch_details(batch)
        all_songs.extend(songs)

    count = 0
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for song in all_songs:
            name = song["name"]
            if contains_chinese(name):
                continue

            artists = "/".join([a["name"] for a in song["artists"]])
            count += 1
            f.write(f"{count}. {name} - {artists}\n")

    print(f"导出完成，共计 {count} 首非中文歌曲，已保存至 {OUTPUT_FILE}")


if __name__ == "__main__":
    run()