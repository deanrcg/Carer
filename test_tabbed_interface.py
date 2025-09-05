#!/usr/bin/env python3
"""
Test script demonstrating the new tabbed interface functionality
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime, date

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_tabbed_interface():
    """Test the new tabbed interface with sample data"""
    
    print("🏥 Tabbed Interface Test")
    print("=" * 50)
    
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
    
    print("📋 Sample Patient Data:")
    for key, value in sample_patient.items():
        print(f"   {key.replace('_', ' ').title()}: {value}")
    
    print(f"\n🎯 Testing Tabbed Interface Features...")
    print("-" * 50)
    
    # Test Patient-Focused Advice
    print(f"\n👤 TAB 1: Patient Advice")
    print("-" * 30)
    
    try:
        import app
        
        # Test patient-focused advice
        patient_advice = app.get_patient_focused_advice(
            sample_patient["gender"],
            sample_patient["age"],
            sample_patient["diagnosis"],
            sample_patient["operation_description"],
            sample_patient["operation_date"],
            sample_patient["treatment_details"],
            sample_patient["treatment_start_date"]
        )
        
        print("✅ Patient-Focused Advice Generated:")
        print(patient_advice[:200] + "..." if len(patient_advice) > 200 else patient_advice)
        
        # Test patient question
        patient_question = "How long will my recovery take?"
        patient_answer = app.get_patient_question_answer(
            sample_patient["gender"],
            sample_patient["age"],
            sample_patient["diagnosis"],
            sample_patient["operation_description"],
            sample_patient["operation_date"],
            sample_patient["treatment_details"],
            sample_patient["treatment_start_date"],
            patient_question
        )
        
        print(f"\n✅ Patient Question Answer:")
        print(f"Question: {patient_question}")
        print(f"Answer: {patient_answer[:200]}..." if len(patient_answer) > 200 else f"Answer: {patient_answer}")
        
    except Exception as e:
        print(f"❌ Patient advice test failed: {str(e)}")
    
    # Test Carer-Focused Advice
    print(f"\n👥 TAB 2: Carer Advice")
    print("-" * 30)
    
    try:
        # Test carer-focused advice
        carer_advice = app.get_carer_focused_advice(
            sample_patient["gender"],
            sample_patient["age"],
            sample_patient["diagnosis"],
            sample_patient["operation_description"],
            sample_patient["operation_date"],
            sample_patient["treatment_details"],
            sample_patient["treatment_start_date"]
        )
        
        print("✅ Carer-Focused Advice Generated:")
        print(carer_advice[:200] + "..." if len(carer_advice) > 200 else carer_advice)
        
        # Test carer question
        carer_question = "How can I help with pain management?"
        carer_answer = app.get_carer_question_answer(
            sample_patient["gender"],
            sample_patient["age"],
            sample_patient["diagnosis"],
            sample_patient["operation_description"],
            sample_patient["operation_date"],
            sample_patient["treatment_details"],
            sample_patient["treatment_start_date"],
            carer_question
        )
        
        print(f"\n✅ Carer Question Answer:")
        print(f"Question: {carer_question}")
        print(f"Answer: {carer_answer[:200]}..." if len(carer_answer) > 200 else f"Answer: {carer_answer}")
        
    except Exception as e:
        print(f"❌ Carer advice test failed: {str(e)}")
    
    # Test Save/Load functionality
    print(f"\n💾 TAB 3: Save/Load Functionality")
    print("-" * 30)
    
    try:
        # Test save
        filename = "test_tabbed_patient"
        status, _ = app.save_patient_data(
            sample_patient["gender"],
            sample_patient["age"],
            sample_patient["diagnosis"],
            sample_patient["operation_description"],
            sample_patient["operation_date"],
            sample_patient["treatment_details"],
            sample_patient["treatment_start_date"],
            filename
        )
        
        print(f"✅ Save Test: {status}")
        
        # Test load
        status, gender, age, diagnosis, op_desc, op_date, treat_details, treat_date = app.load_patient_data(f"{filename}.json")
        print(f"✅ Load Test: {status}")
        
    except Exception as e:
        print(f"❌ Save/Load test failed: {str(e)}")
    
    print(f"\n🎉 Tabbed Interface Test Complete!")
    print("New Features:")
    print("   📋 Tab 1: Patient Info & Save/Load - Clean data management")
    print("   👤 Tab 2: Patient Advice - Patient-focused guidance and Q&A")
    print("   👥 Tab 3: Carer Advice - Carer-focused guidance and Q&A")
    print("   🎯 Specialized AI prompts for different perspectives")
    print("   💬 Separate Q&A sections for patients and carers")

if __name__ == "__main__":
    test_tabbed_interface()
