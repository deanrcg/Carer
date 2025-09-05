# AI-Powered Patient Care System

A Gradio-based web application that collects patient information and provides AI-powered nursing advice from an experienced senior nurse perspective.

## Features

- **Patient Demographics**: Gender and age collection
- **Medical Information**: Diagnosis and operation details
- **Treatment Tracking**: Treatment details and start dates
- **AI Nursing Advice**: Expert guidance from an AI nurse with senior consultant knowledge
- **Specific Question Support**: Ask targeted questions and get personalized advice
- **Data Export**: JSON format output for easy integration
- **User-Friendly Interface**: Clean, intuitive form design with real-time AI consultation

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

## Usage

1. Run the application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:7860`

3. Fill in the patient information form with:
   - Gender selection
   - Age (numeric input)
   - Diagnosis (text)
   - Operation description and date
   - Treatment details and start date

4. Click "Submit & Get AI Advice" to process the data and receive expert nursing guidance

5. View the AI-generated nursing advice and structured JSON record

6. **Ask Specific Questions**: Use the "Ask Specific Questions" section to get personalized advice on any aspect of patient care

7. Type your question and click "Ask AI Nurse" for targeted guidance

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
