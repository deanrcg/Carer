#!/usr/bin/env python3
"""
Test script to verify the dropdown bug fix
"""

import os
import app

def test_dropdown_fix():
    """Test that the dropdown updates after saving"""
    
    print("🐛 Testing Dropdown Bug Fix")
    print("=" * 40)
    
    # Check current files
    current_files = app.get_saved_files()
    print(f"📁 Current files in dropdown: {len(current_files)}")
    for file in current_files:
        print(f"   - {file}")
    
    # Test saving a new file
    print(f"\n💾 Testing save with dropdown update...")
    
    test_data = {
        "gender": "Male",
        "age": 45,
        "diagnosis": "Test diagnosis for dropdown fix",
        "operation_description": "Test operation",
        "operation_date": "2024-01-01",
        "treatment_details": "Test treatment",
        "treatment_start_date": "2024-01-02",
        "filename": "dropdown_test_patient"
    }
    
    try:
        status, updated_files = app.save_patient_data(
            test_data["gender"],
            test_data["age"],
            test_data["diagnosis"],
            test_data["operation_description"],
            test_data["operation_date"],
            test_data["treatment_details"],
            test_data["treatment_start_date"],
            test_data["filename"]
        )
        
        print(f"✅ Save result: {status}")
        print(f"📁 Updated files list: {len(updated_files)}")
        for file in updated_files:
            print(f"   - {file}")
        
        # Check if the new file is in the list
        if "dropdown_test_patient.json" in updated_files:
            print("✅ SUCCESS: New file appears in updated dropdown list!")
        else:
            print("❌ FAILED: New file not found in dropdown list")
            
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
    
    print(f"\n🎉 Dropdown bug fix test complete!")
    print("The dropdown should now update automatically after saving new files.")

if __name__ == "__main__":
    test_dropdown_fix()
