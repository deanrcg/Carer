import gradio as gr
from datetime import datetime, date
import json
import os
from dotenv import load_dotenv
from openai import OpenAI
import glob

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_nursing_advice(gender, age, diagnosis, operation_description, operation_date, treatment_details, treatment_start_date):
    """
    Get AI-powered nursing advice based on patient information
    """
    try:
        # Calculate days since operation and treatment start
        op_date = datetime.strptime(operation_date, "%Y-%m-%d").date()
        treat_date = datetime.strptime(treatment_start_date, "%Y-%m-%d").date()
        today = date.today()
        
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
        
        # Create comprehensive prompt for AI nurse
        prompt = f"""
You are an experienced senior nurse with the knowledge of a senior consultant. Based on the following patient information, provide comprehensive nursing advice for the carer.

PATIENT INFORMATION:
- Gender: {gender}
- Age: {age} years
- Primary Diagnosis: {diagnosis}
- Operation: {operation_description}
- Operation Date: {operation_date} ({days_since_op} days ago)
- Treatment Details: {treatment_details}
- Treatment Start Date: {treatment_start_date} - {treatment_status}

Please provide advice in the following structure:

1. **PATIENT STAGE ASSESSMENT**: What stage of recovery/treatment is this patient currently in? Consider whether treatment has started yet.

2. **CARER EXPECTATIONS**: What should the carer expect during this stage? Focus on the current situation (pre-treatment, starting treatment, or ongoing treatment).

3. **CARING GUIDANCE**: Specific ways the carer can help the patient, including:
   - Daily care activities appropriate for current stage
   - Monitoring signs to watch for
   - Comfort measures
   - Medication management (if applicable)
   - Mobility and activity recommendations

4. **WARNING SIGNS**: Red flags or symptoms that require immediate medical attention

5. **RECOVERY TIMELINE**: Expected progression and milestones, considering treatment timing

6. **EMOTIONAL SUPPORT**: How to provide psychological support to the patient

IMPORTANT: Tailor your advice based on whether treatment has started, is starting today, or is scheduled for the future. Provide appropriate guidance for the current phase.
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
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"❌ Error getting AI advice: {str(e)}\n\nPlease check your OpenAI API key and internet connection."

def collect_patient_info(gender, age, diagnosis, operation_description, operation_date, treatment_details, treatment_start_date):
    """
    Collect and process patient information
    """
    # Validate inputs
    if not all([gender, age, diagnosis, operation_description, operation_date, treatment_details, treatment_start_date]):
        return "Please fill in all fields before submitting.", None, "Please complete all fields to get AI nursing advice."
    
    # Create patient record
    patient_record = {
        "timestamp": datetime.now().isoformat(),
        "gender": gender,
        "age": int(age),
        "diagnosis": diagnosis,
        "operation": {
            "description": operation_description,
            "date": operation_date
        },
        "treatment": {
            "details": treatment_details,
            "start_date": treatment_start_date
        }
    }
    
    # Convert to JSON for display
    json_output = json.dumps(patient_record, indent=2)
    
    # Success message
    success_msg = f"✅ Patient information collected successfully!\n\nPatient: {gender}, Age {age}\nDiagnosis: {diagnosis}\nOperation Date: {operation_date}\nTreatment Start: {treatment_start_date}"
    
    # Get AI nursing advice
    ai_advice = get_nursing_advice(gender, age, diagnosis, operation_description, operation_date, treatment_details, treatment_start_date)
    
    return success_msg, json_output, ai_advice

def get_specific_advice(gender, age, diagnosis, operation_description, operation_date, treatment_details, treatment_start_date, specific_question):
    """
    Get AI-powered specific advice based on carer's question
    """
    try:
        # Calculate days since operation and treatment start
        op_date = datetime.strptime(operation_date, "%Y-%m-%d").date()
        treat_date = datetime.strptime(treatment_start_date, "%Y-%m-%d").date()
        today = date.today()
        
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
        
        # Create specific advice prompt
        prompt = f"""
You are an experienced senior nurse with the knowledge of a senior consultant. A carer is asking for specific advice about their patient. Please provide detailed, practical guidance.

PATIENT INFORMATION:
- Gender: {gender}
- Age: {age} years
- Primary Diagnosis: {diagnosis}
- Operation: {operation_description}
- Operation Date: {operation_date} ({days_since_op} days ago)
- Treatment Details: {treatment_details}
- Treatment Start Date: {treatment_start_date} - {treatment_status}

CARER'S SPECIFIC QUESTION:
"{specific_question}"

Please provide:
1. **DIRECT ANSWER**: Address the specific question with practical guidance appropriate for the current treatment phase
2. **STEP-BY-STEP INSTRUCTIONS**: Clear, actionable steps the carer can follow
3. **IMPORTANT CONSIDERATIONS**: Things to be aware of or monitor
4. **WHEN TO SEEK HELP**: Signs that indicate the need for medical attention
5. **ADDITIONAL TIPS**: Extra helpful information related to the question

IMPORTANT: Consider whether treatment has started yet when providing your advice. Tailor your response to the current phase (pre-treatment, starting treatment, or ongoing treatment).

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
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"❌ Error getting specific advice: {str(e)}\n\nPlease check your OpenAI API key and internet connection."

def save_patient_data(gender, age, diagnosis, operation_description, operation_date, treatment_details, treatment_start_date, filename):
    """
    Save patient data to a JSON file
    """
    try:
        if not filename:
            return "Please enter a filename to save the patient data.", None
        
        # Create patient record
        patient_record = {
            "timestamp": datetime.now().isoformat(),
            "gender": gender,
            "age": int(age) if age else None,
            "diagnosis": diagnosis,
            "operation": {
                "description": operation_description,
                "date": operation_date
            },
            "treatment": {
                "details": treatment_details,
                "start_date": treatment_start_date
            }
        }
        
        # Ensure saved_data directory exists
        os.makedirs("saved_data", exist_ok=True)
        
        # Add .json extension if not present
        if not filename.endswith('.json'):
            filename += '.json'
        
        filepath = os.path.join("saved_data", filename)
        
        # Save to file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(patient_record, f, indent=2, ensure_ascii=False)
        
        return f"✅ Patient data saved successfully to {filename}", None
        
    except Exception as e:
        return f"❌ Error saving patient data: {str(e)}", None

def load_patient_data(filename):
    """
    Load patient data from a JSON file
    """
    try:
        if not filename:
            return "Please select a file to load.", None, None, None, None, None, None
        
        # Ensure saved_data directory exists
        os.makedirs("saved_data", exist_ok=True)
        
        filepath = os.path.join("saved_data", filename)
        
        if not os.path.exists(filepath):
            return f"❌ File {filename} not found.", None, None, None, None, None, None
        
        # Load from file
        with open(filepath, 'r', encoding='utf-8') as f:
            patient_record = json.load(f)
        
        # Extract data
        gender = patient_record.get("gender", "")
        age = patient_record.get("age", "")
        diagnosis = patient_record.get("diagnosis", "")
        operation_description = patient_record.get("operation", {}).get("description", "")
        operation_date = patient_record.get("operation", {}).get("date", "")
        treatment_details = patient_record.get("treatment", {}).get("details", "")
        treatment_start_date = patient_record.get("treatment", {}).get("start_date", "")
        
        return f"✅ Patient data loaded successfully from {filename}", gender, age, diagnosis, operation_description, operation_date, treatment_details, treatment_start_date
        
    except Exception as e:
        return f"❌ Error loading patient data: {str(e)}", None, None, None, None, None, None

def get_saved_files():
    """
    Get list of saved patient files
    """
    try:
        os.makedirs("saved_data", exist_ok=True)
        files = glob.glob("saved_data/*.json")
        filenames = [os.path.basename(f) for f in files]
        return filenames if filenames else ["No saved files found"]
    except Exception as e:
        return [f"Error: {str(e)}"]

def clear_form():
    """Clear all form fields"""
    return None, None, None, None, None, None, None, "", "", ""

# Create the Gradio interface
with gr.Blocks(title="AI-Powered Patient Care System", theme=gr.themes.Soft()) as app:
    gr.Markdown("# 🏥 AI-Powered Patient Care System")
    gr.Markdown("Collect patient information and receive expert nursing advice powered by AI")
    
    # Patient Information Section
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## 📋 Patient Information")
            
            gender = gr.Dropdown(
                choices=["Male", "Female", "Other", "Prefer not to say"],
                label="Gender",
                info="Select patient's gender"
            )
            
            age = gr.Number(
                label="Age",
                info="Patient's age in years",
                minimum=0,
                maximum=150,
                step=1
            )
            
            diagnosis = gr.Textbox(
                label="Diagnosis",
                info="Primary medical diagnosis",
                placeholder="Enter the main diagnosis..."
            )
            
            operation_description = gr.Textbox(
                label="Operation Description",
                info="Description of the surgical procedure",
                placeholder="Describe the operation performed...",
                lines=3
            )
            
            operation_date = gr.Textbox(
                label="Operation Date",
                info="Date when the operation was performed (YYYY-MM-DD)",
                placeholder="2024-01-15",
                value=date.today().strftime("%Y-%m-%d")
            )
            
            treatment_details = gr.Textbox(
                label="Treatment Details",
                info="Details about ongoing treatment",
                placeholder="Describe the treatment plan...",
                lines=3
            )
            
            treatment_start_date = gr.Textbox(
                label="Treatment Start Date",
                info="Date when treatment began (YYYY-MM-DD)",
                placeholder="2024-01-15",
                value=date.today().strftime("%Y-%m-%d")
            )
            
            with gr.Row():
                submit_btn = gr.Button("Submit & Get AI Advice", variant="primary", size="lg")
                clear_btn = gr.Button("Clear Form", variant="secondary")
            
            # Save/Load Section
            gr.Markdown("## 💾 Save & Load Patient Data")
            
            with gr.Row():
                with gr.Column(scale=2):
                    save_filename = gr.Textbox(
                        label="Save As",
                        info="Enter filename to save patient data",
                        placeholder="patient_john_doe",
                        lines=1
                    )
                    save_btn = gr.Button("💾 Save Patient Data", variant="secondary")
                
                with gr.Column(scale=2):
                    load_file_dropdown = gr.Dropdown(
                        choices=get_saved_files(),
                        label="Load Patient Data",
                        info="Select a saved patient file to load",
                        value=None
                    )
                    load_btn = gr.Button("📂 Load Patient Data", variant="secondary")
            
            save_load_status = gr.Textbox(
                label="Save/Load Status",
                interactive=False,
                lines=2,
                placeholder="Save/load status will appear here..."
            )
        
        with gr.Column(scale=1):
            gr.Markdown("## 🤖 AI Nursing Advice")
            
            output_message = gr.Textbox(
                label="Status",
                interactive=False,
                lines=3
            )
            
            ai_advice_output = gr.Textbox(
                label="Expert Nursing Advice",
                interactive=False,
                lines=15,
                placeholder="AI nursing advice will appear here after submitting patient information..."
            )
            
            gr.Markdown("## 📊 Patient Record")
            
            json_output = gr.JSON(
                label="Patient Record (JSON)"
            )
    
    # Specific Advice Section
    gr.Markdown("---")
    gr.Markdown("## 💬 Ask Specific Questions")
    gr.Markdown("Have a specific question about your patient's care? Ask our AI nurse for personalized advice!")
    
    with gr.Row():
        with gr.Column(scale=2):
            specific_question = gr.Textbox(
                label="Your Question",
                info="Ask any specific question about your patient's care, recovery, or what you should do",
                placeholder="e.g., 'How can I help with pain management?', 'What exercises are safe?', 'When should I be concerned about swelling?'",
                lines=3
            )
            
            ask_btn = gr.Button("Ask AI Nurse", variant="primary", size="lg")
        
        with gr.Column(scale=3):
            specific_advice_output = gr.Textbox(
                label="AI Nurse's Specific Advice",
                interactive=False,
                lines=15,
                placeholder="Your specific advice will appear here after asking a question..."
            )
    
    # Event handlers
    submit_btn.click(
        fn=collect_patient_info,
        inputs=[gender, age, diagnosis, operation_description, operation_date, treatment_details, treatment_start_date],
        outputs=[output_message, json_output, ai_advice_output]
    )
    
    ask_btn.click(
        fn=get_specific_advice,
        inputs=[gender, age, diagnosis, operation_description, operation_date, treatment_details, treatment_start_date, specific_question],
        outputs=[specific_advice_output]
    )
    
    save_btn.click(
        fn=save_patient_data,
        inputs=[gender, age, diagnosis, operation_description, operation_date, treatment_details, treatment_start_date, save_filename],
        outputs=[save_load_status]
    )
    
    load_btn.click(
        fn=load_patient_data,
        inputs=[load_file_dropdown],
        outputs=[save_load_status, gender, age, diagnosis, operation_description, operation_date, treatment_details, treatment_start_date]
    )
    
    clear_btn.click(
        fn=clear_form,
        outputs=[gender, age, diagnosis, operation_description, operation_date, treatment_details, treatment_start_date, output_message, ai_advice_output, specific_advice_output]
    )

if __name__ == "__main__":
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )