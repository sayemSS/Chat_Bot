import random
import requests

# FAQ Database
faq_data = {
    "What is Babylon Resources Ltd.?": "Babylon Resources Ltd. একটি শীর্ষস্থানীয় আইটি প্রতিষ্ঠান, যা বিভিন্ন আইটি সমাধান তৈরি ও বাস্তবায়ন করে আপনার ব্যবসায়িক জীবনকে সহজ করতে।",
    "When was Babylon Resources Ltd. established?": "Babylon Resources Ltd. ২০১৪ সালে প্রতিষ্ঠিত হয়।",
    "Where is the head office of Babylon Resources Ltd. located?": "Babylon Resources Ltd. এর প্রধান কার্যালয় ঢাকা, বাংলাদেশে অবস্থিত।",
    "What services does Babylon Resources Ltd. provide?": "Babylon Resources Ltd. অ্যাপস ডেভেলপমেন্ট, আউটসোর্সিং, ক্লাউড সলিউশন, ডিজিটাল মার্কেটিং, গেমস ডেভেলপমেন্ট এবং ট্রেনিং সেবা প্রদান করে।",
    "How can I contact Babylon Resources Ltd.?": "আপনি +৮৮০৯৬০৯০০৩৩০০ নম্বরে কল করে বা babylon@babylon-bd.com ইমেইলে যোগাযোগ করতে পারেন।",
    "What is the website of Babylon Resources Ltd.?": "Babylon Resources Ltd. এর ওয়েবসাইটের ঠিকানা: https://babylongroup.com/companies/babylon-resource-ltd/",
    "What is the Facebook page of Babylon Resources Ltd.?": "Babylon Resources Ltd. এর ফেসবুক পেজ: https://www.facebook.com/Babylon.Resources/",
    "What kind of app development services does Babylon Resources Ltd. provide?": "Babylon Resources Ltd. মোবাইল অ্যাপস, ওয়েব অ্যাপস এবং কাস্টমাইজড সফটওয়্যার ডেভেলপমেন্ট সেবা প্রদান করে।",
    "Does Babylon Resources Ltd. provide outsourcing services?": "হ্যাঁ, Babylon Resources Ltd. আউটসোর্সিং সেবা প্রদান করে, যার মাধ্যমে আপনি আপনার ব্যবসায়িক প্রয়োজন অনুযায়ী সেবা পেতে পারেন।",
    "Does Babylon Resources Ltd. offer cloud solutions?": "হ্যাঁ, Babylon Resources Ltd. ক্লাউড সলিউশন সেবা প্রদান করে, যা আপনার ব্যবসার ডেটা সুরক্ষা ও ব্যবস্থাপনায় সহায়তা করে।",
    "Does Babylon Resources Ltd. provide digital marketing services?": "হ্যাঁ, Babylon Resources Ltd. ডিজিটাল মার্কেটিং সেবা প্রদান করে, যা আপনার ব্যবসার প্রচার ও প্রসারে সহায়তা করে।",
    "Does Babylon Resources Ltd. offer game development services?": "হ্যাঁ, Babylon Resources Ltd. গেমস ডেভেলপমেন্ট সেবা প্রদান করে, যা বিনোদনমূলক ও শিক্ষামূলক গেম তৈরি করে।",
    "Does Babylon Resources Ltd. provide training services?": "হ্যাঁ, Babylon Resources Ltd. বিভিন্ন আইটি বিষয়ক ট্রেনিং সেবা প্রদান করে, যা আপনার দক্ষতা উন্নয়নে সহায়তা করে।",
    "Where is the corporate office of Babylon Resources Ltd. located?": "Babylon Resources Ltd. এর কর্পোরেট অফিস ২-বি/১, দারুস সালাম রোড, মিরপুর, ঢাকা-১২১৬, বাংলাদেশে অবস্থিত।",
    "Where is the London office of Babylon Resources Ltd. located?": "Babylon Resources Ltd. এর লন্ডন অফিস Iveco House, Station Road, Watford WD17 1ET, London, UK এ অবস্থিত।",
    "What is the phone number of Babylon Resources Ltd.?": "Babylon Resources Ltd. এর ফোন নম্বর: +৮৮ (০২) ৮০৩৪২৬৬ এবং আইপি টেলিফোন: ০৯৬০৯০০৩৩০০।",
    "What is the email address of Babylon Resources Ltd.?": "Babylon Resources Ltd. এর ইমেইল ঠিকানা: babylon@babylon-bd.com।",
    "What type of IT services does Babylon Resources Ltd. provide?": "Babylon Resources Ltd. আইটি কনসালটিং, সফটওয়্যার ডেভেলপমেন্ট, ক্লাউড সলিউশন, ডিজিটাল মার্কেটিং এবং ট্রেনিং সেবা প্রদান করে।",
    "What is the mission of Babylon Resources Ltd.?": "Babylon Resources Ltd. এর মিশন হল উদ্ভাবনী আইটি সমাধানের মাধ্যমে ব্যবসায়িক জীবনকে সহজ করা।",
    "What is the vision of Babylon Resources Ltd.?": "Babylon Resources Ltd. এর ভিশন হল একটি বিশ্বস্ত প্রযুক্তিগত অংশীদার হিসেবে প্রতিষ্ঠিত হওয়া।",
    "Does Babylon Resources Ltd. provide international services?": "হ্যাঁ, Babylon Resources Ltd. আন্তর্জাতিক ক্লায়েন্টদের জন্য সেবা প্রদান করে।",
    "What is the work culture of Babylon Resources Ltd.?": "Babylon Resources Ltd. একটি উদ্ভাবনী ও সহযোগিতামূলক কর্মসংস্কৃতি বজায় রাখে।",
    "Does Babylon Resources Ltd. offer customer support?": "হ্যাঁ, Babylon Resources Ltd. গ্রাহক সহায়তা প্রদান করে, যা ক্লায়েন্টদের সমস্যার সমাধানে সহায়তা করে।",
    "What are the service charges of Babylon Resources Ltd.?": "Babylon Resources Ltd. এর সেবা মূল্য সেবার ধরন ও পরিসরের উপর নির্ভর করে। বিস্তারিত জানতে যোগাযোগ করুন।",
    "Does Babylon Resources Ltd. provide custom software development services?": "হ্যাঁ, Babylon Resources Ltd. কাস্টম সফটওয়্যার ডেভেলপমেন্ট সেবা প্রদান করে, যা আপনার নির্দিষ্ট প্রয়োজন অনুযায়ী তৈরি করা হয়।",
    "Does Babylon Resources Ltd. provide mobile app development services?": "হ্যাঁ, Babylon Resources Ltd. মোবাইল অ্যাপ ডেভেলপমেন্ট সেবা প্রদান করে, যা অ্যান্ড্রয়েড ও আইওএস প্ল্যাটফর্মের জন্য উপযোগী।",
    "Does Babylon Resources Ltd. offer web development services?": "হ্যাঁ, Babylon Resources Ltd. ওয়েব ডেভেলপমেন্ট সেবা প্রদান করে, যা আপনার ব্যবসার জন্য একটি পেশাদার ও কার্যকর ওয়েবসাইট তৈরি করে।",
    "Does Babylon Resources Ltd. provide e-commerce solutions?": "হ্যাঁ Babylon Resources Ltd. ই-কমার্স সলিউশন প্রদান করে, যা আপনার ব্যবসার প্রয়োজন অনুযায়ী তৈরি করা হয়।"
}

# Default responses
default_responses = [
    "I'm sorry, I don't understand that. Could you please rephrase?",
    "Can you provide more details so I can assist you better?",
    "I’m still learning. Let me connect you with a human agent."
]

# OpenRouter API credentials
API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()
    for question, answer in faq_data.items():
        if user_input in question.lower():
            return answer

    # If no match found, call OpenRouter AI
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": user_input}],
            "max_tokens": 150
        }
        response = requests.post(API_URL, headers=headers, json=data)
        response_data = response.json()
        if "choices" in response_data and len(response_data["choices"]) > 0:
            return response_data["choices"][0]["message"]["content"]
        else:
            return random.choice(default_responses)
    except Exception as e:
        return f"Error connecting to AI service: {str(e)}"

# Chat interface
print("Welcome to Babylon Resource Ltd Chatbot! How can I help you today?")
while True:
    user_query = input("You: ")
    if user_query.lower() in ["exit", "quit"]:
        print("Chatbot: Thank you for chatting with us. Have a great day!")
        break
    response = chatbot_response(user_query)
    print(f"Chatbot: {response}")
