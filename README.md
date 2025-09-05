# AI-Powered Patient Care System

A comprehensive Gradio-based web application with a clean tabbed interface that provides AI-powered nursing advice tailored for both patients and carers.

## Features

- **Clean Tabbed Interface**: Organized into 3 logical sections for better user experience
- **Patient Demographics**: Gender and age collection
- **Medical Information**: Diagnosis and operation details
- **Treatment Tracking**: Treatment details and start dates with timeline awareness
- **Dual-Perspective AI Advice**: Separate guidance for patients and carers
- **Specialized Q&A**: Patient-focused and carer-focused question answering
- **Save/Load Patient Data**: Persistent data management with JSON files
- **Data Export**: JSON format output for easy integration
- **User-Friendly Interface**: Clean, intuitive design with real-time AI consultation

## AI Nursing Advisor

The system includes an AI-powered nursing advisor that provides:

1. **Patient Stage Assessment**: Determines the current stage of recovery/treatment
2. **Carer Expectations**: What to expect during the current stage
3. **Caring Guidance**: Specific daily care activities and monitoring
4. **Warning Signs**: Red flags requiring immediate medical attention
5. **Recovery Timeline**: Expected progression and milestones
6. **Emotional Support**: Psychological support guidance for carers

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your OpenAI API key:
   - Create a `.env` file in the project directory
   - Add your OpenAI API key: `OPENAI_API_KEY=your_actual_api_key_here`
   - Get your API key from: https://platform.openai.com/api-keys

## Tabbed Interface

The application is organized into three clean, focused tabs:

### 📋 Tab 1: Patient Info & Save/Load
- **Patient Information Collection**: Enter demographics, diagnosis, operation details
- **Save/Load Functionality**: Persistent data management with JSON files
- **Patient Record Display**: Structured JSON output for easy reference

### 👤 Tab 2: Patient Advice
- **Patient-Focused Guidance**: AI advice tailored for the patient's perspective
- **Patient Q&A**: Ask questions from the patient's viewpoint
- **Encouraging Language**: Uses "you" language and empowering tone
- **Self-Care Focus**: Emphasizes what patients can do for themselves

### 👥 Tab 3: Carer Advice
- **Carer-Focused Guidance**: AI advice tailored for caregivers
- **Carer Q&A**: Ask questions from the carer's perspective
- **Practical Instructions**: Step-by-step caregiving guidance
- **Monitoring Focus**: Emphasizes what carers should watch for

## Usage

1. Run the application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:7860`

3. **Tab 1 - Patient Info & Save/Load**: Fill in patient information and manage saved data
   - Enter patient demographics and medical details
   - Save patient data to files for future reference
   - Load previously saved patient information
   - View structured JSON patient record

4. **Tab 2 - Patient Advice**: Get advice tailored for the patient
   - Click "Get Patient Advice" for comprehensive patient-focused guidance
   - Ask specific questions from the patient's perspective
   - Receive encouraging, empowering advice using "you" language

5. **Tab 3 - Carer Advice**: Get advice tailored for carers
   - Click "Get Carer Advice" for comprehensive caregiving guidance
   - Ask specific questions from the carer's perspective
   - Receive practical, actionable caregiving instructions

## Form Fields

- **Gender**: Dropdown selection (Male, Female, Other, Prefer not to say)
- **Age**: Numeric input (0-150 years)
- **Diagnosis**: Text input for primary medical diagnosis
- **Operation Description**: Multi-line text for procedure details
- **Operation Date**: Date input field (YYYY-MM-DD format)
- **Treatment Details**: Multi-line text for treatment plan
- **Treatment Start Date**: Date input field (YYYY-MM-DD format)

## AI Output

### General Nursing Advice
The AI nursing advisor provides comprehensive guidance including:

- **Stage Assessment**: Current recovery/treatment phase
- **Carer Expectations**: What to expect during this stage
- **Daily Care Activities**: Specific tasks and monitoring
- **Warning Signs**: Symptoms requiring immediate attention
- **Recovery Timeline**: Expected milestones and progression
- **Emotional Support**: Psychological care guidance

### Specific Question Support
For targeted questions, the AI provides:

- **Direct Answer**: Addresses the specific question with practical guidance
- **Step-by-Step Instructions**: Clear, actionable steps the carer can follow
- **Important Considerations**: Things to be aware of or monitor
- **When to Seek Help**: Signs that indicate the need for medical attention
- **Additional Tips**: Extra helpful information related to the question

### Example Questions Carers Can Ask:
- "How can I help with pain management?"
- "What exercises are safe for my patient?"
- "When should I be concerned about swelling?"
- "How can I help with mobility and transfers?"
- "What signs indicate infection?"
- "How can I help with medication management?"

## Treatment Timeline Awareness

The AI system intelligently considers treatment timing:

- **Future Treatment**: Provides pre-treatment guidance and preparation advice
- **Treatment Starting Today**: Focuses on immediate transition and first-day care
- **Ongoing Treatment**: Offers current treatment phase guidance and monitoring

The AI automatically calculates days since operation and treatment status to provide contextually appropriate advice for each phase of the patient's journey.

## Save/Load Functionality

The system includes comprehensive data persistence features:

### Saving Patient Data
- **File Format**: JSON files stored in `saved_data/` directory
- **Automatic Naming**: Adds `.json` extension if not provided
- **Complete Records**: Saves all patient information including timestamps
- **Error Handling**: Validates data before saving

### Loading Patient Data
- **File Browser**: Dropdown shows all saved patient files
- **Automatic Population**: Loads all form fields with saved data
- **Status Feedback**: Shows success/error messages
- **Data Validation**: Checks file existence and format

### File Management
- **Organized Storage**: All files stored in dedicated `saved_data/` folder
- **Easy Access**: Simple dropdown interface for file selection
- **Backup Ready**: JSON format allows easy backup and sharing

## Requirements

- Python 3.7+
- Gradio 4.44.0
- OpenAI 1.3.0
- python-dotenv 1.0.0
- Valid OpenAI API key

## Testing

Run the test suite to verify everything is working:
```bash
python test_app.py
```

This will check:
- All required imports
- Environment setup (API key)
- App structure and functionality
