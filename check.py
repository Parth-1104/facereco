import face_recognition
image_path = "path/to/your/image.jpg"
image = face_recognition.load_image_file(image_path)
face_locations = face_recognition.face_locations(image)
print("Number of faces found:", len(face_locations))
