class Member:
    def __init__(self,name,user_id,password):
        self.name = name
        self.user_id = user_id
        self.password = password

    def display(self):
        print(f'사용자의 이름은{self.name} 사용자의 아이디는{self.user_id} 입니다.')

    def __repr__(self):
        return f"{self.name}님의 회원정보 아이디:{self.user_id}"



class Post:
    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f"{self.author}님이 작성하신 {self.title}{self.content}"


members = []

user1 = Member('임성혁','dlatjdrnf','1234')
user2 = Member('김철수','dddd','5432')
user3 = Member('홍길동','aaaaa','7890')
user4 = Member(input('이름을 입력하세요'),input('id를 입력하세요'),input('비밀번호를 입력하세요'))

user1.display()
user2.display()
user3.display()
user4.display()


members.append(user1)
members.append(user2)
members.append(user3)
members.append(user4)

posts = []

for member in members:
    print(member)

post1 = Post('제목:안녕하세요','내용:화이팅입니다.',user1.name)
post2 = Post('제목:헬로우','내용:사랑합니다',user1.name)
post3 = Post('제목:니하오','내용:할 수 있습니다.',user1.name)
posts.append(post1)
posts.append(post2)
posts.append(post3)

post4 = Post('제목:안녕하세요','내용:화이팅입니다.',user2.name)
post5 = Post('제목:헬로우','내용:사랑합니다',user2.name)
post6 = Post('제목:니하오','내용:할 수 있습니다.',user2.name)
posts.append(post4)
posts.append(post5)
posts.append(post6)

post7 = Post('제목:안녕하세요','내용:화이팅입니다.',user3.name)
post8 = Post('제목:헬로우','내용:사랑합니다',user3.name)
post9 = Post('제목:니하오','내용:할 수 있습니다.',user3.name)
posts.append(post7)
posts.append(post8)
posts.append(post9)

post10 = Post(input('제목을 입력하세요'),input('내용을 입력하세요'),user4.name)
post11 = Post(input('제목을 입력하세요'),input('내용을 입력하세요'),user4.name)
post12 = Post(input('제목을 입력하세요'),input('내용을 입력하세요'),user4.name)
posts.append(post10)
posts.append(post11)
posts.append(post12)

for post in posts:
    print(post)

for post in posts:
    if post.author == '임성혁':
        print(post.title)

for post in posts:
    if '사랑' in post.content:
        print(post.title)




# TODO : 코드 구현이 필요합니다.
