#!/usr/bin/env python3
"""
Demo script showing the new specific advice feature
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime, date

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def demo_specific_advice():
    """Demonstrate the specific advice feature with sample questions"""
    
    # Sample patient data
    sample_patient = {
        "gender": "Male",
        "age": 72,
        "diagnosis": "Knee replacement surgery",
        "operation_description": "Total knee arthroplasty (left knee) due to severe osteoarthritis and bone-on-bone contact",
        "operation_date": "2024-01-05",
        "treatment_details": "Physical therapy 2x weekly, pain management with prescribed medications, wound care monitoring, mobility assistance",
        "treatment_start_date": "2024-01-07"
    }
    
    # Sample questions carers might ask
    sample_questions = [
        "How can I help manage his pain at home?",
        "What exercises are safe for him to do on his own?",
        "When should I be concerned about swelling in his knee?",
        "How can I help him get in and out of bed safely?",
        "What signs should I watch for that indicate infection?"
    ]
    
    print("🏥 AI-Powered Patient Care System - Specific Advice Demo")
    print("=" * 60)
    print("\n📋 Sample Patient Information:")
    for key, value in sample_patient.items():
        print(f"   {key.replace('_', ' ').title()}: {value}")
    
    print(f"\n💬 Sample Questions Carers Might Ask:")
    for i, question in enumerate(sample_questions, 1):
        print(f"   {i}. {question}")
    
    print(f"\n🤖 Generating AI Responses to Sample Questions...")
    print("-" * 60)
    
    # Calculate days since operation
    op_date = datetime.strptime(sample_patient["operation_date"], "%Y-%m-%d").date()
    treat_date = datetime.strptime(sample_patient["treatment_start_date"], "%Y-%m-%d").date()
    today = date.today()
    
    days_since_op = (today - op_date).days
    days_since_treatment = (today - treat_date).days
    
    for i, question in enumerate(sample_questions[:2], 1):  # Show first 2 examples
        print(f"\n🔍 QUESTION {i}: {question}")
        print("-" * 40)
        
        try:
            # Create specific advice prompt
            prompt = f"""
You are an experienced senior nurse with the knowledge of a senior consultant. A carer is asking for specific advice about their patient. Please provide detailed, practical guidance.

PATIENT INFORMATION:
- Gender: {sample_patient['gender']}
- Age: {sample_patient['age']} years
- Primary Diagnosis: {sample_patient['diagnosis']}
- Operation: {sample_patient['operation_description']}
- Operation Date: {sample_patient['operation_date']} ({days_since_op} days ago)
- Treatment Details: {sample_patient['treatment_details']}
- Treatment Start Date: {sample_patient['treatment_start_date']} ({days_since_treatment} days ago)

CARER'S SPECIFIC QUESTION:
"{question}"

Please provide:
1. **DIRECT ANSWER**: Address the specific question with practical guidance
2. **STEP-BY-STEP INSTRUCTIONS**: Clear, actionable steps the carer can follow
3. **IMPORTANT CONSIDERATIONS**: Things to be aware of or monitor
4. **WHEN TO SEEK HELP**: Signs that indicate the need for medical attention
5. **ADDITIONAL TIPS**: Extra helpful information related to the question

Be empathetic, specific, and practical. Focus on what the carer can do right now to help their patient.
"""

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an experienced senior nurse with extensive clinical knowledge. Provide practical, evidence-based nursing advice for patient carers. Be empathetic and specific in your guidance."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1200,
                temperature=0.7
            )
            
            print("✅ AI Response:")
            print(response.choices[0].message.content)
            
        except Exception as e:
            print(f"❌ Error generating response: {str(e)}")
        
        print("\n" + "=" * 60)
    
    print(f"\n🎉 Demo completed! The specific advice feature allows carers to:")
    print("   • Ask targeted questions about their patient's care")
    print("   • Get personalized, practical guidance")
    print("   • Receive step-by-step instructions")
    print("   • Learn about warning signs to watch for")
    print("   • Get additional tips and considerations")

if __name__ == "__main__":
    demo_specific_advice()
