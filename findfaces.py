import face_recognition

image = face_recognition.load_image_file('./img/groups/team2.jpg')

face_locations = face_recognition.face_locations(image)

# array of coords of each face
# coodinates of Top, right, bottom and left

print(face_locations)

print(f'There are {len(face_locations)} people in this images')