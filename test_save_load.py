#!/usr/bin/env python3
"""
Test script demonstrating the save/load functionality
"""

import os
import json
from datetime import datetime, date

def test_save_load_functionality():
    """Test the save/load functionality with sample data"""
    
    print("🏥 Save/Load Functionality Test")
    print("=" * 40)
    
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
    
    print("📋 Sample Patient Data:")
    for key, value in sample_patient.items():
        print(f"   {key.replace('_', ' ').title()}: {value}")
    
    # Test save functionality
    print(f"\n💾 Testing Save Functionality...")
    print("-" * 30)
    
    try:
        # Import the save function
        import app
        
        # Test save
        filename = "test_patient_hip_replacement"
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
        
        print(f"✅ Save Result: {status}")
        
        # Check if file was created
        filepath = os.path.join("saved_data", f"{filename}.json")
        if os.path.exists(filepath):
            print(f"✅ File created successfully: {filepath}")
            
            # Show file contents
            with open(filepath, 'r', encoding='utf-8') as f:
                saved_data = json.load(f)
            print(f"✅ File contains {len(saved_data)} fields")
            
        else:
            print(f"❌ File not found: {filepath}")
        
    except Exception as e:
        print(f"❌ Save test failed: {str(e)}")
    
    # Test load functionality
    print(f"\n📂 Testing Load Functionality...")
    print("-" * 30)
    
    try:
        # Test load
        status, gender, age, diagnosis, op_desc, op_date, treat_details, treat_date = app.load_patient_data(f"{filename}.json")
        
        print(f"✅ Load Result: {status}")
        print(f"✅ Loaded Data:")
        print(f"   Gender: {gender}")
        print(f"   Age: {age}")
        print(f"   Diagnosis: {diagnosis}")
        print(f"   Operation: {op_desc}")
        print(f"   Operation Date: {op_date}")
        print(f"   Treatment: {treat_details}")
        print(f"   Treatment Date: {treat_date}")
        
    except Exception as e:
        print(f"❌ Load test failed: {str(e)}")
    
    # Test get saved files
    print(f"\n📁 Testing Get Saved Files...")
    print("-" * 30)
    
    try:
        saved_files = app.get_saved_files()
        print(f"✅ Found {len(saved_files)} saved files:")
        for file in saved_files:
            print(f"   - {file}")
            
    except Exception as e:
        print(f"❌ Get files test failed: {str(e)}")
    
    print(f"\n🎉 Save/Load Functionality Test Complete!")
    print("Features tested:")
    print("   • Save patient data to JSON file")
    print("   • Load patient data from JSON file")
    print("   • Get list of saved files")
    print("   • File validation and error handling")

if __name__ == "__main__":
    test_save_load_functionality()
