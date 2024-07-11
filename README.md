# Extracting-information-from-PDF-using-LangChain-and-OpenAI-APIs
This project focusses on extracting text from the PDF documents which contain more complex structures like tables. We will be requesting the model to extract the text from PDF table and structure the ouput in JSON format.

Here we will be using the OpenAI models and Langchain to extracts the texts from tables inside the PDF files. We can use two libraries for extracting the information from PDF and they are:
1. PyPDFLoader
2. PyMuPDFLoader.

In the context of Langchain, both `PyPDFLoader` and `PyMuPDFLoader` are tools used for loading and processing PDF documents. However, they rely on different underlying libraries and have distinct capabilities and use cases. Here are the primary differences between the two:

### PyPDFLoader
1. **Underlying Library**: PyPDFLoader typically relies on the `PyPDF2` library.
2. **Functionality**:
   - It focuses on extracting text from PDF documents.
   - Can handle a wide variety of PDF formats but might struggle with more complex layouts or embedded objects.
   - Usually offers basic text extraction without much processing of the layout or structure of the document.
3. **Use Case**: Suitable for simple text extraction tasks where the PDF documents have a straightforward layout.

### PyMuPDFLoader
1. **Underlying Library**: PyMuPDFLoader uses the `PyMuPDF` library, also known as `fitz`.
2. **Functionality**:
   - Provides more advanced features for handling PDFs, including text extraction, image extraction, and more.
   - Better at handling complex PDF layouts, including documents with images, annotations, and various formatting elements.
   - Offers capabilities to work with the document structure more effectively, such as retrieving text by blocks or paragraphs.
3. **Use Case**: Ideal for more complex PDFs where advanced extraction capabilities are needed, such as extracting both text and images or dealing with documents that have complex formatting.


## Reference
https://github.com/ronidas39/LLMtutoria



