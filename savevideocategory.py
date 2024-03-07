import os
import cv2
from tqdm import tqdm

def save_video_by_category(path, categories):
    for category in categories:
        img_array = []
        height, width = 0, 0
        for filename in tqdm(sorted([f for f in os.listdir(path) if category in f], key=lambda x: extract_number(x))):
            img = cv2.imread(os.path.join(path, filename))
            if img is None:  # 이미지 파일이 아닐 경우 건너뛰기
                continue
            if height != 0:
                img = cv2.resize(img, (width, height))
            else:
                height, width, _ = img.shape
                size = (width, height)
            img_array.append(img)

        if img_array:  # 이미지 배열이 비어있지 않을 경우에만 비디오 생성
            out_name = category + '_video'
            out = cv2.VideoWriter(out_name + '.mp4', 0x7634706d, 10, size) #10 : frame 수, 변경 가능
            for i in img_array:
                out.write(i)
            out.release()
            print(f'{out_name}.mp4 saved successfully')

def extract_number(filename):
    import re
    numbers = re.findall(r'\d+', filename)
    return int(numbers[1]) if numbers else 0 # 시간을 기준으로 sort하기 때문에 숫자가 나오는 부분

# 사용 예시
path = '/home/yeom/Desktop/youngeon/hand_pose/dataset/edgecase3_240305'  # 폴더 경로를 입력하세요
categories = ['box','skeleton','mesh'] # image 카테고리에 따라 변경하면 됩니다.
save_video_by_category(path, categories)


