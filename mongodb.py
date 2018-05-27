from flask import jsonify

if __name__ == '__main__':
    week = [(29, '200'), (30, '300')]
    for i in range(1, 5):
        week.append((i, i*100))
    print(jsonify(dict(week)))