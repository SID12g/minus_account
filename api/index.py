import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, send_file
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        interest_rate = float(request.form['interest_rate']) / 100
        borrowed = float(request.form['borrowed'])
        periods = int(request.form['periods'])

        amounts = []
        current_amount = borrowed

        for _ in range(periods):
            current_amount += current_amount * interest_rate
            amounts.append(current_amount)

        # 그래프 생성
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, periods + 1), amounts, marker='o')
        plt.title('Debt Growth Over Time')
        plt.xlabel('Months')
        plt.ylabel('Debt Amount (₩)')
        plt.grid(True)

        # 그래프를 이미지로 저장
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()

        return send_file(img, mimetype='image/png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
