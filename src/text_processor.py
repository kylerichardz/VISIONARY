from typing import BinaryIO
import docx

def process_uploaded_file(file: BinaryIO) -> str:
    """
    Process uploaded file and extract text content.
    
    Args:
        file (BinaryIO): Uploaded file object
        
    Returns:
        str: Extracted text content
    """
    file_extension = file.name.split('.')[-1].lower()
    
    if file_extension == 'txt':
        return file.read().decode('utf-8')
    
    elif file_extension == 'docx':
        doc = docx.Document(file)
        return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    
    elif file_extension == 'md':
        return file.read().decode('utf-8')
    
    else:
        raise ValueError(f"Unsupported file type: {file_extension}") 