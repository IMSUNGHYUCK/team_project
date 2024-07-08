from flask import Flask, render_template, request, redirect, url_for
import random
import sqlite3

app = Flask(__name__)

list_user = ['가위', '바위', '보']
emoji_map = {'가위': '✌️', '바위': '✊', '보': '✋'}


def reset_scores():
    global cont_win, cont_lose, cont_draw
    cont_win = 0
    cont_lose = 0
    cont_draw = 0


reset_scores()


def get_db_connection():
    conn = sqlite3.connect('game.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    global cont_win, cont_lose, cont_draw

    if request.method == 'POST':
        if 'user' in request.form:
            user = request.form['user']
        else:
            user = request.form.get('hidden_user')  # JavaScript에서 설정한 hidden input에서 값을 가져옴

        if user == 'reset':
            reset_scores()
            conn = get_db_connection()
            conn.execute('DELETE FROM game_results')
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

        if user not in list_user:
            return render_template('index.html', message='잘못 입력하셨습니다. 가위, 바위, 보 중 하나를 선택해주세요', cont_win=cont_win,
                                   cont_lose=cont_lose, cont_draw=cont_draw, log=[])

        num = random.randint(1, 3)
        com = list_user[num - 1]

        if (user == '가위' and com == '보') or (user == '보' and com == '바위') or (user == '바위' and com == '가위'):
            cont_win += 1
            result = '승'
        elif user == com:
            cont_draw += 1
            result = '무'
        else:
            cont_lose += 1
            result = '패'

        conn = get_db_connection()
        conn.execute('INSERT INTO game_results (user_choice, com_choice, result) VALUES (?, ?, ?)',
                     (user, com, result))
        conn.commit()
        conn.close()

    conn = get_db_connection()
    log = conn.execute(
        'SELECT id, user_choice, com_choice, result, timestamp FROM game_results ORDER BY timestamp DESC').fetchall()
    conn.close()

    log_entries = [
        {'game_id': entry['id'], 'user': emoji_map[entry['user_choice']], 'com': emoji_map[entry['com_choice']],
         'result': entry['result']} for entry in log]

    return render_template('index.html', cont_win=cont_win, cont_lose=cont_lose, cont_draw=cont_draw, log=log_entries)


if __name__ == '__main__':
    app.run(debug=True)
