import streamlit as st
import random

# List of quotes with descriptions
quotes = [
    {
        "quote": "You are unstoppable.",
        "description": "Believe in yourself and your abilities. Every day is a new chance to move forward."
    },
    {
        "quote": "Keep pushing forward.",
        "description": "Challenges are opportunities in disguise. Embrace them and grow stronger."
    },
    {
        "quote": "Stay positive, work hard, make it happen.",
        "description": "A positive mindset fuels hard work and leads to success."
    },
    {
        "quote": "Your limitation—it's only your imagination.",
        "description": "Believe in yourself and break your limits."
    },
    {
        "quote": "Push yourself, because no one else is going to do it for you.",
        "description": "Self-motivation is key to success."
    },
    {
        "quote": "Sometimes later becomes never. Do it now.",
        "description": "Don't procrastinate—start today."
    },
    {
        "quote": "Great things never come from comfort zones.",
        "description": "Step out and grow."
    },
    {
        "quote": "Dream it. Wish it. Do it.",
        "description": "Turn dreams into reality."
    },
    {
        "quote": "Success doesnt just find you. You have to go out and get it.",
        "description": "Be proactive and chase your goals."
    },
    {
        "quote": "The harder you work for something, the greater youll feel when you achieve it.",
        "description": "Effort leads to satisfaction."
    },
    {
        "quote": "Dream bigger. Do bigger.",
        "description": "Think big, act bigger."
    },
    {
        "quote": "Don’t stop when you’re tired. Stop when you’re done.",
        "description": "Push through fatigue to reach your goal."
    },
    {
        "quote": "Wake up with determination. Go to bed with satisfaction.",
        "description": "Daily commitment fuels success."
    },
    {
        "quote": "Do something today that your future self will thank you for.",
        "description": "Invest in yourself daily."
    },
    {
        "quote": "Little things make big days.",
        "description": "Small wins add up."
    },
    {
        "quote": "It’s going to be hard, but hard does not mean impossible.",
        "description": "Stay resilient."
    },
    {
        "quote": "Don’t wait for opportunity. Create it.",
        "description": "Be the architect of your destiny."
    },
    {
        "quote": "Sometimes we’re tested not to show our weaknesses, but to discover our strengths.",
        "description": "Challenges reveal who we are."
    },
    {
        "quote": "The key to success is to focus on goals, not obstacles.",
        "description": "Keep your eyes on the prize."
    },
    {
        "quote": "Believe you can and you’re halfway there.",
        "description": "Confidence fuels progress."
    },
    {
        "quote": "Your only limit is your mind.",
        "description": "Change your thinking, change your life."
    },
    {
        "quote": "Don’t watch the clock; do what it does. Keep going.",
        "description": "Keep moving forward."
    },
    {
        "quote": "The future depends on what you do today.",
        "description": "Make today count."
    },
    {
        "quote": "Success is not for the lazy.",
        "description": "Hard work pays off."
    },
    {
        "quote": "Push yourself, because no one else is going to do it for you.",
        "description": "Self-motivation is essential."
    },
    {
        "quote": "Dream it. Believe it. Build it.",
        "description": "Manifest your vision."
    },
    {
        "quote": "The only place where success comes before work is in the dictionary.",
        "description": "Effort precedes success."
    },
    {
        "quote": "Don’t limit your challenges. Challenge your limits.",
        "description": "Growth happens outside comfort zones."
    },
    {
        "quote": "It always seems impossible until it’s done.",
        "description": "Persevere and succeed."
    },
    {
        "quote": "Hard work beats talent when talent doesn’t work hard.",
        "description": "Effort surpasses natural ability."
    },
    {
        "quote": "Success is the sum of small efforts repeated day in and day out.",
        "description": "Consistency is key."
    },
    {
        "quote": "Make your fear of losing your greatest motivator.",
        "description": "Let fear fuel your action."
    },
    {
        "quote": "You don’t have to be great to start, but you have to start to be great.",
        "description": "Begin to become better."
    },
    {
        "quote": "Every sunrise is a new opportunity.",
        "description": "Embrace each day with hope and determination."
    },
    {
        "quote": "Progress is better than perfection.",
        "description": "Small steps forward are still steps in the right direction."
    },
    {
        "quote": "Your journey is your own masterpiece.",
        "description": "Paint it with courage, effort, and joy."
    },
    {
        "quote": "Let your dreams be bigger than your fears.",
        "description": "Focus on what you want, not what you fear."
    },
    {
        "quote": "You are the author of your own story.",
        "description": "Write a chapter today that makes you proud tomorrow."
    },
    {
        "quote": "Strength grows in the moments you think you can’t go on but you keep going anyway.",
        "description": "Resilience is built one challenge at a time."
    },
    {
        "quote": "Your attitude determines your direction.",
        "description": "Stay positive and keep moving forward."
    },
    {
        "quote": "Success starts with self-belief.",
        "description": "Trust in your abilities and take the first step."
    },
    {
        "quote": "Mistakes are proof that you are trying.",
        "description": "Learn from them and keep improving."
    },
    {
        "quote": "The best way to predict the future is to create it.",
        "description": "Take action today for a better tomorrow."
    },
    {
        "quote": "Rise above the storm and you will find the sunshine.",
        "description": "Challenges are temporary; your strength is lasting."
    },
    {
        "quote": "Be your own biggest supporter.",
        "description": "Encourage yourself when no one else does."
    },
    {
        "quote": "Growth begins at the end of your comfort zone.",
        "description": "Dare to try something new."
    },
    {
        "quote": "Your potential is endless.",
        "description": "There are no limits to what you can achieve."
    },
    {
        "quote": "Focus on the solution, not the problem.",
        "description": "A positive mindset finds a way forward."
    },
    {
        "quote": "Celebrate every small victory.",
        "description": "Each win brings you closer to your goal."
    },
    {
        "quote": "You are stronger than your excuses.",
        "description": "Push past them and see what you can do."
    },
    {
        "quote": "Let your passion be your motivation.",
        "description": "Do what you love and success will follow."
    },
    {
        "quote": "Keep your vision clear and your heart strong.",
        "description": "Stay true to your purpose."
    },
    {
        "quote": "Turn obstacles into opportunities.",
        "description": "Every challenge is a chance to grow."
    },
    {
        "quote": "Your energy introduces you before you even speak.",
        "description": "Radiate positivity wherever you go."
    },
    {
        "quote": "The only way to fail is to give up.",
        "description": "Keep trying and you will succeed."
    },
    {
        "quote": "Be patient with yourself. Growth takes time.",
        "description": "Trust the process and keep moving forward."
    },
    {
        "quote": "Your dreams are valid and achievable.",
        "description": "Believe in them and work towards them every day."
    },
    {
        "quote": "Let today be the start of something new.",
        "description": "Take the first step and the rest will follow."
    },
]

# Title and description
st.title("Motivational Quote of the Day")
st.write("Click the button below to get your daily boost!")

# Button to get a random quote
if st.button("Get Quote"):
    selected = random.choice(quotes)
    st.subheader(selected["quote"])
    st.write(selected["description"])

# Footer or additional info
st.write("---")
st.write("Made with ❤️ by Pawan Singh")
