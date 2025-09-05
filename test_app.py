#!/usr/bin/env python3
"""
Test script for the AI-Powered Patient Information System
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all required modules can be imported"""
    try:
        import gradio as gr
        from datetime import datetime, date
        import json
        from dotenv import load_dotenv
        from openai import OpenAI
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_env_setup():
    """Test if .env file exists and has API key"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key and api_key != "your_openai_api_key_here":
            print("✅ OpenAI API key found in .env file")
            return True
        else:
            print("⚠️  OpenAI API key not found or not set in .env file")
            print("   Please create a .env file with your OpenAI API key")
            return False
    except Exception as e:
        print(f"❌ Environment setup error: {e}")
        return False

def test_app_structure():
    """Test if the app can be loaded"""
    try:
        # Import the app module
        import app
        print("✅ App module loads successfully")
        return True
    except Exception as e:
        print(f"❌ App loading error: {e}")
        return False

def test_specific_advice_function():
    """Test if the specific advice function exists and is callable"""
    try:
        import app
        # Check if the function exists
        if hasattr(app, 'get_specific_advice'):
            print("✅ Specific advice function exists")
            return True
        else:
            print("❌ Specific advice function not found")
            return False
    except Exception as e:
        print(f"❌ Error testing specific advice function: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing AI-Powered Patient Information System...")
    print("-" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Environment Setup Test", test_env_setup),
        ("App Structure Test", test_app_structure),
        ("Specific Advice Function Test", test_specific_advice_function),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name}...")
        if test_func():
            passed += 1
        else:
            print(f"❌ {test_name} failed")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The AI-powered app is ready to run.")
        print("\nTo start the app, run: python app.py")
        print("Make sure your .env file contains a valid OpenAI API key!")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        if not test_env_setup():
            print("\n💡 To fix the API key issue:")
            print("   1. Create a .env file in the project directory")
            print("   2. Add: OPENAI_API_KEY=your_actual_api_key_here")
            print("   3. Get your API key from: https://platform.openai.com/api-keys")

if __name__ == "__main__":
    main()
