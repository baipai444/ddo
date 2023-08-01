import tkinter as tk
import webbrowser
from flask import Flask, render_template
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def run_tkinter_game():
    jm = tk.Tk()
    jm.title('Jamal')

    ml = tk.Label(jm, text='กดเพื่อนับถือจาเม่า', width=50, font=300, bg='red')
    ml.pack()

    ml2 = tk.Label(jm, text='คลิกด้านหน้า', font=150, fg='red')
    ml2.place(x=10, y=45)

    ml3 = tk.Label(jm, text='พิมพ์ชื่อตัวเองก่อนกด')
    ml3.place(x=330, y=360)

    ji = tk.StringVar()
    tk.Entry(jm, textvariable=ji).place(x=320, y=400)

    count = 0

    def ma():
        ll = ji.get()
        x = ('ไอโง่', ll)
        tk.Label(jm, text=x, font=80, fg='blue').place(x=0, y=400)

    def mm():
        tk.Label(jm, text='จาเม่ารับรู้', font=80, bg='black', fg='red').pack()
        nonlocal count
        count += 1
        labelltext.set(str(count))

    labelltext = tk.StringVar()
    labelltext.set(str(count))

    tk.Button(jm, text='กดเพื่อเคารพ', font=600, command=mm).place(x=100, y=30)
    tk.Button(jm, text='กดเพื่อเสร็จสิ้น', font=600, command=lambda: jm.destroy()).place(x=100, y=60)
    tk.Button(jm, text='กดยืนยัน', command=ma, font=400).place(x=340, y=430)

    tk.Label(jm, borderwidth=5, relief='ridge', textvariable=labelltext, width=10).place(x=350, y=200)

    tk.Button(jm, text='กลับเข้าลิ้ง', font=600, command=open_web_page).place(x=100, y=430)

    jm.geometry("500x500")
    jm.mainloop()

def open_web_page():
    webbrowser.open("http://localhost:8080")

def run_flask_app():
    app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == "__main__":
    threading.Thread(target=run_flask_app).start()
    threading.Thread(target=run_tkinter_game).start()


    


