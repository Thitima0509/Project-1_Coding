import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันคำนวณค่างวดผ่อนบ้าน
def calculate_monthly_payment(house_price, mrr, interest_rate, years):
    annual_interest_rate = interest_rate + mrr  # คำนวณอัตราดอกเบี้ยที่แท้จริง
    months = years * 12  # จำนวนเดือนทั้งหมด
    monthly_interest_rate = (annual_interest_rate / 100) / 12  # อัตราดอกเบี้ยรายเดือน
    
    # คำนวณค่างวดผ่อนรายเดือน (M)
    M = (house_price * monthly_interest_rate * (1 + monthly_interest_rate) ** months) / \
        ((1 + monthly_interest_rate) ** months - 1)
    
    return M

# ฟังก์ชันตรวจสอบวงเงินที่สามารถผ่อนต่อเดือนได้
def get_maximum_loan_payment(salary, percentage):
    return (salary * percentage) / 100

# ฟังก์ชันคำนวณและแสดงผล
def calculate():
    try:
        house_price = float(entry_house_price.get())
        years = int(entry_years.get())
        mrr = float(entry_mrr.get())
        interest_rate = float(entry_interest_rate.get())
        salary = float(entry_salary.get())
        
        max_payment_40 = get_maximum_loan_payment(salary, 40)
        max_payment_20 = get_maximum_loan_payment(salary, 20)
        
        monthly_payment = calculate_monthly_payment(house_price, mrr, interest_rate, years)
        
        if monthly_payment > max_payment_40:
            result_text = f"ไม่สามารถผ่อนได้ ค่างวด {monthly_payment:,.2f} บาท สูงเกิน 40% ของเงินเดือนคุณ ({max_payment_40:,.2f} บาท)"
        elif max_payment_20 <= monthly_payment <= max_payment_40:
            result_text = f"ค่างวดที่ต้องจ่ายต่อเดือน: {monthly_payment:,.2f} บาท (สามารถผ่อนได้)"
        else:
            result_text = f"ค่างวดที่ต้องจ่ายต่อเดือน: {monthly_payment:,.2f} บาท (สามารถผ่อนได้แบบสบายกระเป๋า)"
        
        messagebox.showinfo("ผลการคำนวณ", result_text)
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขที่ถูกต้องในทุกช่อง")

# สร้าง GUI
root = tk.Tk()
root.title("โปรแกรมคำนวณค่างวดผ่อนบ้าน")

# สร้าง Label และ Entry สำหรับรับข้อมูล
labels = ["ราคาบ้าน (บาท):", "จำนวนปีที่ผ่อนชำระ:", "อัตราดอกเบี้ย MRR (%):", "ส่วนลด MRR (%):", "เงินเดือนของคุณ:"]
entries = []
for i, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_house_price, entry_years, entry_mrr, entry_interest_rate, entry_salary = entries

# ปุ่มคำนวณ
btn_calculate = tk.Button(root, text="คำนวณ", command=calculate)
btn_calculate.grid(row=len(labels), columnspan=2, pady=10)

# เริ่ม GUI
root.mainloop()
