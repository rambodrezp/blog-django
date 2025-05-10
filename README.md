# 📝 Django Blog App

یک پروژه ساده وبلاگ با استفاده از Django، ساخته شده برای تمرین و آشنایی با مفاهیم پایه‌.
![view](Screenshot(505).png)

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
## Build and Run Dockerfile
```bash
docker build -t blog-django .
docker run -p 8000:8000 blog-django
```
## Push to Docker Hub
```bash
docker tag blog-django your_dockerhub_username/blog-django:latest
docker push your_dockerhub_username/blog-django:latest
```
## Deploy with Kubernetes (Minikube)
```bash
minikube image load blog-django
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
##Manual Scaling
```bash
kubectl scale deployment blog-django-deployment --replicas=3
```
## Autoscaling with HPA
```bash
minikube addons enable metrics-server
kubectl autoscale deployment blog-django-deployment --cpu-percent=50 --min=1 --max=5
kubectl get hpa
```

## 🔮 برنامه‌های آینده
### فعال‌سازی ثبت‌نام و لاگین خودکار

### افزودن بخش کامنت برای پست‌ها

### جستجوی پست‌ها


