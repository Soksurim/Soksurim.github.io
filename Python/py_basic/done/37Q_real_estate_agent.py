# 부동산 프로그램 작성

# 출력 예시
# 총 n개의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")

total = []
total.append(House("강남","아파트","매매","10억","2010년"))
total.append(House("마포","오피스텔","전세","5억","207년"))
total.append(House("송파","빌라","월세","500/50","2000년"))

print(f"총 {len(total)}개의 매물이 있습니다.")
for m in total:
    House.show_detail(m)
