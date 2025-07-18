# extensions.py

filename = input("Enter the filename: ").lower().strip()

if filename.endswith('.gif'):
    print("image/gif")
elif filename.endswith('.jpg') or filename.endswith('.jpeg'):
    print("image/jpeg")
elif filename.endswith('.png'):
    print("image/png")
elif filename.endswith('.pdf'):
    print("application/pdf")
elif filename.endswith('.txt'):
    print("text/plain")
elif filename.endswith('.zip'):
    print("application/zip")
elif filename.endswith('.htm') or filename.endswith('.html'):
    print("text/html")
elif filename.endswith('.css'):
    print("text/css")
elif filename.endswith('.js'):
    print("text/javascript")
elif filename.endswith('.json'):
    print("application/json")
elif filename.endswith('.xml'):
    print("application/xml")
elif filename.endswith('.mp3'):
    print("audio/mpeg")
elif filename.endswith('.wav'):
    print("audio/wav")
elif filename.endswith('.mp4'):
    print("video/mp4")
elif filename.endswith('.avi'):
    print("video/x-msvideo")
elif filename.endswith('.mpeg'):
    print("video/mpeg")
elif filename.endswith('.csv'):
    print("text/csv")
elif filename.endswith('.doc'):
    print("application/msword")
elif filename.endswith('.docx'):
    print("application/vnd.openxmlformats-officedocument.wordprocessingml.document")
elif filename.endswith('.xls'):
    print("application/vnd.ms-excel")
elif filename.endswith('.xlsx'):
    print("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
elif filename.endswith('.ppt'):
    print("application/vnd.ms-powerpoint")
elif filename.endswith('.pptx'):
    print("application/vnd.openxmlformats-officedocument.presentationml.presentation")
else:
    print("application/octet-stream")
