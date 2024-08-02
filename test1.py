import eyed3

def extract_metadata(mp3_file):
    try:
        audiofile = eyed3.load(mp3_file)

        if audiofile.tag is None:
            print("No metadata found for this MP3 file.")
            return

        # Extract common metadata
        title = audiofile.tag.title
        artist = audiofile.tag.artist
        album = audiofile.tag.album
        genre = audiofile.tag.genre
        duration = audiofile.info.time_secs  # Duration in seconds

        # Print the extracted metadata
        print("Title:", title)
        print("Artist:", artist)
        print("Album:", album)
        print("Genre:", genre)
        print("Duration (seconds):", duration)

        # Additional metadata stored in the tag
        for tag in audiofile.tag.frame_set:
            print(tag, audiofile.tag.frame_set[tag])

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    mp3_file = r"Music\American Authors - Best day of my life (lyrics) (1).mp3"  # Replace with the path to your MP3 file
    extract_metadata(mp3_file)
























# import cv2

# # Initialize the camera
# cap = cv2.VideoCapture(0)  # 0 indicates the default camera (usually the built-in webcam)

# # Check if the camera was opened successfully
# if not cap.isOpened():
#     print("Error: Could not open camera.")
# else:
#     while True:
#         # Read a frame from the camera
#         ret, frame = cap.read()

#         # Check if the frame was read successfully
#         if not ret:
#             print("Error: Could not read frame.")
#             break

#         # Display the frame in a window
#         cv2.imshow("Camera Feed", frame)

#         # Exit the loop when the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the camera and close the window
#     cap.release()
#     cv2.destroyAllWindows()



# import nltk
# from nltk.corpus import movie_reviews
# from nltk.classify import NaiveBayesClassifier
# from nltk.classify.util import accuracy

# nltk.download("movie_reviews")

# # Define a feature extractor function
# def extract_features(words):
#     return dict([(word, True) for word in words])

# # Prepare the movie reviews dataset
# documents = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)]

# # Shuffle the documents
# import random
# random.shuffle(documents)

# # Extract features and split the dataset into training and testing sets
# featuresets = [(extract_features(words), category) for (words, category) in documents]
# split_ratio = int(len(featuresets) * 0.8)
# train_set, test_set = featuresets[:split_ratio], featuresets[split_ratio:]

# # Train a Naive Bayes classifier
# classifier = NaiveBayesClassifier.train(train_set)

# # Evaluate the classifier's accuracy on the test set
# accuracy_score = accuracy(classifier, test_set)
# print("Classifier Accuracy:", accuracy_score)

# # Classify some example movie reviews
# positive_review = "This movie is absolutely amazing!"
# negative_review = "I hated every moment of this terrible film."

# positive_features = extract_features(positive_review.split())
# negative_features = extract_features(negative_review.split())

# print("Positive Review Classification:", classifier.classify(positive_features))
# print("Negative Review Classification:", classifier.classify(negative_features))
