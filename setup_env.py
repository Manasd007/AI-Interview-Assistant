#!/usr/bin/env python3
import os
import sys

def create_env_file():
    env_content = """# Gemini API Configuration
GEMINI_API_KEY=AIzaSyCZ9McwZL_PXHBsImKEAeOlT8ROjZpZZrM

# Instructions:
# 1. Replace the API key above with your actual Gemini API key if needed
# 2. Get your API key from: https://makersuite.google.com/app/apikey
"""
    
    try:
        with open('.env', 'w', encoding='utf-8') as f:
            f.write(env_content)
        print("✅ Created .env file successfully!")
        print("📝 Please edit the .env file and add your Gemini API key")
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def recreate_env_file():
    try:
        if os.path.exists('.env'):
            os.remove('.env')
            print("🗑️ Deleted corrupted .env file")
        
        return create_env_file()
    except Exception as e:
        print(f"❌ Error recreating .env file: {e}")
        return False

def check_api_key():
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key and api_key != "your_google_ai_key_here":
        print("✅ GEMINI_API_KEY is set")
        return True
    else:
        print("❌ GEMINI_API_KEY is not set or is using placeholder value")
        return False

def main():
    print("🤖 TalentScout AI - Environment Setup")
    print("=" * 40)
    
    if not os.path.exists('.env'):
        print("📁 .env file not found. Creating one...")
        if create_env_file():
            print("\n📋 Next steps:")
            print("1. Edit the .env file")
            print("2. Replace the API key with your actual key if needed")
            print("3. Get your API key from: https://makersuite.google.com/app/apikey")
            print("4. Run: streamlit run app.py")
        else:
            print("❌ Failed to create .env file")
            return
    else:
        print("📁 .env file found")
        
        try:
            from dotenv import load_dotenv
            load_dotenv()
            print("✅ .env file loaded successfully")
        except Exception as e:
            print(f"❌ Error loading .env file: {e}")
            print("💡 Recreating .env file with proper UTF-8 encoding...")
            if recreate_env_file():
                print("✅ .env file recreated successfully!")
                try:
                    from dotenv import load_dotenv
                    load_dotenv()
                    print("✅ New .env file loaded successfully")
                except Exception as e2:
                    print(f"❌ Still having issues: {e2}")
                    return
            else:
                print("❌ Failed to recreate .env file")
                return
    
    if check_api_key():
        print("\n🚀 Ready to run! Execute: streamlit run app.py")
    else:
        print("\n🔧 Setup required:")
        print("1. Get your Gemini API key from: https://makersuite.google.com/app/apikey")
        print("2. Add it to your .env file")
        print("3. Or set it as environment variable: set GEMINI_API_KEY=your_key_here")

if __name__ == "__main__":
    main() 