# PDF Analysis Tool for Systematic Literature Review

**Version 1.0**
### Creator: Juhani Merilehto - @juhanimerilehto - Jyväskylä University of Applied Sciences (JAMK), Likes institute

![JAMK Likes Logo](./assets/likes_str_logo.png)

## Overview

A Python-based tool designed for supporting in **systematic literature review** analysis using OpenAI's GPT-4. This tool automates the process of analyzing academic PDFs by extracting text content and processing it through AI analysis. It was developed for the Strategic Exercise Information and Research unit in Likes Institute, at JAMK University of Applied Sciences. The tool provides a streamlined way to process multiple PDF documents and generate structured analysis outputs.

## Features

- **Automated PDF Processing**: Batch processing of multiple PDF documents
- **Text Extraction**: Reliable extraction of text content from PDF files
- **AI-Powered Analysis**: Integration with OpenAI's GPT-4 for comprehensive text analysis
- **Structured Output**: Consistent analysis format for each processed document
- **Error Handling**: Robust error management and reporting
- **Progress Tracking**: Clear feedback on processing status

## Hardware Requirements

- **CPU:** Any modern processor capable of running Python
- **RAM:** 8GB minimum, 16GB recommended
- **Storage:** Space dependent on PDF collection size
- **Internet:** Required for API communication

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/juhanimerilehto/llm-literature-review-tool.git
cd pdf-analysis-tool
```

### 2. Create a virtual environment:
```bash
python -m venv pdf-env
source pdf-env/bin/activate  # For Windows: pdf-env\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Configure API Key:
Insert API key into the codeblock:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Basic usage:
```bash
python aislr.py
```

With custom parameters:
```bash
python aislr.py --input_folder "./PDFs" --output_folder "./Analysis" --max_tokens 4000
```

## Configuration Parameters

- `input_folder`: Directory containing PDF files (default: "./PDFs")
- `output_folder`: Directory for analysis output (default: "./Texts")
- `max_tokens`: Maximum tokens for API response (default: 4000)
- Custom prompt modifications available in the script

## File Structure

```plaintext
llm-literature-review-tool/
├── assets/
│   └── likes_str_logo.png
├── aislr.py
├── requirements.txt
└── README.md
```

## Credits

- **Juhani Merilehto (@juhanimerilehto)** – Specialist, Data and Statistics
- **JAMK Likes** – Organization sponsor

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Notes

- Ensure your OpenAI API key has sufficient credits
- Large PDF collections may require significant processing time
- Consider API usage costs when processing large volumes
- Regularly check the output folder for analysis results