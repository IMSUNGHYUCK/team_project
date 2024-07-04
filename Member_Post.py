class Member:
    def __init__(self, name, user_id, password):
        self.name = name
        self.user_id = user_id
        self.password = password



    def display(self):
        print(f'사용자의 이름은 {self.name}, 사용자의 아이디는 {self.user_id} 입니다.')

    def __repr__(self):
        return f"{self.name}님의 회원정보 아이디: {self.user_id}"


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f"{self.author}님이 작성하신 제목:{self.title} 내용: {self.content}"


members = {}


num_members = int(input("멤버 수를 입력하세요: "))
for i in range(num_members):
    name = input(f"{i+1}번째 멤버의 이름을 입력하세요: ")
    user_id = input(f"{name}님의 사용자 아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    members[user_id] = Member(name, user_id, password)


for member in members.values():
    print(member)

posts = []


for member in members.values():
    title = input(f"{member.name}님, 포스트의 제목을 입력하세요: ")
    content = input("포스트의 내용을 입력하세요: ")
    posts.append(Post(title, content, member.name))


for post in posts:
    print(post)


print("\n'임성혁'이 작성한 포스트 제목:")
for post in posts:
    if post.author == '임성혁':
        print(post.title)


print("\n포스트 내용에 '사랑'이 포함된 포스트 제목:")
for post in posts:
    if '사랑' in post.content:
        print(post.title)
