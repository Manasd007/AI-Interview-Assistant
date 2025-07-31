#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import google.generativeai as genai

def test_gemini_api():
    print("🤖 Testing Gemini API Connection...")
    print("=" * 40)
    
    try:
        load_dotenv()
        print("✅ .env file loaded successfully")
    except Exception as e:
        print(f"❌ Error loading .env file: {e}")
        return False
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY not found in environment variables")
        return False
    
    if api_key == "your_google_ai_key_here":
        print("❌ API key is still using placeholder value")
        return False
    
    print(f"✅ API key found: {api_key[:10]}...")
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        test_prompt = "Generate 1 simple technical question about Python programming."
        print("🔄 Testing API with simple prompt...")
        
        response = model.generate_content(test_prompt)
        
        if response.text:
            print("✅ API test successful!")
            print(f"📝 Response: {response.text.strip()}")
            return True
        else:
            print("❌ API returned empty response")
            return False
            
    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False

def main():
    print("🧪 TalentScout AI - API Test")
    print("=" * 40)
    
    if test_gemini_api():
        print("\n🎉 API is working correctly!")
        print("Your application should work fine now.")
    else:
        print("\n🔧 API issues detected. Please check:")
        print("1. API key is valid and active")
        print("2. You have sufficient quota")
        print("3. Internet connection is stable")
        print("4. API key is properly set in .env file")

if __name__ == "__main__":
    main() 