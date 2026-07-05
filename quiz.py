#!/usr/bin/env python3
"""
vSLAM Quiz Application

An interactive quiz to test knowledge about Visual SLAM
(Simultaneous Localization and Mapping)
"""

import sys


class VSLAMQuiz:
    """A quiz about vSLAM concepts."""

    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.questions = [
            {
                "question": "What does SLAM stand for?",
                "options": [
                    "A) Systematic Location and Mapping",
                    "B) Simultaneous Localization and Mapping",
                    "C) Sequential Location Analysis Method",
                    "D) Spatial Learning and Memory"
                ],
                "answer": "B",
                "explanation": "SLAM stands for Simultaneous Localization and Mapping, "
                              "a technique where a robot builds a map while simultaneously "
                              "tracking its position within that map."
            },
            {
                "question": "What is the primary difference between vSLAM and traditional SLAM?",
                "options": [
                    "A) vSLAM uses visual sensors like cameras",
                    "B) vSLAM is faster",
                    "C) vSLAM doesn't require sensors",
                    "D) vSLAM only works indoors"
                ],
                "answer": "A",
                "explanation": "vSLAM (Visual SLAM) specifically uses visual sensors such as "
                              "cameras to perform SLAM, unlike traditional SLAM which might use "
                              "other sensors like LiDAR or sonar."
            },
            {
                "question": "Which of the following is a key feature detection algorithm used in vSLAM?",
                "options": [
                    "A) SIFT (Scale-Invariant Feature Transform)",
                    "B) HTTP (HyperText Transfer Protocol)",
                    "C) SMTP (Simple Mail Transfer Protocol)",
                    "D) FTP (File Transfer Protocol)"
                ],
                "answer": "A",
                "explanation": "SIFT is a computer vision algorithm used to detect and describe "
                              "local features in images, commonly used in vSLAM systems."
            },
            {
                "question": "What are 'loop closures' in SLAM?",
                "options": [
                    "A) Errors in the mapping process",
                    "B) When the robot returns to a previously visited location",
                    "C) The end of a mapping session",
                    "D) A type of sensor failure"
                ],
                "answer": "B",
                "explanation": "Loop closures occur when the robot recognizes that it has returned "
                              "to a previously visited location, which helps reduce accumulated "
                              "drift and improve map accuracy."
            },
            {
                "question": "Which type of camera is commonly used in vSLAM systems?",
                "options": [
                    "A) Monocular cameras",
                    "B) Stereo cameras",
                    "C) RGB-D cameras",
                    "D) All of the above"
                ],
                "answer": "D",
                "explanation": "vSLAM systems can use monocular cameras (single camera), "
                              "stereo cameras (two cameras for depth), or RGB-D cameras "
                              "(color + depth), each with different advantages."
            },
            {
                "question": "What is the main challenge in vSLAM?",
                "options": [
                    "A) High computational cost",
                    "B) Sensitivity to lighting conditions",
                    "C) Accumulation of estimation errors (drift)",
                    "D) All of the above"
                ],
                "answer": "D",
                "explanation": "vSLAM faces multiple challenges including computational demands, "
                              "sensitivity to lighting and environmental conditions, and the "
                              "accumulation of position estimation errors over time (drift)."
            },
            {
                "question": "What is ORB-SLAM?",
                "options": [
                    "A) A type of orbital satellite",
                    "B) A popular open-source vSLAM algorithm",
                    "C) A mapping software for drones only",
                    "D) A 3D graphics rendering engine"
                ],
                "answer": "B",
                "explanation": "ORB-SLAM (Oriented FAST and Rotated BRIEF SLAM) is a widely-used "
                              "open-source visual SLAM system that works with monocular, stereo, "
                              "and RGB-D cameras."
            },
            {
                "question": "What does the 'localization' part of SLAM refer to?",
                "options": [
                    "A) Finding the local WiFi network",
                    "B) Determining the robot's position in the environment",
                    "C) Identifying local landmarks",
                    "D) Setting up the local coordinate system"
                ],
                "answer": "B",
                "explanation": "Localization in SLAM refers to the process of determining the "
                              "robot's position and orientation within the environment."
            },
            {
                "question": "Which mathematical technique is commonly used for state estimation in SLAM?",
                "options": [
                    "A) Kalman Filter or Extended Kalman Filter",
                    "B) Bubble Sort",
                    "C) Binary Search",
                    "D) Quick Sort"
                ],
                "answer": "A",
                "explanation": "Kalman Filters and Extended Kalman Filters are probabilistic "
                              "methods commonly used to estimate the state (position and map) "
                              "in SLAM systems by combining sensor measurements."
            },
            {
                "question": "What is a 'feature point' in the context of vSLAM?",
                "options": [
                    "A) A distinctive point in an image that can be reliably detected",
                    "B) A defect in the camera lens",
                    "C) A waypoint in the robot's path",
                    "D) A measurement error"
                ],
                "answer": "A",
                "explanation": "Feature points are distinctive locations in images (like corners, "
                              "edges, or blobs) that can be reliably detected and tracked across "
                              "multiple frames, essential for vSLAM."
            }
        ]

    def display_question(self, q_num, question_data):
        """Display a single question with its options."""
        print(f"\n{'='*60}")
        print(f"Question {q_num}/{len(self.questions)}")
        print(f"{'='*60}")
        print(f"\n{question_data['question']}\n")
        for option in question_data['options']:
            print(f"  {option}")
        print()

    def get_answer(self):
        """Get and validate user's answer."""
        while True:
            answer = input("Your answer (A/B/C/D) or 'Q' to quit: ").strip().upper()
            if answer in ['A', 'B', 'C', 'D', 'Q']:
                return answer
            print("Invalid input. Please enter A, B, C, D, or Q to quit.")

    def check_answer(self, user_answer, correct_answer, explanation):
        """Check if the answer is correct and display result."""
        self.total_questions += 1
        if user_answer == correct_answer:
            self.score += 1
            print("\n✓ Correct! Well done!")
        else:
            print(f"\n✗ Incorrect. The correct answer is: {correct_answer}")
        print(f"\nExplanation: {explanation}")
        return user_answer == correct_answer

    def display_final_score(self):
        """Display the final quiz results."""
        print(f"\n{'='*60}")
        print("QUIZ COMPLETED!")
        print(f"{'='*60}")
        print(f"\nYour Score: {self.score}/{self.total_questions}")
        
        if self.total_questions > 0:
            percentage = (self.score / self.total_questions) * 100
            print(f"Percentage: {percentage:.1f}%\n")
            
            if percentage >= 90:
                print("🌟 Excellent! You have a strong understanding of vSLAM!")
            elif percentage >= 70:
                print("👍 Good job! You have a solid grasp of vSLAM concepts.")
            elif percentage >= 50:
                print("📚 Not bad! Keep learning about vSLAM to improve.")
            else:
                print("📖 Keep studying! vSLAM is a complex topic that takes time to master.")
        
        print(f"\n{'='*60}\n")

    def run(self):
        """Run the quiz."""
        print("\n" + "="*60)
        print("Welcome to the vSLAM Quiz!")
        print("="*60)
        print("\nThis quiz will test your knowledge about Visual SLAM")
        print("(Simultaneous Localization and Mapping).\n")
        print("Answer each question by typing A, B, C, or D.")
        print("Type 'Q' at any time to quit.\n")
        input("Press Enter to start...")

        for i, question_data in enumerate(self.questions, 1):
            self.display_question(i, question_data)
            answer = self.get_answer()
            
            if answer == 'Q':
                print("\nQuiz terminated by user.")
                break
            
            self.check_answer(answer, question_data['answer'], question_data['explanation'])
        
        self.display_final_score()


def main():
    """Main entry point for the quiz application."""
    try:
        quiz = VSLAMQuiz()
        quiz.run()
    except KeyboardInterrupt:
        print("\n\nQuiz interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
