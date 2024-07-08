from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)


# 초기화 함수
def reset_scores():
    global cont_win, cont_lose, cont_draw, log
    cont_win = 0
    cont_lose = 0
    cont_draw = 0
    log = []


reset_scores()

list_user = ['가위', '바위', '보']
emoji_map = {'가위': '✌️', '바위': '✊', '보': '✋'}


@app.route('/', methods=['GET', 'POST'])
def index():
    global cont_win, cont_lose, cont_draw, log

    if request.method == 'POST':
        user = request.form['user']

        if user == 'reset':
            reset_scores()
            return redirect(url_for('index'))

        if user not in list_user:
            return render_template('index.html', message='잘못 입력하셨습니다. 가위, 바위, 보 중 하나를 선택해주세요', cont_win=cont_win,
                                   cont_lose=cont_lose, cont_draw=cont_draw, log=log)

        num = random.randint(1, 3)
        com = list_user[num - 1]

        if (user == '가위' and com == '보') or (user == '보' and com == '바위') or (user == '바위' and com == '가위'):
            cont_win += 1
            result = '이겼습니다'
        elif user == com:
            cont_draw += 1
            result = '비겼습니다'
        else:
            cont_lose += 1
            result = '졌습니다'

        log_entry = {
            'user': emoji_map[user],
            'com': emoji_map[com],
            'result': result
        }
        log.append(log_entry)

        return render_template('index.html', cont_win=cont_win, cont_lose=cont_lose, cont_draw=cont_draw, log=log)

    return render_template('index.html', cont_win=cont_win, cont_lose=cont_lose, cont_draw=cont_draw, log=log)


if __name__ == '__main__':
    app.run(debug=True)
