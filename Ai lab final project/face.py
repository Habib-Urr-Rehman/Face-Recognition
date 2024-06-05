
###############################
import cv2
import face_recognition
import threading
import tkinter as tk
from tkinter import messagebox

class FaceRecognitionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Face Recognition App")

        self.video_cap = cv2.VideoCapture(0)
        self.exit_flag = threading.Event()
        self.known_encodings = self.train_model()
        self.known_encodings_lfw = []

        self.create_widgets()

    def train_model(self, image_paths=None, lfw_mode=False):
        
        training_image_paths = image_paths or [

           
            "D:/ALL COURSES/5th Semester/AI Lab/Ai project/Project and dataset/sample_img/ha.jpeg",
            "D:/ALL COURSES/5th Semester/AI Lab/Ai project/Project and dataset/sample_img/tal.jpeg",
        
        ]

        known_encodings = []
        for image_path in training_image_paths:
            image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(image)

            if face_encoding:
                known_encodings.append(face_encoding[0])

      
        if lfw_mode:
            lfw_image_paths = [
                "D:/ALL COURSES/5th Semester/AI Lab/Ai project/Project and dataset/sample_img/lfw1.jpg",
                "D:/ALL COURSES/5th Semester/AI Lab/Ai project/Project and dataset/sample_img/lfw2.jpg",
               
            ]

            known_encodings_lfw = []
            for lfw_path in lfw_image_paths:
                lfw_image = face_recognition.load_image_file(lfw_path)
                lfw_encoding = face_recognition.face_encodings(lfw_image)

                if lfw_encoding:
                    known_encodings_lfw.append(lfw_encoding[0])

            return known_encodings_lfw

        return known_encodings

    def recognize_faces(self, known_encodings):
        while not self.exit_flag.is_set():
            ret, video_data = self.video_cap.read()
            rgb_frame = cv2.cvtColor(video_data, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_frame)

            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(video_data, (left, top), (right, bottom), (0, 255, 0), 2)

                face_encoding = face_recognition.face_encodings(rgb_frame, [(top, right, bottom, left)])[0]

                results = face_recognition.compare_faces(known_encodings, face_encoding)

                name = "Unknown"
                for i, result in enumerate(results):
                    if result:
                        name = f"Known Person {i + 1}"
                        break

                cv2.putText(video_data, name, (left + 6, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            cv2.imshow("video_live", video_data)

            key = cv2.waitKey(10)
            if key == ord("a"):
                self.exit_flag.set()
                break

    def recognize_faces_lfw(self):
        while not self.exit_flag.is_set():
            ret, video_data = self.video_cap.read()
            rgb_frame = cv2.cvtColor(video_data, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_frame)

            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(video_data, (left, top), (right, bottom), (0, 255, 0), 2)

                face_encoding = face_recognition.face_encodings(rgb_frame, [(top, right, bottom, left)])[0]

                results = face_recognition.compare_faces(self.known_encodings_lfw, face_encoding)

                name = "Unknown"
                for i, result in enumerate(results):
                    if result:
                        name = f"Known Person {i + 1}"
                        break

                cv2.putText(video_data, name, (left + 6, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            cv2.imshow("video_live", video_data)

            key = cv2.waitKey(10)
            if key == ord("a"):
                self.exit_flag.set()
                break

    def face_recognition_loop(self):
        self.recognize_faces(self.known_encodings)

    def face_recognition_loop_lfw(self):
        self.known_encodings_lfw = self.train_model(lfw_mode=True)
        self.recognize_faces_lfw()

    def face_detection(self):
        face_cascade = cv2.CascadeClassifier("D:/Python/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

        while not self.exit_flag.is_set():
            ret, video_data = self.video_cap.read()
            col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                col,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            for (x, y, w, h) in faces:
                cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

            video_data = cv2.flip(video_data, 1)

            cv2.imshow("video_live", video_data)

            key = cv2.waitKey(10)
            if key == ord("a"):
                self.exit_flag.set()
                break

    def create_widgets(self):
      
        font_title = ("Helvetica", 20, "bold")
        font_button = ("Helvetica", 14)
        bg_color = "#F5F5F5"
        btn_bg_color = "#4CAF50"
        btn_fg_color = "white"

        self.master.configure(bg=bg_color)

        tk.Label(self.master, text="Face Recognition App", font=font_title, bg=bg_color).pack(pady=10)

        btn_face_detection = tk.Button(
            self.master,
            text="Face Detection",
            command=self.start_face_detection,
            font=font_button,
            bg=btn_bg_color,
            fg=btn_fg_color,
            padx=20,
            pady=10,
            borderwidth=5,
            relief="raised",
        )
        btn_face_detection.pack(pady=10)

        btn_face_recognition = tk.Button(
            self.master,
            text="Face Recognition",
            command=self.start_face_recognition,
            font=font_button,
            bg=btn_bg_color,
            fg=btn_fg_color,
            padx=20,
            pady=10,
            borderwidth=5,
            relief="raised",
        )
        btn_face_recognition.pack(pady=10)

        btn_face_recognition_lfw = tk.Button(
            self.master,
            text="Face Recognition via LFW",
            command=self.start_face_recognition_lfw,
            font=font_button,
            bg=btn_bg_color,
            fg=btn_fg_color,
            padx=20,
            pady=10,
            borderwidth=5,
            relief="raised",
        )
        btn_face_recognition_lfw.pack(pady=10)

        btn_quit = tk.Button(
            self.master,
            text="Quit",
            command=self.quit_app,
            font=font_button,
            bg=btn_bg_color,
            fg=btn_fg_color,
            padx=20,
            pady=10,
            borderwidth=5,
            relief="raised",
        )
        btn_quit.pack(pady=10)

    def start_face_detection(self):
        self.exit_flag.clear()
        self.face_detection()

    def start_face_recognition(self):
        self.exit_flag.clear()
        self.face_recognition_loop()

    def start_face_recognition_lfw(self):
        self.exit_flag.clear()
        self.face_recognition_loop_lfw()

    def quit_app(self):
        self.exit_flag.set()
        self.master.destroy()

def main():
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


