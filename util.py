import random

def get_movie(label):
    pos_movies = ["나 홀로 집에", "브리짓 존스의 다이어리", "로맨틱 홀리데이", "언포기버블", "6 언더그라운드", "그린북", "폴라", "코드 8", "올드 가드", "스타 이즈 본"]
    neg_movies = ["러브 액츄얼리", "어바웃 타임", "비긴어게인", "찰리와 초콜렛 공장", "그 여자 작사 그 남자 작곡", "맘마미아", "겨울왕국", "반창꼬", "로마 위드 러브", "러브레터", "말할 수 없는 비밀", "초속 5센티미터"]

    if label == "positive": return random.choice(pos_movies)
    elif label == "negative": return random.choice(neg_movies)
    else: return None

def get_temperature(score, label):
    if label == "positive": return int(abs(score - 0.5) * 200)
    elif label == "negative": return int((score - 0.5) * (-20))
    else: return None
        
