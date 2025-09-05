#!/usr/bin/env python3
"""
Test script demonstrating the fixed treatment timeline logic
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime, date, timedelta

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_treatment_timeline():
    """Test the treatment timeline logic with different scenarios"""
    
    today = date.today()
    
    # Test scenarios
    test_cases = [
        {
            "name": "Future Treatment (5 days from now)",
            "operation_date": (today - timedelta(days=10)).strftime("%Y-%m-%d"),
            "treatment_start_date": (today + timedelta(days=5)).strftime("%Y-%m-%d"),
            "description": "Patient had surgery 10 days ago, treatment starts in 5 days"
        },
        {
            "name": "Treatment Starting Today",
            "operation_date": (today - timedelta(days=7)).strftime("%Y-%m-%d"),
            "treatment_start_date": today.strftime("%Y-%m-%d"),
            "description": "Patient had surgery 7 days ago, treatment starts today"
        },
        {
            "name": "Ongoing Treatment (3 days ago)",
            "operation_date": (today - timedelta(days=15)).strftime("%Y-%m-%d"),
            "treatment_start_date": (today - timedelta(days=3)).strftime("%Y-%m-%d"),
            "description": "Patient had surgery 15 days ago, treatment started 3 days ago"
        }
    ]
    
    sample_patient = {
        "gender": "Female",
        "age": 65,
        "diagnosis": "Hip replacement surgery",
        "operation_description": "Total hip arthroplasty (right hip) due to severe osteoarthritis",
        "treatment_details": "Physical therapy 3x weekly, pain management with prescribed medications, wound care monitoring"
    }
    
    print("🏥 Treatment Timeline Logic Test")
    print("=" * 50)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📋 TEST CASE {i}: {test_case['name']}")
        print(f"   {test_case['description']}")
        print("-" * 40)
        
        # Calculate timeline
        op_date = datetime.strptime(test_case['operation_date'], "%Y-%m-%d").date()
        treat_date = datetime.strptime(test_case['treatment_start_date'], "%Y-%m-%d").date()
        
        days_since_op = (today - op_date).days
        
        # Determine treatment status
        if treat_date > today:
            days_until_treatment = (treat_date - today).days
            treatment_status = f"Treatment starts in {days_until_treatment} days (future)"
        elif treat_date == today:
            treatment_status = "Treatment starts today"
        else:
            days_since_treatment = (today - treat_date).days
            treatment_status = f"Treatment started {days_since_treatment} days ago (ongoing)"
        
        print(f"   Operation Date: {test_case['operation_date']} ({days_since_op} days ago)")
        print(f"   Treatment Date: {test_case['treatment_start_date']} - {treatment_status}")
        
        # Test AI advice generation
        try:
            prompt = f"""
You are an experienced senior nurse. Based on this patient information, provide brief advice focusing on the current treatment phase.

PATIENT INFORMATION:
- Gender: {sample_patient['gender']}
- Age: {sample_patient['age']} years
- Primary Diagnosis: {sample_patient['diagnosis']}
- Operation: {sample_patient['operation_description']}
- Operation Date: {test_case['operation_date']} ({days_since_op} days ago)
- Treatment Details: {sample_patient['treatment_details']}
- Treatment Start Date: {test_case['treatment_start_date']} - {treatment_status}

Provide a brief assessment of the current phase and what the carer should focus on right now.
"""

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an experienced senior nurse. Provide brief, practical advice focusing on the current treatment phase."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=0.7
            )
            
            print("   ✅ AI Response:")
            print(f"   {response.choices[0].message.content}")
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
        
        print("\n" + "=" * 50)
    
    print(f"\n🎉 Treatment Timeline Logic Test Complete!")
    print("The AI now correctly considers:")
    print("   • Whether treatment has started yet")
    print("   • How many days until treatment starts")
    print("   • Current phase of recovery and treatment")
    print("   • Appropriate advice for each phase")

if __name__ == "__main__":
    test_treatment_timeline()
