import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def testJoy(self):
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1["dominant_emotion"],"joy")

    def testAnger(self):
        result1 = emotion_detector("I am really mad about this")
        self.assertEqual(result1["dominant_emotion"],"anger")

    def testDisgust(self):
        result1 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result1["dominant_emotion"],"disgust")

    def testSadness(self):
        result1 = emotion_detector("I am so sad about this")
        self.assertEqual(result1["dominant_emotion"],"sadness")

    def testFear(self):
        result1 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result1["dominant_emotion"],"fear")

if __name__== "__main__":
    unittest.main()
