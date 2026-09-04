#chatbot for FAQS
import string
your_doubt={
    "How to get addmision in college":"go on collge website & check of eligibility criteriya",
    "what soxuments are rewuired?":"marksheet, adhar card, id ",
    "any scholarship is available?":"yes:DRCC",
    "in this college hostle is available":" yes",
    "how many students are studying in this college":"more than 1k students",
    "What is the last date for admission": "30th September"
}



import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)
from sklearn.feature_extraction.text import TfidfVectorizer

faq_questions = list(your_doubt.keys())
faq_answers = list(your_doubt.values())

cleaned_questions = [clean_text(q) for q in faq_questions]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(cleaned_questions)
from sklearn.metrics.pairwise import cosine_similarity

def get_answer(user_query):
    user_clean = clean_text(user_query)
    user_vector = vectorizer.transform([user_clean])
    similarities = cosine_similarity(user_vector, faq_vectors)
    best_match_index = similarities.argmax()
    return faq_answers[best_match_index]

   # Testing the chatbot
while True:
    user_input = input("Apna sawaal poocho (exit likhne se ruk jayega): ")
    if user_input.lower() == "exit":
        break
    
    user_clean = clean_text(user_input)
    user_vector = vectorizer.transform([user_clean])
    similarities = cosine_similarity(user_vector, faq_vectors)
    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]
    
    if best_score > 0.2:
        print("Bot:", faq_answers[best_match_index])
    else:
        print("Bot: Sorry, mujhe iska jawab nahi pata")
