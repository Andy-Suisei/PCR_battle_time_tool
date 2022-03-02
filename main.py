from tkinter import *
import tkinter.messagebox
import re


def time_convert(time):
    if len(time) == 3:
        result_time = int(time) - spend_time
        if time[0] == "1" and 40 < result_time < 100:
            result_time -= 40
    else:
        result_time = int(time[1] + time[3:5]) - spend_time
        if time[1] == "1" and 40 < result_time < 100:
            result_time -= 40

    if result_time > 0:
        return "{:03d}".format(result_time)
    return None


spend_time = 0
ub = re.compile(r'\d\d\d[ ]+\w')
boss_ub = re.compile(r'-+\d\d\d')
ub2 = re.compile(r'0\d:\d\d')


def text_convert(text):
    output_text = []
    for line in text:
        if line:
            if re.match(ub, line):
                if time_convert(line[0:3]):
                    output_text.append(f"{time_convert(line[0:3])}{line[3:]}\n")
            elif re.match(ub2, line):
                if time_convert(line[0:5]):
                    output_text.append(f"{time_convert(line[0:5])}{line[5:]}\n")

            if re.match(boss_ub, line):
                if time_convert(line[4:7]):
                    output_text.append(f"----{time_convert(line[4:7])}{line[7:]}\n")
    return output_text


def convert():
    global spend_time
    spend_time = 90 - int(time_ent.get())
    if spend_time < 0:
        spend_time += 40
    output = text_convert(str(table.get(1.0, END)).split("\n"))
    table.delete(1.0, END)

    for line in output:
        table.insert(END, line)


root = Tk()
root.geometry("400x400")
root.title("公主連結補償刀")
Label(root, text="剩餘時間(格式範例：110、058)：", font="30").place(x=0, y=0)
Label(root, text="")
time_ent = Entry(root)
time_ent.place(x=250, y=0)
table = Text(root, width=55)
table.place(x=5, y=50)
btn = Button(root, text="轉換秒數", font="30", width=43, command=convert)
btn.place(x=1, y=370)
tkinter.messagebox.showinfo("使用方法", "輸入剩餘時間後將軸複製進去文字框中即可使用")
root.mainloop()
