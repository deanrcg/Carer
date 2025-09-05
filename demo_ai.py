#!/usr/bin/env python3
"""
Demo script showing AI nursing advice capabilities
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime, date

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def demo_ai_advice():
    """Demonstrate AI nursing advice with sample patient data"""
    
    # Sample patient data
    sample_patient = {
        "gender": "Female",
        "age": 65,
        "diagnosis": "Hip replacement surgery",
        "operation_description": "Total hip arthroplasty (right hip) due to severe osteoarthritis",
        "operation_date": "2024-01-10",
        "treatment_details": "Physical therapy 3x weekly, pain management with prescribed medications, wound care monitoring",
        "treatment_start_date": "2024-01-12"
    }
    
    print("🏥 AI-Powered Patient Care System - Demo")
    print("=" * 50)
    print("\n📋 Sample Patient Information:")
    for key, value in sample_patient.items():
        print(f"   {key.replace('_', ' ').title()}: {value}")
    
    print("\n🤖 Generating AI Nursing Advice...")
    print("-" * 30)
    
    try:
        # Calculate days since operation
        op_date = datetime.strptime(sample_patient["operation_date"], "%Y-%m-%d").date()
        treat_date = datetime.strptime(sample_patient["treatment_start_date"], "%Y-%m-%d").date()
        today = date.today()
        
        days_since_op = (today - op_date).days
        days_since_treatment = (today - treat_date).days
        
        # Create prompt
        prompt = f"""
You are an experienced senior nurse with the knowledge of a senior consultant. Based on the following patient information, provide comprehensive nursing advice for the carer.

PATIENT INFORMATION:
- Gender: {sample_patient['gender']}
- Age: {sample_patient['age']} years
- Primary Diagnosis: {sample_patient['diagnosis']}
- Operation: {sample_patient['operation_description']}
- Operation Date: {sample_patient['operation_date']} ({days_since_op} days ago)
- Treatment Details: {sample_patient['treatment_details']}
- Treatment Start Date: {sample_patient['treatment_start_date']} ({days_since_treatment} days ago)

Please provide advice in the following structure:

1. **PATIENT STAGE ASSESSMENT**: What stage of recovery/treatment is this patient currently in?

2. **CARER EXPECTATIONS**: What should the carer expect during this stage?

3. **CARING GUIDANCE**: Specific ways the carer can help the patient, including:
   - Daily care activities
   - Monitoring signs to watch for
   - Comfort measures
   - Medication management (if applicable)
   - Mobility and activity recommendations

4. **WARNING SIGNS**: Red flags or symptoms that require immediate medical attention

5. **RECOVERY TIMELINE**: Expected progression and milestones

6. **EMOTIONAL SUPPORT**: How to provide psychological support to the patient

Please be specific, practical, and empathetic in your advice. Focus on actionable guidance that a carer can implement immediately.
"""

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an experienced senior nurse with extensive clinical knowledge. Provide practical, evidence-based nursing advice for patient carers."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        
        print("✅ AI Nursing Advice Generated Successfully!")
        print("\n" + "=" * 50)
        print("🤖 EXPERT NURSING ADVICE:")
        print("=" * 50)
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"❌ Error generating AI advice: {str(e)}")
        print("Please check your OpenAI API key and internet connection.")

if __name__ == "__main__":
    demo_ai_advice()
