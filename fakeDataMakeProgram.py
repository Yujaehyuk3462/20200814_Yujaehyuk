import random
import faker
import csv
import os

# Faker를 사용하여 랜덤 이름 생성
fake = faker.Faker()

# 랜덤 데이터 생성 함수
def generate_random_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "이름": fake.name(),  # 랜덤 이름
            "나이": random.randint(18, 22),  # 나이: 18~22세
            "성적": random.randint(0, 100)  # 성적: 0~100
        }
        data.append(record)
    return data

# 랜덤 데이터 300명 생성
new_data = generate_random_data(300)

def save_to_csv(directory, filename, new_data):
    filepath = os.path.join(directory, filename)
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = new_data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_data)

# 현재 디렉토리 저장
current_dir = os.path.dirname(os.path.abspath(__file__))
save_to_csv(current_dir, "nameList.csv", new_data)