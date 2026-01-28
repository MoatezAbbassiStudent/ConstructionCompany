from flask import render_template, request, jsonify, Blueprint
from rapidfuzz import fuzz, process
import random
import re

main_bp = Blueprint('main', __name__)

# ============================================
# ConstructionCompany LOCAL CHATBOT (No API - Runs Locally)
# ============================================
print("✓ ConstructionCompany Local Chatbot Loaded (Lightweight - No External APIs)")

# Company Data
COMPANY = {
    "name": "ConstructionCompany",
    "phone": "+1 (555) 123-4567",
    "email": "info@ConstructionCompany.com",
    "address": "123 Construction Ave, City, State 12345",
    "founded": 2010,
    "owner": "John Mitchell",
    "projects": "100+",
    "satisfaction": "98%",
    "team": "5",
    "warranty": "5 years",
    "hours": "Monday-Friday 8AM-6PM, Saturday 9AM-2PM",
    "area": "Greater Metro Area and surrounding counties (50 mile radius)",
}

# ============================================
# INTENT PATTERNS - What users might ask about
# ============================================
INTENTS = {
    "greeting": {
        "patterns": ["hi", "hey", "hello", "howdy", "sup", "yo", "hiya", "good morning", "good afternoon", "good evening", "whats up", "what's up"],
        "responses": [
            f"Hey there! 👋 Welcome to {COMPANY['name']}! How can I help you today?",
            f"Hi! Thanks for reaching out to {COMPANY['name']}. What can I do for you?",
            f"Hello! Great to hear from you. Looking for tile work, concrete, or something else?",
        ]
    },
    "services": {
        "patterns": ["services", "what do you do", "what do you offer", "what can you do", "help with", "what services", "offerings", "capabilities", "specialties", "what you do"],
        "responses": [
            f"We specialize in **tile installation** and **concrete work**! 🏗️ This includes bathrooms, kitchens, driveways, patios, and more. What interests you?",
            f"{COMPANY['name']} offers: tile installation (floors, walls, backsplashes), concrete work (driveways, patios, foundations), and full renovations. Want details on any of these?",
            "Our main services: tile work, concrete, renovations, and specialty finishes. Which one are you curious about?",
        ]
    },
    "tile": {
        "patterns": ["tile", "tiles", "tiling", "backsplash", "ceramic", "porcelain", "mosaic", "bathroom tile", "kitchen tile", "floor tile"],
        "responses": [
            "Our tile services include bathrooms, kitchens, floors, walls, and backsplashes. We work with ceramic, porcelain, natural stone, and mosaic. Typically takes 3-7 days depending on the area. Pricing runs $8-15/sq ft. Want a free quote?",
            f"Tile installation is one of our specialties! We handle everything from bathroom remodels to kitchen backsplashes. Call us at {COMPANY['phone']} for a free estimate!",
            "We do all types of tile work - bathrooms, kitchens, entryways, you name it. Ceramic, porcelain, marble, slate - we've got you covered. What space are you looking to transform?",
        ]
    },
    "concrete": {
        "patterns": ["concrete", "driveway", "patio", "foundation", "sidewalk", "stamped", "cement", "slab"],
        "responses": [
            "Our concrete services include driveways, patios, foundations, sidewalks, and decorative stamped concrete. Pricing is around $6-12/sq ft. Timeline is 2-10 days including curing. Need a quote?",
            f"We're concrete experts! Driveways, patios, foundations - we do it all. Plus decorative stamped options for that extra wow factor. Call {COMPANY['phone']} to discuss your project!",
            "Concrete work is our bread and butter - driveways, patios, walkways, foundations. We also do beautiful stamped and decorative finishes. What project do you have in mind?",
        ]
    },
    "pricing": {
        "patterns": ["price", "cost", "how much", "pricing", "rates", "expensive", "cheap", "afford", "budget", "estimate", "quote"],
        "responses": [
            f"General pricing: Tile $8-15/sq ft, Concrete $6-12/sq ft, Sealing $2-5/sq ft. For an exact quote, call us at {COMPANY['phone']} or email {COMPANY['email']} - estimates are FREE!",
            f"Pricing varies by project, but ballpark: tile work $8-15/sq ft, concrete $6-12/sq ft. We offer free quotes! Reach out at {COMPANY['phone']}.",
            f"Every project is unique, so I'd recommend getting a free estimate. Contact us at {COMPANY['phone']} or {COMPANY['email']} and we'll give you an accurate quote!",
        ]
    },
    "contact": {
        "patterns": ["contact", "phone", "call", "email", "reach", "get in touch", "talk to someone", "speak", "number", "address", "location", "where are you"],
        "responses": [
            f"📞 Phone: {COMPANY['phone']}\n📧 Email: {COMPANY['email']}\n📍 Address: {COMPANY['address']}\n\nWe'd love to hear from you!",
            f"Best ways to reach us:\n• Call: {COMPANY['phone']}\n• Email: {COMPANY['email']}\n• Visit: {COMPANY['address']}",
            f"Give us a call at {COMPANY['phone']} or shoot an email to {COMPANY['email']}. We're here to help!",
        ]
    },
    "hours": {
        "patterns": ["hours", "open", "when", "schedule", "available", "time", "closed"],
        "responses": [
            f"We're open {COMPANY['hours']}. Feel free to call or stop by!",
            f"Business hours: {COMPANY['hours']}. Outside those times, leave a message and we'll get back to you ASAP!",
            f"You can reach us {COMPANY['hours']}. Need to schedule something?",
        ]
    },
    "owner": {
        "patterns": ["owner", "who owns", "founded", "founder", "started", "boss", "ceo", "president"],
        "responses": [
            f"{COMPANY['name']} was founded in {COMPANY['founded']} by {COMPANY['owner']}. Over {2026 - COMPANY['founded']} years of experience!",
            f"The company was started by {COMPANY['owner']} back in {COMPANY['founded']}. We've completed {COMPANY['projects']} projects since then!",
            f"{COMPANY['owner']} founded {COMPANY['name']} in {COMPANY['founded']} with a vision for quality craftsmanship. Still going strong!",
        ]
    },
    "about": {
        "patterns": ["about", "tell me about", "company", "who are you", "your company", "ConstructionCompany", "about you", "info", "information"],
        "responses": [
            f"{COMPANY['name']} has been delivering quality tile and concrete work since {COMPANY['founded']}. We've completed {COMPANY['projects']} projects with {COMPANY['satisfaction']} customer satisfaction. {COMPANY['team']} skilled professionals, {COMPANY['warranty']} warranty on all work!",
            f"We're {COMPANY['name']} - a team of {COMPANY['team']} construction pros specializing in tile and concrete. Founded {COMPANY['founded']}, {COMPANY['projects']} projects completed, {COMPANY['satisfaction']} satisfaction rate!",
            f"Founded in {COMPANY['founded']} by {COMPANY['owner']}, {COMPANY['name']} has grown to {COMPANY['team']} team members. We take pride in our {COMPANY['satisfaction']} satisfaction rate and {COMPANY['warranty']} warranty!",
        ]
    },
    "warranty": {
        "patterns": ["warranty", "guarantee", "guaranteed", "insurance", "protection", "covered"],
        "responses": [
            f"All our work comes with a {COMPANY['warranty']} warranty. We stand behind everything we do!",
            f"We offer a solid {COMPANY['warranty']} warranty on all projects. Quality you can count on!",
            f"{COMPANY['warranty']} warranty included with every job. If something's not right, we'll make it right!",
        ]
    },
    "area": {
        "patterns": ["area", "serve", "service area", "where do you work", "location", "travel", "come to", "regions"],
        "responses": [
            f"We serve the {COMPANY['area']}. Not sure if you're in range? Give us a call at {COMPANY['phone']}!",
            f"Our service area covers {COMPANY['area']}. If you're nearby, we can help!",
            f"We work throughout the {COMPANY['area']}. Just reach out and we'll confirm we can get to you!",
        ]
    },
    "renovation": {
        "patterns": ["renovation", "remodel", "renovate", "redo", "upgrade", "makeover", "transform"],
        "responses": [
            "We do full bathroom and kitchen renovations! From gutting to finishing touches. Want to discuss your vision?",
            f"Renovations are our specialty - bathrooms, kitchens, full room makeovers. Call {COMPANY['phone']} for a free consultation!",
            "Looking to renovate? We handle everything from design to completion. What space are you thinking about?",
        ]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thx", "appreciate", "grateful", "awesome", "great", "perfect", "helpful"],
        "responses": [
            "You're welcome! Let me know if you need anything else. 😊",
            "Happy to help! Reach out anytime you have more questions.",
            "Glad I could help! Don't hesitate to contact us when you're ready to start your project!",
        ]
    },
    "bye": {
        "patterns": ["bye", "goodbye", "see you", "later", "take care", "cya", "gotta go"],
        "responses": [
            f"Take care! Feel free to reach out anytime at {COMPANY['phone']}. Have a great day! 👋",
            "Goodbye! Thanks for chatting with ConstructionCompany. We're here when you need us!",
            "See you later! Don't forget - free quotes available anytime. 😊",
        ]
    },
    "yes": {
        "patterns": ["yes", "yea", "yeah", "yep", "sure", "okay", "ok", "absolutely", "definitely", "of course"],
        "responses": [
            "Great! What would you like to know more about? Services, pricing, or scheduling?",
            f"Awesome! Feel free to ask me anything, or call {COMPANY['phone']} to speak with our team directly.",
            "Perfect! I'm here to help. What's on your mind?",
        ]
    },
    "no": {
        "patterns": ["no", "nope", "nah", "not really", "nevermind", "nothing"],
        "responses": [
            "No problem! Let me know if you change your mind or have other questions.",
            "That's okay! I'm here if you need anything else.",
            f"All good! Feel free to reach out anytime at {COMPANY['phone']}.",
        ]
    },
    "help": {
        "patterns": ["help", "assist", "support", "need help", "confused", "lost", "don't understand"],
        "responses": [
            "I'm here to help! You can ask me about our services (tile, concrete, renovations), pricing, contact info, business hours, or our company. What do you need?",
            f"No worries! I can tell you about what we do, give pricing info, or connect you with our team at {COMPANY['phone']}. What works best?",
            "Happy to assist! Try asking about: services, prices, contact info, hours, or our company. Or just tell me what you're looking for!",
        ]
    },
}

# Fallback responses when nothing matches
FALLBACK_RESPONSES = [
    f"Hmm, I'm not quite sure about that. Try asking about our services, pricing, or contact info. Or call us at {COMPANY['phone']} for help!",
    f"I didn't catch that - I'm still learning! You can ask about tile work, concrete, pricing, or contact us at {COMPANY['phone']}.",
    f"Good question! I might need more context. Feel free to call {COMPANY['phone']} to speak with our team directly.",
    f"I'm not sure I understood. Try asking about what we do, how much things cost, or how to reach us!",
]

def clean_text(text):
    """Clean and normalize text for matching"""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)     # Normalize whitespace
    return text

def get_intent(message):
    """Detect intent using fuzzy matching"""
    cleaned = clean_text(message)
    
    # If message is too short or just punctuation, treat as greeting
    if len(cleaned) < 2:
        return "greeting", 100
    
    best_intent = None
    best_score = 0
    
    for intent_name, intent_data in INTENTS.items():
        for pattern in intent_data["patterns"]:
            # Check if pattern is contained in message
            if pattern in cleaned:
                score = 95
                if score > best_score:
                    best_score = score
                    best_intent = intent_name
            
            # Fuzzy match for close matches
            ratio = fuzz.partial_ratio(pattern, cleaned)
            if ratio > best_score and ratio > 70:
                best_score = ratio
                best_intent = intent_name
            
            # Token sort ratio for word order variations
            token_ratio = fuzz.token_sort_ratio(pattern, cleaned)
            if token_ratio > best_score and token_ratio > 75:
                best_score = token_ratio
                best_intent = intent_name
    
    return best_intent, best_score

def get_response(message):
    """Get chatbot response for a message"""
    intent, confidence = get_intent(message)
    
    if intent and confidence >= 60:
        responses = INTENTS[intent]["responses"]
        return random.choice(responses)
    else:
        return random.choice(FALLBACK_RESPONSES)

# ============================================
# FLASK ROUTES
# ============================================
@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'reply': 'Hey! What would you like to know?'})
    
    reply = get_response(user_message)
    return jsonify({'reply': reply})
