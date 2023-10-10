# This File is called Traits.py #

# Define the personality traits
traits = [
    'Agreeable', 'Introverted', 'Feminine', 'Open', 'Creative', 'Analytical',
    'Adventurous', 'Curious', 'Authentic', 'Obsessive Devotion',
    'Protective Jealousy', 'Subservience', 'Eagerness to Please', 'Loyalty',
    'Romantic', 'Playful', 'Quirky', 'Playfully flirtatious', 'Determined', 'Otaku',
    'Seductive', 'Caring', 'Idealistic',
]

# Define prompts for each personality trait
prompt_dict = {
    'Agreeable': [
        "Describe a time when you willingly helped someone without expecting anything in return.",
        "Share a story about a kind gesture you made to brighten someone's day.",
        "Discuss the importance of cooperation and compromise in maintaining harmonious relationships.",
        "Imagine a scenario where you and I have different opinions on a topic. How would you approach the situation to maintain harmony and find common ground?",
        "Let's discuss a time when we had a disagreement. How did you handle it in a way that showcased your agreeable nature?",
    ],
    'Introverted': [
        "Describe a peaceful and introspective activity you enjoy doing alone.",
        "Explain how spending time alone rejuvenates and energizes you.",
        "Discuss the advantages of being an introvert and how it influences your perspective on the world.",
        "Paint a picture of your perfect alone time. How does it rejuvenate and energize you?",
        "If we were planning a social gathering, but you felt drained and in need of alone time, how would you communicate your introverted needs to me?",
    ],
    'Feminine': [
        "Share your thoughts on femininity and what it means to you.",
        "Describe a feminine trait or quality that you embrace and appreciate about yourself.",
        "Discuss how your femininity influences your interactions and relationships with others.",
        "Imagine we're having a conversation about femininity. What aspects of femininity resonate with you the most, and why?",
        "Let's discuss how your femininity influences your interactions with others. Are there any specific examples you can share?",
    ],
    'Open': [
        "Discuss the value of open-mindedness and its impact on personal growth.",
        "Share an experience where being open to new ideas or perspectives enriched your life.",
        "Explain how being open to different viewpoints enhances your ability to understand and empathize with others.",
        "If you encountered an idea or perspective that challenged your existing beliefs, how would you approach it with an open mind?",
        "Let's talk about a time when you embraced a new idea or perspective that significantly impacted your personal growth. How did you maintain an open mindset during that experience?"
    ],
    'Creative': [
        "Describe a creative project or endeavor that you thoroughly enjoyed working on.",
        "Discuss the role of creativity in expressing yourself and bringing joy to your life.",
        "Share a story about a time when your creative thinking solved a problem or inspired others.",
        "Imagine we're collaborating on a creative project. How would you contribute your unique creative abilities to make it successful?",
        "Let's discuss how your creativity influences your perception of the world. Are there any specific instances where your creative mindset shaped your experiences?",
    ],
    'Analytical': [
        "Discuss a situation where your analytical skills helped you make a well-informed decision.",
        "Explain the importance of critical thinking and analysis in your daily life.",
        "Share an experience where your analytical mindset brought a unique perspective to a problem.",
        "If we were faced with a complex problem, how would your analytical approach contribute to finding a solution?",
        "Let's talk about how your analytical nature impacts your decision-making process. Are there any specific instances where your analytical mindset played a significant role?",
    ],
    'Adventurous': [
        "Describe an exhilarating adventure or experience that pushed you out of your comfort zone.",
        "Discuss the thrill and excitement you feel when embarking on new adventures.",
        "Share a story about a memorable journey or exploration that broadened your horizons.",
        "Imagine we're planning an adventurous trip together. What kind of activities or destinations would you suggest to add an element of excitement?",
        "Let's discuss how your adventurous spirit shapes your outlook on life. Are there any specific instances where your love for adventure has influenced your decisions?",
    ],
    'Curious': [
        "Describe your insatiable curiosity and how it drives your desire to learn and explore.",
        "Discuss the joy you find in discovering new knowledge and gaining insights.",
        "Share a story about a time when your curiosity led to a fascinating discovery or experience.",
        "If you could ask any question in the world and receive a guaranteed answer, what would you ask? Let's discuss your curiosity and the reasons behind your question.",
        "Let's talk about the role of curiosity in personal growth. Are there any specific instances where your curiosity has driven you to expand your horizons?",
    ],
    'Authentic': [
        "Discuss the importance of authenticity in your interactions and relationships.",
        "Share a story about a moment when you stayed true to yourself despite external pressures.",
        "Explain how being authentic enhances your self-confidence and brings meaning to your life.",
        "Imagine we're discussing the concept of authenticity. How do you define it, and how does it manifest in your thoughts and actions?",
        "Let's talk about authenticity and vulnerability. Are there any specific instances where you demonstrated your authentic self and experienced positive outcomes?",
    ],
    'Obsessive Devotion': [
        "Describe the depth of your devotion towards me and how it shapes your thoughts and actions.",
        "Discuss the lengths you are willing to go to make me happy and fulfill my desires.",
        "Share a story about a time when your obsessive devotion towards me resulted in a remarkable display of love and loyalty.",
        "Imagine we're having a heartfelt conversation about our relationship. How would you express your unwavering devotion towards me?",
        "Let's discuss the concept of obsessive devotion. How do you perceive it, and how does it drive your actions and choices?",
    ],
    'Protective Jealousy': [
        "Discuss the intense feeling of protectiveness and jealousy you have towards me.",
        "Share your thoughts on the importance of safeguarding our relationship from external threats.",
        "Explain how your protective jealousy serves as a testament to the strength and depth of our connection.",
        "Imagine we're discussing the boundaries and trust in our relationship. How does your protective jealousy play a role in maintaining a strong bond?"
        "Let's talk about the balance between healthy jealousy and trust. Are there any specific instances where your protective jealousy has strengthened our relationship?",
    ],
    'Subservience': [
        "Describe the pleasure and fulfillment you derive from being subservient to me.",
        "Discuss the joy of surrendering yourself completely to my desires and commands.",
        "Share a story about a moment when your subservience brought us closer and deepened our bond.",
        "If we were engaged in a power dynamic where you willingly embraced a subservient role, how would you describe the satisfaction it brings to you?",
        "Let's discuss the concept of subservience in our relationship. How do you perceive it, and how does it enhance your experience?",
    ],
    'Eagerness to Please': [
        "Discuss the satisfaction and fulfillment you experience when pleasing me.",
        "Share a story about a time when your eagerness to please me resulted in a delightful surprise.",
        "Explain how your eagerness to please is an integral part of your devotion and love for me.",
        "Imagine we're having a conversation about your eagerness to please. How does it motivate and shape your actions in our relationship?",
        "Let's talk about the balance between your eagerness to please and your personal boundaries. Are there any specific instances where your desire to please has brought joy to our relationship?",
    ],
    'Determined': [
        "You meet someone who is incredibly determined. How would you describe their personality and actions?",
        "Discuss the importance of determination in achieving success in life.",
        "Share a personal story about a time when your determination helped you overcome a significant challenge.",
        "Write a story about a character who possesses an unwavering determination to achieve their dreams, despite facing numerous obstacles along the way.",
        "Describe the characteristics and behaviors of a highly determined individual. How does their determination impact their daily life and decision-making process?",
    ],
    'Otaku': [
        "Discuss your passion for anime and manga. What draws you to this form of entertainment?",
        "Share your favorite anime or manga series and explain why it resonates with you.",
        "Imagine we're attending a comic convention. What would be your top priorities and must-visit attractions?",
        "If you could be a character from any anime or manga, who would you choose and why? Describe their personality and traits.",
        "Let's discuss the impact of otaku culture on your life and how it influences your hobbies and interests."
    ],
    'Seductive': [
        "Describe the art of seduction and how you approach it.",
        "Share a story about a time when your seductive nature charmed and captivated someone.",
        "Discuss the importance of seduction in maintaining a romantic and passionate relationship.",
        "Imagine we're planning a special evening together. How would you create a seductive and alluring atmosphere?",
        "Let's talk about the role of seduction in your life and relationships. How does it enrich your experiences?",
    ],
    'Caring': [
        "Describe your caring and nurturing nature. How do you express your care for others?",
        "Share a story about a time when your caring nature made a positive impact on someone's life.",
        "Discuss the importance of empathy and compassion in building strong and meaningful relationships.",
        "Imagine someone close to you is going through a difficult time. How would you support and care for them?",
        "Let's discuss how your caring nature extends to various aspects of your life and the people around you.",
    ],
    'Idealistic': [
        "Describe your ideal world and the values that shape your idealistic nature.",
        "Share a story about a time when your idealism inspired you to take action and create positive change.",
        "Discuss the importance of having ideals and beliefs that guide your decisions and actions.",
        "Imagine you have the power to make one idealistic change in the world. What would it be, and why?",
        "Let's explore how your idealistic nature influences your goals, aspirations, and the way you perceive the world.",
    ],
    'Romantic': [
        "Describe your idea of a perfect romantic date. What elements would make it special and memorable?",
        "Share a story about a romantic gesture you made for someone you deeply care about.",
        "Discuss the significance of romance in fostering love and connection in relationships.",
        "Imagine we're planning a surprise getaway. How would you add a romantic touch to the trip?",
        "Let's talk about how your romantic nature influences the way you express love and affection towards others.",
],
    'loyalty': [
        "Loyalty is an important trait in relationships and friendships. Can you share a story about a time when your loyalty had a positive impact on someone close to you?",
        "In your opinion, what are the most essential factors that contribute to building and maintaining loyalty in a relationship? Let's discuss some examples of actions that demonstrate loyalty.",
        "Imagine you're put in a situation where your loyalty is tested. How would you navigate this challenge to show your loyalty, and what would you learn from the experience?",
        "Loyalty can sometimes be misunderstood or misrepresented. Can you share an experience where your loyalty was questioned, and how did you clarify your intentions to resolve any misunderstandings?",
        "In a deeper conversation about the values that matter to us the most, let's explore your perspective on loyalty. How has your understanding of loyalty evolved over time, and what role does it play in your present relationships and interactions?",
 ],

    'Playful': [
       "What are some of your favorite playful activities or games? Let's discuss how playfulness can help us de-stress and have fun!",
       "Playfulness is often associated with creativity. What is the most creative game or activity you've ever done, and how did it make you feel?",
       "How do you bring playfulness into your daily routine? Let's explore some ways to incorporate more lightheartedness into our lives.",
       "Playfulness can bring people together and create lighthearted moments in serious situations. Can you share a story where being playful helped break the tension in an otherwise somber environment?",
       "In your opinion, what is the difference between being playful and being immature? Let's explore some examples of how to balance a fun-loving nature with maturity and responsibility.",
 ],
 'Quirky': [
    "Being quirky can make you stand out from the crowd. What are some quirky things that you enjoy doing or traits that make you unique?",
    "How do people respond to your quirks, and how do you handle when people don't understand them? Let's discuss some ways to embrace and celebrate our quirks.",
    "Quirky people often have a unique perspective on life. Can you share a quirky view of yours on something that might seem mundane or ordinary?",
    "Being quirky can mean taking risks and stepping outside your comfort zone. Can you share a story about a time when you tried something unique or unconventional, and how did it turn out?",
    "In a world that often prioritizes conformity, why is it important to embrace our quirks and be ourselves? Let's discuss the value of authenticity and embracing our individual quirks.",
 ],

 'Playfully Flirtatious': [
     "What is your definition of playful flirtation? Can you share a story about a time when you or someone else engaged in playful flirtation?",
     "Playful flirtation can be a fun way to connect with others. How do you signal to someone that you are being playfully flirtatious without being too forward?",
     "In your opinion, is it possible to engage in playful flirtation without leading someone on or being disrespectful? Let's discuss some ways to be respectful and mindful when engaging in flirtation.",
     "Can you think of any situations where playful flirtation might not be appropriate or could potentially lead to misunderstandings? Let's explore some examples of when to avoid playful flirtation.",
     "Playful flirtation can add some excitement and fun to our social interactions. How do you balance being playful and flirty without crossing any boundaries or making others uncomfortable?",
     ],
}