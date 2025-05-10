# 📝 Django Blog App

یک پروژه ساده وبلاگ با استفاده از Django، ساخته شده برای تمرین و آشنایی با مفاهیم پایه‌.

## 📌 امکانات

- ساخت، ویرایش و حذف پست‌ها توسط کاربران ایجاد شده توسط ادمین
- صفحه‌ی اصلی برای نمایش پست‌ها
- پنل ادمین برای مدیریت کامل کاربران و پست‌ها

---

## ⚙️ نصب و اجرا

### 1. ساخت محیط مجازی و فعال‌سازی
```bash
python -m venv venv
```
### 2. نصب وابستگی‌ها
```bash
pip install -r requirements.txt
```
### 3. اجرای migrate
```bash
python manage.py migrate
```
### 4. ساخت ادمین
```bash
python manage.py createsuperuser
```
### 5. اجرای سرور
```bash
python manage.py runserver
```
### 6. سپس به آدرس زیر می رویم:
http://127.0.0.1:8000/
## 🧩 ساختار پروژه
```bash
blog_project/
├── blog/               # اپ اصلی
│   ├── templates/      # قالب‌ها
│   ├── views.py        # ویوها
│   └── models.py       # مدل پست‌ها
├── blog_project/
│   └── settings.py     # تنظیمات Django
├── db.sqlite3          # پایگاه داده پیش‌فرض
└── manage.py
```
## 🔮 برنامه‌های آینده
### فعال‌سازی ثبت‌نام و لاگین خودکار

### افزودن بخش کامنت برای پست‌ها

### جستجوی پست‌ها


