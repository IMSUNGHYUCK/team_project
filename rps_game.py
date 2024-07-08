from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

cont_win = 0
cont_lose = 0
cont_draw = 0
list_user = ['가위', '바위', '보']

@app.route('/', methods=['GET', 'POST'])
def index():
    global cont_win, cont_lose, cont_draw

    if request.method == 'POST':
        user = request.form['user']
        if user not in list_user:
            return render_template('index.html', message='잘못 입력하셨습니다. 가위, 바위, 보 중 하나를 입력해주세요', cont_win=cont_win, cont_lose=cont_lose, cont_draw=cont_draw)

        num = random.randint(1, 3)
        com = list_user[num - 1]

        if (user == '가위' and com == '보') or (user == '보' and com == '바위') or (user == '바위' and com == '가위'):
            cont_win += 1
            message = f'이겼습니다! 컴퓨터: {com}, 사용자: {user}'
        elif user == com:
            cont_draw += 1
            message = f'비겼습니다! 컴퓨터: {com}, 사용자: {user}'
        else:
            cont_lose += 1
            message = f'졌습니다. 컴퓨터: {com}, 사용자: {user}'

        return render_template('index.html', message=message, cont_win=cont_win, cont_lose=cont_lose, cont_draw=cont_draw)

    return render_template('index.html', cont_win=cont_win, cont_lose=cont_lose, cont_draw=cont_draw)

if __name__ == '__main__':
    app.run(debug=True)
