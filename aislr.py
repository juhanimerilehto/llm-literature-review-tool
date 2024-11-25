
# PDF Analysis and OpenAI GPT-4 Integration Script for Systematic Literature Review
# ------------------------------------------------------------------------------
# This script processes PDF files using OpenAI's GPT-4 to conduct systematic literature review analysis.
# It extracts text from PDFs and analyzes them in the given context and format.
#
# Tämä skripti käsittelee PDF-tiedostoja käyttäen OpenAI:n GPT-4:ää systemaattisen kirjallisuuskatsauksen analyysiin.
# Se poimii tekstin PDF-tiedostoista ja analysoi niitä annetun kontekstin ja formaatin mukaisesti.
#
# Author: @juhanimerilehto
# Version: 1.0
# Created: 20.11.2024

import os
import PyPDF2
import openai

# Initialize OpenAI client with API key
client = openai.Client(api_key='YOUR_OPENAI_API_KEY')  # Replace with your API key

def extract_text_from_pdf(pdf_path):
    """
    Extract text content from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text or error message if no text found
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text if text else "No text extracted."

def query_openai_api(text, api_key, max_tokens=120000):
    """
    Query OpenAI API with extracted text for analysis.
    
    Args:
        text (str): Text to analyze
        api_key (str): OpenAI API key
        max_tokens (int): Maximum tokens for response
        
    Returns:
        str: API response or error message
    """
    # System prompt defining the analysis context and requirements
    prompt = """You are an advanced text analysis assistant specializing in analyzing academic articles, 
    both theoretical pieces and empirical studies."""
    
    # Detailed instructions for the analysis
    instructions = """
    Read and analyze the provided text very accurately and comprehensively.
    
    Context:
    - This analysis is for a Health Sciences MSc. Thesis Systematic Literature Review
    - Currently in the full-text screening phase
    - Focus: Physical activity interventions for elderly people
    - Analytical lens: Social-Ecological Model of Health Behavior
    
    Research Question:
    How have physical activity interventions and their effectiveness been studied 
    and implemented among elderly populations in community settings?
    
    Please provide:
    A) Critical assessment of text relevance to context (yes/no with brief explanation)
    B) Summary of article's main objectives, research questions, and relevance to thesis
    C) Detailed study design analysis
    D) Primary findings related to intervention effectiveness, adherence factors, and health outcomes in elderly populations
    """
    
    full_prompt = prompt + text + instructions
    openai.api_key = api_key
    
    try:
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[{"role": "system", "content": full_prompt}],
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error in API response: {e}"

def process_pdfs(input_folder, output_folder, api_key, max_tokens=1250):
    """
    Process multiple PDFs from input folder and save analysis results to output folder.
    
    Args:
        input_folder (str): Path to folder containing PDFs
        output_folder (str): Path to save analysis results
        api_key (str): OpenAI API key
        max_tokens (int): Maximum tokens for API response
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('.pdf', '.txt'))
            
            try:
                text = extract_text_from_pdf(pdf_path)
                response_content = query_openai_api(text, api_key, max_tokens)
                with open(output_path, 'w', encoding='utf-8') as file:
                    file.write(response_content)
                print(f"Successfully processed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

def main():
    # Configuration
    api_key = "YOUR_OPENAI_API_KEY"  # Replace with your API key
    input_folder = "./PDFs"  # Folder containing PDF files
    output_folder = "./Texts"  # Folder for analysis results
    max_tokens = 4000  # Adjust based on your requirements
    
    # Process PDFs
    process_pdfs(input_folder, output_folder, api_key, max_tokens)

if __name__ == "__main__":
    main()