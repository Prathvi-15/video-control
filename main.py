import cv2 
import mediapipe as mp
import pyautogui
import time

def count_fingers(lst):
    cnt = 0

thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2